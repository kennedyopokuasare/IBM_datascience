import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html, Input, Output, callback


# Load the data using pandas
data = pd.read_csv(
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv"
)


dropdown_options = [
    {"label": "Yearly Statistics", "value": "yearly_statistics"},
    {"label": "Recession Period Statistics", "value": "recession_period_statistics"},
]
year_list = [i for i in range(1980, 2024, 1)]


# Create a dash application
app = dash.Dash(__name__)


app.layout = html.Div(
    children=[
        html.H1(
            "Automobile Sales Statistics Dashboard",
            style={"textAlign": "center", "color": "#503D36", "font-size": 24},
        ),
        html.Div(
            dcc.Dropdown(
                id="dropdown-statistics",
                options=dropdown_options,
                placeholder=" Select a report type",
                value="Select Statistics",
                style={"width": "80%", "font-size": 20, "textAlign": "center"},
                clearable=False,
            )
        ),
        html.Br(),
        html.Div(
            dcc.Dropdown(
                id="select-year",
                options=year_list,
                value="Select-Year",
                placeholder="Select Year",
                style={"width": "80%", "font-size": 20, "textAlign": "center"},
            )
        ),
        html.Br(),
        html.Div(
            [
                html.Div(
                    id="output-container",
                    className="chart-grid",
                    style={"display": "flex", "flex-wrap": "wrap"},
                ),
            ]
        ),
    ]
)


@callback(
    Output(component_id="select-year", component_property="disabled"),
    Input(component_id="dropdown-statistics", component_property="value"),
)
def update_input_container(report_type):
    if report_type == "yearly_statistics":
        return False
    else:
        return True


@callback(
    Output(component_id="output-container", component_property="children"),
    [
        Input(component_id="dropdown-statistics", component_property="value"),
        Input(component_id="select-year", component_property="value"),
    ],
)
def update_container(report_type, year):

    if report_type == "recession_period_statistics":
        return generate_recession_period_graphs()
    elif year and report_type == "yearly_statistics":
        return generate_yearly_graphs(year=year)
    else:
        print(report_type, year)
        pass


def generate_recession_period_graphs():
    recession_data = data[data.Recession == 1]

    yearly_rec = recession_data.groupby("Year")["Automobile_Sales"].mean().reset_index()
    yearly_rec_graph = dcc.Graph(
        figure=px.line(
            yearly_rec,
            x="Year",
            y="Automobile_Sales",
            labels={
                "Year": "Year",
                "Automobile_Sales": "Average Automobile Sales",
            },
            title="Average Automobile Sales per Year",
        )
    )

    average_vehicle_sales = (
        recession_data.groupby("Vehicle_Type")["Automobile_Sales"].mean().reset_index()
    )

    average_vehicle_sales_graph = dcc.Graph(
        figure=px.bar(
            average_vehicle_sales,
            x="Vehicle_Type",
            y="Automobile_Sales",
            labels={
                "Vehicle_Type": "Vehicle Type",
                "Automobile_Sales": "Average Automobile Sales",
            },
            title="Average Automobile Sales per Vehicle Type",
        )
    )

    average_vehicle_expenditure = (
        recession_data.groupby("Vehicle_Type")["Advertising_Expenditure"]
        .mean()
        .reset_index()
    )
    average_vehicle_expenditure_graph = dcc.Graph(
        figure=px.pie(
            average_vehicle_expenditure,
            values="Advertising_Expenditure",
            names="Vehicle_Type",
            title="Average Automobile Expenditure per Vehicle Type",
        )
    )

    average_vehicle_sales_unemp = (
        recession_data.groupby(["Vehicle_Type"])[
            ["Automobile_Sales", "unemployment_rate"]
        ]
        .mean()
        .reset_index()
    )
    average_vehicle_sales_unemp_graph = dcc.Graph(
        figure=px.bar(
            average_vehicle_sales_unemp,
            x="Vehicle_Type",
            y="Automobile_Sales",
            color="unemployment_rate",
            labels={
                "Vehicle_Type": "Vehicle Type",
                "unemployment_rate": "Unemployment Rate",
                "Automobile_Sales": "Average Automobile Sales",
            },
            title="Effect of Unemployment Rate on Vehicle Type and Sales",
        )
    )

    return [
        html.Div(
            className="chart-item",
            children=[
                html.Div(children=yearly_rec_graph),
                html.Div(children=average_vehicle_sales_graph),
            ],
            style={"display": "flex"},
        ),
        html.Div(
            className="chart-item",
            children=[
                html.Div(children=average_vehicle_expenditure_graph),
                html.Div(children=average_vehicle_sales_unemp_graph),
            ],
            style={"display": "flex"},
        ),
    ]


def generate_yearly_graphs(year):
    yearly_data = data
    input_year = ""
    if isinstance(year, int):
        yearly_data = yearly_data[yearly_data.Year == int(year)]
        input_year = int(year)

    sales_per_year = (
        yearly_data.groupby("Year")["Automobile_Sales"].mean().reset_index()
    )

    sales_per_year_graph = dcc.Graph(
        figure=px.line(
            sales_per_year,
            x="Year",
            y="Automobile_Sales",
            labels={
                "Year": "Year",
                "Automobile_Sales": "Average Automobile Sales",
            },
            title="Average Automobile Sales per Year",
        )
    )

    sales_per_month = (
        yearly_data.groupby("Month", sort=False)["Automobile_Sales"].sum().reset_index()
    )
    sales_per_month_graph = dcc.Graph(
        figure=px.line(
            sales_per_month,
            x="Month",
            y="Automobile_Sales",
            labels={
                "Automobile_Sales": "Total Automobile Sales",
            },
            title="Total Monthly Automobile Sales",
        )
    )

    vehicle_sales_per_year = (
        yearly_data.groupby(
            [
                "Year",
                "Vehicle_Type",
            ]
        )["Automobile_Sales"]
        .mean()
        .reset_index()
    )
    vehicle_sales_per_year_graph = dcc.Graph(
        figure=px.bar(
            vehicle_sales_per_year,
            x="Year",
            y="Automobile_Sales",
            color="Vehicle_Type",
            labels={
                "Vehicle_Type": "Vehicle Type",
                "Automobile_Sales": "Average Automobile Sales",
            },
            title=f"Average Vehicles Sold by Vehicle Type in the year {input_year}",
        )
    )

    add_expenditure = (
        yearly_data.groupby("Vehicle_Type")["Advertising_Expenditure"]
        .sum()
        .reset_index()
    )
    add_expenditurer_graph = dcc.Graph(
        figure=px.pie(
            values=add_expenditure.Advertising_Expenditure,
            names=add_expenditure.Vehicle_Type,
            title="Total Advertisment Expenditure for Each Vehicle",
        )
    )
    return [
        html.Div(
            className="chart-item",
            children=[
                html.Div(children=sales_per_year_graph),
                html.Div(children=sales_per_month_graph),
            ],
            style={"display": "flex"},
        ),
        html.Div(
            className="chart-item",
            children=[
                html.Div(children=vehicle_sales_per_year_graph),
                html.Div(children=add_expenditurer_graph),
            ],
            style={"display": "flex"},
        ),
    ]


# Run the application
if __name__ == "__main__":
    app.run_server(port=8051, debug=True)
