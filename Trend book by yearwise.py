import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from matplotlib.pyplot import title
import plotly.express as px
import pandas as pd
import pyodbc as py
#Sql server connection
server = 'd2mtrainingdb.database.windows.net'
db = 'd2manalysistraining'
user = 'dbtuser'
pwd = 'Disys@2022'


conn = py.connect('DRIVER={SQL Server};SERVER=' + server +
                      ';DATABASE=' + db +
                      '; UID=' + user +
                      '; PWD=' + pwd +
                      ';Trusted_Connection=no')
cursor = conn.cursor()
# SQL Query and storing data into df
df = pd.read_sql_query('execute trending_books',conn)
all_year =df.publication_year.unique()
#dash app
app = dash.Dash(__name__)

app.layout =html.Div([
        dcc.Checklist(                                       #creating a checklist
            id="checklist",
            options=[{"label": x, "value": x} 
                    for x in all_year],
            value=all_year[1:],
            labelStyle={'display': 'inline-block'}
        ),
        dcc.Graph(id="scatter-chart"),
    ])
@app.callback(
    Output("scatter-chart", "figure"), 
    [Input("checklist", "value")])
def update_line_chart(all_Batch):
    mask = df.publication_year.isin(all_Batch)
    df[mask] = df[mask].sort_values(by="category")
    #plotting the graph here we are using Scatter graph for representation
    fig = px.scatter(df[mask], 
        x="category", y="percentages", color='publication_year',text='percentages',symbol="publication_year",width=2000, height=600 , template='xgridoff',
        title = "Trending Books by year ",color_discrete_sequence=px.colors.qualitative.Set2,)
    fig.update_layout(coloraxis_showscale=False)
    fig.update_traces(textposition="top center")
    fig.update_layout( title_x=0.5)
    fig.update_layout(                       #creating two button and using restyle function from plotly
    updatemenus=[
        dict(
            buttons=list([
                 dict(
                    args=["type", "scatter"],
                    label="Scatter Chart",
                    method="restyle"
                ),
                dict(
                    args=["type", "bar"],
                    label="Bar  Chart",
                    method="restyle"
                )
            ]),
            direction="down",
        ),
    ]
)
  
   
    return fig

app.run_server(debug=True)