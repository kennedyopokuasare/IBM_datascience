# Import required libraries
# %%
import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html, Input, Output, callback

# %%
# Read the airline data into pandas dataframe
url = "./spacex_launch_dash.csv"
spacex_df = pd.read_csv(url)
max_payload = spacex_df["Payload Mass (kg)"].max()
min_payload = spacex_df["Payload Mass (kg)"].min()

dropdown_options = [
    {"label": f"{site}", "value": f"{site}"}
    for site in spacex_df["Launch Site"].unique()
]

min_payload = spacex_df["Payload Mass (kg)"].min()
max_payload = spacex_df["Payload Mass (kg)"].max()

# Create a dash application
app = dash.Dash(__name__)

# %%
# Create an app layout
app.layout = html.Div(
    children=[
        html.H1(
            "SpaceX Launch Records Dashboard",
            style={"textAlign": "center", "color": "#503D36", "font-size": 40},
        ),
        # TASK 1: Add a dropdown list to enable Launch Site selection
        # The default select value is for ALL sites
        # dcc.Dropdown(id='site-dropdown',...)
        html.Div(
            dcc.Dropdown(
                id="site-dropdown",
                options=dropdown_options,
                placeholder=" Select a report type",
                style={"width": "80%", "font-size": 20, "textAlign": "center"},
                clearable=False,
            )
        ),
        html.Br(),
        # TASK 2: Add a pie chart to show the total successful launches count for all sites
        # If a specific launch site was selected, show the Success vs. Failed counts for the site
        html.Div(dcc.Graph(id="success-pie-chart")),
        html.Br(),
        html.P("Payload range (Kg):"),
        # TASK 3: Add a slider to select payload range
        html.Div(dcc.RangeSlider(min_payload, max_payload, 1000, id="payload-slider")),
        # TASK 4: Add a scatter chart to show the correlation between payload and launch success
        html.Div(dcc.Graph(id="success-payload-scatter-chart")),
    ]
)

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output


@callback(
    Output(component_id="success-pie-chart", component_property="figure"),
    Input(component_id="site-dropdown", component_property="value"),
)
def update_pie_chart(site):
    """Update the pie chart based on the selected launch site.

    Args:
        site (str): The launch site selected from the dropdown. If 'ALL', show total successes by site.

    Returns:
        plotly.graph_objs._figure.Figure: A pie chart figure object.
    """

    fig = px.pie(
        spacex_df.groupby("Launch Site")["class"].sum().reset_index(),
        values="class",
        names="Launch Site",
        title="Total Success Launches By Site",
    )

    if site:
        print(site)
        filtered_df = spacex_df[spacex_df["Launch Site"] == site]
        filtered_df = filtered_df.groupby("class", as_index=False).agg(
            count=("class", "count")
        )
        filtered_df["class"] = filtered_df["class"].map({0: "Failure", 1: "Success"})

        fig = px.pie(
            filtered_df,
            values="count",
            names="class",
            title="Total Success and Failure for Launches Site " + site,
        )

    fig.update_layout()
    return fig


# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output

# %%
# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
# %%
