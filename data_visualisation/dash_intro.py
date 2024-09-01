import pandas as pd
import plotly.express as px
import dash 
from dash import dcc, html,Input, Output, callback

data_url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv'
airline_data =  pd.read_csv(
    data_url, 
    encoding = "ISO-8859-1", 
    dtype={'Div1Airport': str, 'Div1TailNum': str, 'Div2Airport': str, 'Div2TailNum': str}
)

# Create a dash application
app = dash.Dash(__name__)

# Get the layout of the application and adjust it.
# Create an outer division using html.Div and add title to the dashboard using html.H1 component
# Add description about the graph using HTML P (paragraph) component
# Finally, add graph component.


app.layout = html.Div(
    children=[
                html.H1('Airline Dashboard',style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
                html.Div(["Input Year: ", 
                         dcc.Slider(
                                     airline_data['Year'].min(),
                                     airline_data['Year'].max(),
                                     step=None,
                                     value=airline_data['Year'].min(),
                                     marks={str(year): str(year) for year in airline_data['Year'].unique()},
                                     id='input-year'
                                )
                        ]), 
                html.P(
                    'Proportion of distance group (250 mile distance interval group) by flights.', style={'textAlign':'center', 'color': '#F57241'}
                ),
                dcc.Graph(id="airline-grapth"),                               
            ]
)

# Add computation to callback function and return graph
@callback(
    Output('airline-grapth', 'figure'),
    Input('input-year', 'value'))
def get_graph(entered_year):
    df = None
    if entered_year is None:
        df = airline_data
    else:
        df =  airline_data[airline_data.Year==int(entered_year)] 
    fig = px.pie(df, values='Flights', names='DistanceGroup', title='Distance group proportion by flights')
    fig.update_layout()
    return fig

# Run the application                  
if __name__ == '__main__':
    app.run_server()
