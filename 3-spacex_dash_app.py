# Import required libraries
import pandas as pd
import dash
from dash import Dash, html, dash_table, dcc, Output, Input
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
import plotly.express as px
from datetime import datetime

# Read the launch data into pandas dataframe
spacex_df = pd.read_csv("dataset/dataset_part_2_wrangle.csv")

# Determine max and min year for year slider
year = []
def extract_year(date):
    for i in spacex_df["Date"]:
        year.append(i.split("-")[0])
    return year

spacex_df['Year'] = extract_year(spacex_df['Date']) # Append year into df

max_year = spacex_df['Year'].max()
min_year = spacex_df['Year'].min()

# Determine max and min of payload for payload slider
max_payload = spacex_df['PayloadMass'].max()
min_payload = spacex_df['PayloadMass'].min()



# Create a dash applicatio
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create an app layout
app.layout = html.Div(
    [
        dbc.Row([ # Row 1 - Name of the dashboard
            dbc.Card(
                dbc.Col(html.H1(
                    'SpaceX Launch Records Dashboard',
                    style = {
                        'textAlign': 'center',
                        'font-size': 40
                    }
                ))
            )
        ],
        style={
            'margin': '15px',
            'margin-bottom': '20px',
        }
),
        dbc.Row([ # Row 2 - Statistics
            dbc.Col([ # Total launches
                dbc.Card(
                    [
                        dbc.CardHeader(
                            'Total launches',
                            style = {
                                'textAlign': 'center'
                            }
                        ),
                        dbc.CardBody(
                            html.Div(
                                id = 'stats-total-launches'
                            ),
                            style = {
                                'textAlign': 'center',
                                'font-size': '72px'
                            }
                        )
                    ],
                    style={
                        'margin': '15px',
                        'margin-bottom': '20px',
                    }
                )
            ],
                xs=6, sm=6, md=3, lg=3, xl=3
            ),
            dbc.Col([ # Success rate
                dbc.Card(
                    [
                        dbc.CardHeader(
                            'Success rate',
                            style = {
                                'textAlign': 'center'
                            }
                        ),
                        dbc.CardBody(
                            html.Div(
                                id = 'stats-success-rate'
                            ),
                            style = {
                                'textAlign': 'center',
                                'font-size': '72px'
                            }
                        )
                    ],
                    style={
                        'margin': '15px',
                        'margin-bottom': '20px',
                    }
                )
            ],
                xs=6, sm=6, md=3, lg=3, xl=3
            ),
            dbc.Col([ # Average payload mass
                dbc.Card(
                    [
                        dbc.CardHeader(
                            'Average payload mass',
                            style = {
                                'textAlign': 'center'
                            }
                        ),
                        dbc.CardBody(
                            html.Div(
                                id = 'stats-avg-payload'
                            ),
                            style = {
                                'textAlign': 'center',
                                'font-size': '72px'
                            }
                        )
                    ],
                    style={
                        'margin': '15px',
                        'margin-bottom': '20px',
                    }
                )
            ],
                xs=6, sm=6, md=3, lg=3, xl=3
            ),
            dbc.Col([ # Latest launch
                dbc.Card(
                    [
                        dbc.CardHeader(
                            'Latest launch',
                            style = {
                                'textAlign': 'center'
                            }
                        ),
                        dbc.CardBody(
                            html.Div(
                                id = 'stats-latest-launch'
                            ),
                            style = {
                                'textAlign': 'center',
                                'font-size': '72px'
                            }
                        )
                    ],
                    style={
                        'margin': '15px',
                        'margin-bottom': '20px',
                    }
                )
            ],
                xs=6, sm=6, md=3, lg=3, xl=3
            )
        ]),
        dbc.Row([ # Row 3 - Parameters board
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader("Select launch site"),
                    dbc.CardBody(
                        html.Div(
                            [
                                html.Label("Select launch site"),
                                dcc.Dropdown(
                                    id = 'site-dropdown',
                                        options = [
                                        {'label': 'All Sites', 'value': 'ALL'}
                                    ]+
                                    [
                                        {'label': i, 'value': i} for i in spacex_df['LaunchSite'].unique()
                                    ],
                                    value = 'ALL',
                                    placeholder = 'Select a launch site',
                                    searchable = True
                                )
                            ],
                            style = {
                                'padding': '3%',
                                'font-size': 20
                            }
                        )
                    )
                ],
                    style={
                        'margin': '15px',
                        'margin-bottom': '20px',
                    }
                )
            ],
            xs=12, sm=12, md=6, lg=6, xl=6
            ),
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader("Select year"),
                    dbc.CardBody(
                        html.Div([
                            html.Label("Select year"),
                            dcc.RangeSlider(
                                id='year-slider',
                                min = 2010, max = 2020, step = 1,
                                value = [min_year, max_year],
                                marks = {
                                    2010: {'label': '2010', 'style': {'color': '#77b0b1'}},
                                    **{i: {'label': str(i), 'value': i} for i in range(2011, 2020, 1)},
                                    2020: {'label': '2020', 'style': {'color': '#f50'}}
                                },
                                tooltip = {
                                    "placement": "bottom",
                                    "always_visible": True
                                }
                            )
                        ],
                            style = {
                                'padding': '3%',
                                'font-size': 20
                            }
                        )
                    )
                ],
                    style={
                        'margin': '15px',
                        'margin-bottom': '20px',
                    }
                )
            ],
            xs=12, sm=12, md=6, lg=6, xl=6
            )
        ]),
        dbc.Row([ # Row 4 - Plot row A
            # Left col    
            dbc.Col([
                dbc.Card(
                    [
                        dbc.CardHeader('Launch outcome by year'),
                        dbc.CardBody(
                                html.Div(
                                    dcc.Graph(id='launch-success-bar-plot'), 
                                )
                        )
                    ],
                        style={
                            'margin': '15px',
                            'margin-bottom': '20px',
                        }
                )            
            ],
                xs=12, sm=12, md=6, lg=6, xl=6
            ),
            # Right col
            dbc.Col([
                dbc.Card(
                    [
                        dbc.CardHeader('Launch site by year'),
                        dbc.CardBody(
                                html.Div(
                                    dcc.Graph(id='launch-site-bar-plot'), 
                                )
                        )
                    ],
                        style={
                            'margin': '15px',
                            'margin-bottom': '20px',
                        }
                )            
            ],
                xs=12, sm=12, md=6, lg=6, xl=6
            )
        ]),
        dbc.Row([ # Row 5 - Plot row B
            # Left col    
            dbc.Col([
                dbc.Card(
                    [
                        dbc.CardHeader('Success rate'),
                        dbc.CardBody(
                                html.Div(
                                    dcc.Graph(id='success-pie-chart'), 
                                )
                        )
                    ],
                        style={
                            'margin': '15px',
                            'margin-bottom': '20px',
                        }
                )            
            ],
                xs=12, sm=12, md=6, lg=6, xl=6
            ),
            # Right col
            dbc.Col([    
                dbc.Card(
                    [
                    dbc.CardHeader('Correlation between Payload and Success rate'),
                    dbc.CardBody(
                        [
                            # Payload graph
                            html.Div(
                                dcc.Graph(id='success-payload-scatter-chart'),
                            ),
                            html.Div([
                                    html.Label("Payload range (Kg):"),
                                    dcc.RangeSlider(
                                        id='payload-slider',
                                        min = 0, max = 15600, step = 5000,
                                        value = [min_payload, max_payload],
                                        marks = {
                                            0: {'label': '0', 'style': {'color': '#77b0b1'}},
                                            **{i: {'label': str(i), 'value': i} for i in range(0, 15600, 5000)},
                                            15600: {'label': '15600', 'style': {'color': '#f50'}}
                                        },
                                        tooltip = {
                                            "placement": "bottom",
                                            "always_visible": True
                                        }
                                    )
                                ],
                                style = {
                                    'padding': '3%',
                                    'font-size': 20
                                }
                            )
                        ]),
                    ],
                        style={
                            'margin': '15px',
                            'margin-bottom': '20px',
                        }
                )
            ],
                xs=12, sm=12, md=6, lg=6, xl=6,
            )
        ]),

    ]
)


# Callback for 2A. Stats - Total launches
@app.callback(
    Output(
        component_id = 'stats-total-launches',
        component_property = 'children'
    ),
    [
        Input(
            component_id = 'site-dropdown',
            component_property = 'value'
        ),
        Input(
            component_id = 'year-slider',
            component_property = 'value'
        )
    ],
    fluid = True
)
def update_stats_total_launches(selected_site, selected_year):
    if selected_site == 'ALL':
        filter_df = spacex_df[
            (
                spacex_df['Year'] >= str(selected_year[0])
            )&(
                spacex_df['Year'] <= str(selected_year[1])
            )
        ]
        total_launches = len(filter_df)
    else:
        filter_df = spacex_df[spacex_df['LaunchSite'] == selected_site]
        filter_df = filter_df[
            (
                filter_df['Year'] >= str(selected_year[0])
            )&(
                filter_df['Year'] <= str(selected_year[1])
            )
        ]
        total_launches = len(filter_df)
    return f'{total_launches}'


# Callback for 2B. Stats - Success rate
@app.callback(
    Output(
        component_id = 'stats-success-rate',
        component_property = 'children'
    ),
    [
        Input(
            component_id = 'site-dropdown',
            component_property = 'value'
        ),
        Input(
            component_id = 'year-slider',
            component_property = 'value'
        )
    ],
    fluid = True
)
def update_stats_success_rate(selected_site, selected_year):
    if selected_site == 'ALL':
        filter_df = spacex_df[
            (
                spacex_df['Year'] >= str(selected_year[0])
            )&(
                spacex_df['Year'] <= str(selected_year[1])
            )
        ]
        success_rate = filter_df['Class'].mean()
    else:
        filter_df = spacex_df[spacex_df['LaunchSite'] == selected_site]
        filter_df = filter_df[
            (
                filter_df['Year'] >= str(selected_year[0])
            )&(
                filter_df['Year'] <= str(selected_year[1])
            )
        ]
        success_rate = filter_df['Class'].mean()
    
    return f'{success_rate:.1%}'


# Callback for 2C. Stats - Average payload mass
@app.callback(
    Output(
        component_id = 'stats-avg-payload',
        component_property = 'children'
    ),
    [
        Input(
            component_id = 'site-dropdown',
            component_property = 'value'
        ),
        Input(
            component_id = 'year-slider',
            component_property = 'value'
        )
    ],
    fluid = True
)
def update_stats_avg_payload(selected_site, selected_year):
    if selected_site == 'ALL':
        filter_df = spacex_df[
            (
                spacex_df['Year'] >= str(selected_year[0])
            )&(
                spacex_df['Year'] <= str(selected_year[1])
            )
        ]
        avg_payload = filter_df['PayloadMass'].mean()
    else:
        filter_df = spacex_df[spacex_df['LaunchSite'] == selected_site]
        filter_df = filter_df[
            (
                filter_df['Year'] >= str(selected_year[0])
            )&(
                filter_df['Year'] <= str(selected_year[1])
            )
        ]
        avg_payload = filter_df['PayloadMass'].mean()
    
    return f'{avg_payload:.0f} kg'


# Callback for 2D. Stats - Latest launch
@app.callback(
    Output(
        component_id = 'stats-latest-launch',
        component_property = 'children'
    ),
    [
        Input(
            component_id = 'site-dropdown',
            component_property = 'value'
        ),
        Input(
            component_id = 'year-slider',
            component_property = 'value'
        )
    ],
    fluid = True
)
def update_stats_latest_launch(selected_site, selected_year):
    if selected_site == 'ALL':
        filter_df = spacex_df[
            (
                spacex_df['Year'] >= str(selected_year[0])
            )&(
                spacex_df['Year'] <= str(selected_year[1])
            )
        ]
        latest_launch = filter_df['Date'].max()
        # Change all values in 'Date' into time data type
        latest_launch = pd.to_datetime(latest_launch)
        formatted_date = latest_launch.strftime('%Y-%m')
    else:
        filter_df = spacex_df[spacex_df['LaunchSite'] == selected_site]
        filter_df = filter_df[
            (
                filter_df['Year'] >= str(selected_year[0])
            )&(
                filter_df['Year'] <= str(selected_year[1])
            )
        ]
        latest_launch = filter_df['Date'].max()
        # Change all values in 'Date' into time data type
        latest_launch = pd.to_datetime(latest_launch)
        formatted_date = latest_launch.strftime('%Y-%m')
    
    return f'{formatted_date}'


# Callback for 3A.launch success bar plot
@app.callback(
    Output(
        component_id = 'launch-success-bar-plot',
        component_property = 'figure'
    ),
    [
        Input(
            component_id = 'site-dropdown',
            component_property = 'value'
        ),
        Input(
            component_id = 'year-slider',
            component_property = 'value'
        )
    ],
    fluid = True
)
def get_success_bar_plot(selected_site, selected_year):
    print(selected_site, selected_year)
    if selected_site == 'ALL':
        filter_df = spacex_df[
            (
                spacex_df['Year'] >= str(selected_year[0])
            )&(
                spacex_df['Year'] <= str(selected_year[1])
            )
        ]
        fig = px.histogram(
            filter_df,
            x = 'Year',
            color = 'Class',
        )
        fig.update_layout(
            xaxis_title = 'Total launch',
            font = dict(color = 'white'),
            plot_bgcolor = 'rgba(0, 0, 0, 0)',
            paper_bgcolor = 'rgba(0, 0, 0, 0)',
        )
    else:
        filter_df = spacex_df[spacex_df['LaunchSite'] == selected_site]
        filter_df = filter_df[
            (
                filter_df['Year'] >= str(selected_year[0])
            )&(
                filter_df['Year'] <= str(selected_year[1])
            )
        ]
        fig = px.histogram(
            filter_df,
            x = 'Year',
            color = 'Class',
        )
        fig.update_layout(
            xaxis_title = 'Total launch',
            font = dict(color = 'white'),
            plot_bgcolor = 'rgba(0, 0, 0, 0)',
            paper_bgcolor = 'rgba(0, 0, 0, 0)',
        )
    return fig
 # return the outcomes piechart for a selected site

# Callback for 3B.launch site area plot
@app.callback(
    Output(
        component_id = 'launch-site-bar-plot',
        component_property = 'figure'
    ),
    [
        Input(
            component_id = 'site-dropdown',
            component_property = 'value'
        ),
        Input(
            component_id = 'year-slider',
            component_property = 'value'
        )
    ],
    fluid = True
)
def get_site_area_plot(selected_site, selected_year):
    print(selected_site, selected_year)
    if selected_site == 'ALL':
        filter_df = spacex_df[
            (
                spacex_df['Year'] >= str(selected_year[0])
            )&(
                spacex_df['Year'] <= str(selected_year[1])
            )
        ]
        filter_df = filter_df.groupby(['Year', 'LaunchSite']).size().reset_index(name='Count')
        fig = px.area(
            filter_df,
            x = 'Year',
            y = 'Count',
            color = 'LaunchSite'
        )
        fig.update_layout(
            xaxis_title = 'Total launch',
            yaxis_title = 'Launches',
            legend_title = 'Site',
            font = dict(color = 'white'),
            plot_bgcolor = 'rgba(0, 0, 0, 0)',
            paper_bgcolor = 'rgba(0, 0, 0, 0)',
        )
    else:
        filter_df = spacex_df[spacex_df['LaunchSite'] == selected_site]
        filter_df = filter_df[
            (
                filter_df['Year'] >= str(selected_year[0])
            )&(
                filter_df['Year'] <= str(selected_year[1])
            )
        ]
        filter_df = filter_df.groupby(['Year', 'LaunchSite']).size().reset_index(name='Count')
        fig = px.area(
            filter_df,
            x = 'Year',
            y = 'Count',
            color = 'LaunchSite'
        )
        fig.update_layout(
            xaxis_title = 'Total launch',
            yaxis_title = 'Launches',
            legend_title = 'Site',
            font = dict(color = 'white'),
            plot_bgcolor = 'rgba(0, 0, 0, 0)',
            paper_bgcolor = 'rgba(0, 0, 0, 0)',
        )
    return fig
 # return the outcomes piechart for a selected site

# Callback for 4A.pie chart
@app.callback(
    Output(
        component_id = 'success-pie-chart',
        component_property = 'figure'
    ),
    [
        Input(
            component_id = 'site-dropdown',
            component_property = 'value'
        ),
        Input(
            component_id = 'year-slider',
            component_property = 'value'
        )
    ],
    fluid = True
)
def get_pie_chart(selected_site, selected_year):
    print(selected_site, selected_year)
    if selected_site == 'ALL':
        filter_df = spacex_df[
            (
                spacex_df['Year'] >= str(selected_year[0])
            )&(
                spacex_df['Year'] <= str(selected_year[1])
            )
        ]
        filter_df = filter_df[filter_df['Class'] == 1]
        filter_df = filter_df.groupby('LaunchSite')['Class'].sum().reset_index()
        fig = px.pie(
            filter_df,
            values= 'Class',
            names = 'LaunchSite'
        )
        fig.update_layout(
            font = dict(color = 'white'),
            plot_bgcolor = 'rgba(0, 0, 0, 0)',
            paper_bgcolor = 'rgba(0, 0, 0, 0)',
        )
    else:
        filter_df = spacex_df[spacex_df['LaunchSite'] == selected_site]
        filter_df = filter_df[
            (
                filter_df['Year'] >= str(selected_year[0])
            )&(
                filter_df['Year'] <= str(selected_year[1])
            )
        ]
        filter_df = pd.DataFrame(filter_df[['Class']].value_counts())
        filter_df.reset_index(inplace=True) 
        filter_df.columns=['Class','count']
        fig = px.pie(
            filter_df,
            values='count',
            names='Class'
        )
        fig.update_layout(
            font = dict(color = 'white'),
            plot_bgcolor = 'rgba(0, 0, 0, 0)',
            paper_bgcolor = 'rgba(0, 0, 0, 0)',
        )
    return fig
 # return the outcomes piechart for a selected site

# Callback for 4B. scatter plot
@app.callback(
    Output(
        component_id = 'success-payload-scatter-chart',
        component_property = 'figure'
    ),
    [
        Input(
            component_id = 'site-dropdown',
            component_property = 'value'
        ),
        Input(
            component_id = 'payload-slider',
            component_property = 'value'
        ),
        Input(
            component_id = 'year-slider',
            component_property = 'value'
        )
    ]
)
def get_scatter_plot(selected_site, payload, selected_year):
    print(selected_site, selected_year)
    if selected_site == 'ALL':
        filter_df = spacex_df[
            (
                spacex_df['PayloadMass'] >= int(payload[0])
            )&(
                spacex_df['PayloadMass']<=int(payload[1])
            )
        ]
        filter_df = filter_df[
            (
                filter_df['Year'] >= str(selected_year[0])
            )&(
                filter_df['Year'] <= str(selected_year[1])
            )
        ]
        fig = px.scatter(
            filter_df,
            x = 'PayloadMass', 
            y = 'Class',
            color = 'Year'
        )
        fig.update_layout(
            font = dict(color = 'white'),
            plot_bgcolor = 'rgba(0, 0, 0, 0)',
            paper_bgcolor = 'rgba(0, 0, 0, 0)',
            yaxis = dict(tickvals = [0,1])
        )
    else:
        filter_df = spacex_df[spacex_df['LaunchSite'] == selected_site]
        filter_df = filter_df[
            (
                filter_df['PayloadMass'] >= int(payload[0])
            )&(
                filter_df['PayloadMass'] <= int(payload[1])
            )
        ]
        filter_df = filter_df[
            (
                filter_df['Year'] >= str(selected_year[0])
            )&(
                filter_df['Year'] <= str(selected_year[1])
            )
        ]
        fig = px.scatter(
            filter_df,
            x = 'PayloadMass', 
            y = 'Class',
            color = 'Year'
        )
        fig.update_layout(
            font = dict(color = 'white'),
            plot_bgcolor = 'rgba(0, 0, 0, 0)',
            paper_bgcolor = 'rgba(0, 0, 0, 0)',
            yaxis = dict(tickvals = [0,1])
        )
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server()
