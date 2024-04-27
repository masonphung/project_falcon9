# Import required libraries
import pandas as pd
import dash
from dash import Dash, html, dash_table, dcc, Output, Input
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
import plotly.express as px
from datetime import datetime

# Read the launch data into pandas dataframe
spacex_df = pd.read_csv("dataset/falcon9_technical.csv")

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
        dbc.Row(# Row 1 - Name of the dashboard
            [ 
                dbc.Col(
                    [
                        html.Header(
                            'SpaceX Launch Records Dashboard',
                        ),
                    
                    ],
                    className = ["Header"]
                ),
                dbc.Col([
                    html.H5("Select site"),
                    html.Div(
                            [
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
                                'font-size': '20px'
                            }
                    ),
                ]),
                dbc.Col([
                        html.H5("Select year"),
                        html.Div([
                            dcc.RangeSlider(
                                id='year-slider',
                                min = 2010, max = 2020, step = 1,
                                value = [min_year, max_year],
                                marks = {
                                    2010: {'label': '2010', 'style': {'color': '#77b0b1'}},
                                    **{i: {'label': str(i), 'value': i} for i in range(2011, 2020, 1)},
                                    2020: {'label': '2020', 'style': {'color': '#fd7e14'}}
                                },
                                tooltip = {
                                    "placement": "bottom",
                                    "always_visible": True
                                }
                            )
                        ],
                            style = {
                                'padding': '3%',
                                'font-size': '20px'
                            }
                        )
                ])
            ], 
            style= {
                'align-items': 'center'
            }
        ),
        dbc.Row(# Row 2 - Dashboard
            [ 
                dbc.Col(
                    [  # Statistics
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
                                        'font-size': '3.2vw',
                                        'align-items': 'center'
                                    }
                                )
                            ],
                            className=["h-25"]
                        ),
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
                                        'font-size': '3.2vw',
                                        'align-items': 'center'
                                    }
                                )
                            ],
                            className=["h-25"]
                        ),
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
                                        'font-size': '3.2vw',
                                        'align-items': 'center'
                                    }
                                )
                            ],
                            className=["h-25"]
                        ),
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
                                        'font-size': '3.2vw',
                                        'align-items': 'center',
                                    }
                                )
                            ],
                            className = ["h-25"]
                        )
                    ],
                    className = [
                        'd-flex',
                        'justify-content-between',
                        'flex-column'
                    ],
                    xs=12, sm=12, md=2, lg=2, xl=2
                ),
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardHeader('Launch outcome by year'),
                                dbc.CardBody(
                                        html.Div(
                                            dcc.Graph(id='launch-success-bar-plot')
                                        )
                                )
                            ]
                        ),
                        dbc.Card(
                            [
                                dbc.CardHeader('Launch site by year'),
                                dbc.CardBody(
                                    html.Div(
                                        dcc.Graph(id='launch-site-bar-plot')
                                    )
                                )
                            ]
                        )
                    ],
                    xs=12, sm=12, md=5, lg=5, xl=5
                ),
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardHeader('Success launches of each site'),
                                dbc.CardBody(
                                        html.Div(
                                            dcc.Graph(id='success-pie-chart'),
                                        )
                                )
                        ]),
                        dbc.Card(
                            [
                                dbc.CardHeader('Launch success percentage of each orbit'),
                                dbc.CardBody(
                                    html.Div(
                                        dcc.Graph(id='orbit-success-rate'),
                                    )
                                ),
                            ]
                        )
                    ],
                    xs=12, sm=12, md=5, lg=5, xl=5
                )
            ],
            style = {
                'margin': '10px'
            }
        )
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
            opacity = 0.7,
            color_discrete_sequence = ['#F9EAE1','#43b2e5']
        )
        fig.update_layout(
            xaxis_title = 'Year',
            yaxis_title = 'Launches',
            font = dict(color = 'white'),
            plot_bgcolor = 'rgba(0, 0, 0, 0)',
            paper_bgcolor = 'rgba(0, 0, 0, 0)',
            legend_traceorder = 'reversed',
            legend_title = '',
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.2,
                xanchor="right",
                x=0.15
            )
        )
        fig.update_xaxes(
            showgrid = False,
        )
        fig.update_yaxes(
            showgrid = False,
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
            opacity = 0.7,
            color_discrete_sequence = ['#F9EAE1','#43b2e5']
        )
        fig.update_layout(
            xaxis_title = 'Year',
            yaxis_title = 'Launches',
            font = dict(color = 'white'),
            plot_bgcolor = 'rgba(0, 0, 0, 0)',
            paper_bgcolor = 'rgba(0, 0, 0, 0)',
            legend_traceorder = 'reversed',
            legend_title = '',
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.2,
                xanchor="right",
                x=0.15
            )
        )
        fig.update_xaxes(
            showgrid = False,
        )
        fig.update_yaxes(
            showgrid = False,
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
            color = 'LaunchSite',
            color_discrete_sequence = ['#43b2e5','#fd7e14','#F9EAE1']
        )
        fig.update_layout(
            xaxis_title = 'Year',
            yaxis_title = 'Launches',
            legend_title = '',
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.2,
                xanchor="right",
                x=0.9
            ),
            font = dict(color = 'white'),
            plot_bgcolor = 'rgba(0, 0, 0, 0)',
            paper_bgcolor = 'rgba(0, 0, 0, 0)',
            hovermode = 'x'
        )
        fig.update_traces(
            hovertemplate = None
        )
        fig.update_xaxes(
            showgrid = False,
            zeroline = False
        )
        fig.update_yaxes(
            showgrid = False,
            zeroline = False
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
            color = 'LaunchSite',
            color_discrete_sequence = ['#43b2e5','#fd7e14','#F9EAE1']
        )
        fig.update_layout(
            xaxis_title = 'Year',
            yaxis_title = 'Launches',
            legend_title = '',
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.2,
                xanchor="right",
                x=1
            ),
            font = dict(color = 'white'),
            plot_bgcolor = 'rgba(0, 0, 0, 0)',
            paper_bgcolor = 'rgba(0, 0, 0, 0)',
            hovermode = 'x'
        )
        fig.update_traces(
            hovertemplate = None
        )
        fig.update_xaxes(
            showgrid = False,
            zeroline = False
        )
        fig.update_yaxes(
            showgrid = False,
            zeroline = False
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
def get_success_rate_pie_chart(selected_site, selected_year):
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
            names = 'LaunchSite',
            color_discrete_sequence = ['#43b2e5','#fd7e14','#F9EAE1'],
            opacity = 0.7,
        )
        fig.update_layout(
            font = dict(color = 'white'),
            plot_bgcolor = 'rgba(0, 0, 0, 0)',
            paper_bgcolor = 'rgba(0, 0, 0, 0)',
            legend_title = '',
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.2,
                xanchor="right",
                x=0.85
            ),
        )
        fig.update_traces(
            hovertemplate = None
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
            names='Class',
            opacity = 0.7,
            color_discrete_sequence = ['#43b2e5','#fd7e14','#F9EAE1']
        )
        fig.update_layout(
            font = dict(color = 'white'),
            plot_bgcolor = 'rgba(0, 0, 0, 0)',
            paper_bgcolor = 'rgba(0, 0, 0, 0)',
            legend_title = '',
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.2,
                xanchor="right",
                x=0.85
            ),
        )
        fig.update_traces(
            hovertemplate = None
        )
    return fig
 # return the outcomes piechart for a selected site

# Callback for 4B. orbit success rate
@app.callback(
    Output(
        component_id = 'orbit-success-rate',
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
    ]
)
def get_orbit_bar_plot(selected_site, selected_year):
    print(selected_site, selected_year)
    if selected_site == 'ALL':
        filter_df = spacex_df[
            (
                spacex_df['Year'] >= str(selected_year[0])
            )&(
                spacex_df['Year'] <= str(selected_year[1])
            )
        ]
        orbit_success_rate = filter_df.groupby(filter_df["Orbit"])["Class"].mean().reset_index()
        # Calculate success rate in percentage
        orbit_success_rate["Class"] = orbit_success_rate["Class"]*100
        # Filter the order of the data by success rate descendently
        orbit_success_rate = orbit_success_rate.sort_values(
            by = 'Class'
        )
        fig = px.bar(
            orbit_success_rate,
            x = 'Class',
            y = 'Orbit',
            color = 'Class',
            color_continuous_scale = ['#fd7e14','#43b2e5'] #'#F9EAE1'
        )
        fig.update_layout(
            font = dict(color = 'white'),
            yaxis_title = 'Orbit',
            xaxis_title = 'Success rate (%)',
            showlegend = False,
            plot_bgcolor = 'rgba(0, 0, 0, 0)',
            paper_bgcolor = 'rgba(0, 0, 0, 0)'
        )
        fig.update_xaxes(
            showgrid = False,
            zeroline = False
        )
        fig.update_yaxes(
            showgrid = False,
            zeroline = False
        )
        fig.update_traces(
            hovertemplate = None
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
        orbit_success_rate = filter_df.groupby(filter_df["Orbit"])["Class"].mean().reset_index()
        # Calculate success rate in percentage
        orbit_success_rate["Class"] = orbit_success_rate["Class"]*100
        # Filter the order of the data by success rate descendently
        orbit_success_rate = orbit_success_rate.sort_values(
            by = 'Class'
        )
        fig = px.bar(
            orbit_success_rate,
            x = 'Class',
            y = 'Orbit',
            color = 'Class',
            color_continuous_scale = ['#fd7e14','#43b2e5'] #'#F9EAE1'
        )
        fig.update_layout(
            font = dict(color = 'white'),
            yaxis_title = 'Orbit',
            xaxis_title = 'Success rate (%)',
            showlegend = False,
            plot_bgcolor = 'rgba(0, 0, 0, 0)',
            paper_bgcolor = 'rgba(0, 0, 0, 0)'
        )
        fig.update_xaxes(
            showgrid = False,
            zeroline = False
        )
        fig.update_yaxes(
            showgrid = False,
            zeroline = False
        )
        fig.update_traces(
            hovertemplate = None
        )
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server()
