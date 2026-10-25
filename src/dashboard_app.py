import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd


def build_dashboard(dataframe):
    app = dash.Dash(__name__)
    app.layout = html.Div([
        html.H2('SpaceX Falcon 9 Launch Analysis'),
        dcc.Dropdown(
            id='launch-site',
            options=[{'label': site, 'value': site} for site in dataframe['LaunchSite'].unique()],
            value='CCAFS SLC 40'
        ),
        dcc.Graph(id='scatter-chart'),
    ])

    @app.callback(Output('scatter-chart', 'figure'), Input('launch-site', 'value'))
    def update_chart(site):
        filtered = dataframe[dataframe['LaunchSite'] == site]
        fig = px.scatter(
            filtered,
            x='PayloadMass',
            y='FlightNumber',
            color='Class',
            title=f'Launch performance for {site}'
        )
        return fig

    return app


if __name__ == '__main__':
    df = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_2.csv')
    app = build_dashboard(df)
    app.run_server(debug=True)
