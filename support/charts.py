import streamlit as st
import plotly.express as px
import json
import support.sql_queries as sql_queries

@st.cache_data
def get_geojson():
    states_id = {}
    states_data = json.load(open('./support/india_state.json','r'))

    for each_state in states_data["features"]:
        each_state["id"] = each_state["properties"]["ID_1"]
        states_id[each_state["properties"]["NAME_1"].lower()] = each_state["id"]
    return {'states_id':states_id,
            'states_data':states_data}

def main_map(year,quarter):
    states_dict = get_geojson()

    df = sql_queries.transaction_data_state(year,quarter)
    df = df[(df['State'] !='ladakh') & (df['State'] !='telangana')]
    df['id'] = df['State'].apply(lambda x: states_dict['states_id'][x])

    fig = px.choropleth_mapbox(
            df,
            locations="id",
            geojson=states_dict['states_data'],
            color="Transaction Count",
            hover_name="State",
            hover_data=['Transaction Count','Transaction Value','Average'],
            title=f"PhonePe Transactions in Q{quarter} of {year}",
            mapbox_style="carto-positron",
            center={"lat": 24, "lon": 79},
            color_continuous_scale="Viridis",
            range_color=(0, 1000000000),
            zoom=3.6,
            width=800, 
            height=800
        ) 
    fig.update_layout(coloraxis_colorbar=dict(title=' ', showticklabels=True),title={
            'font': {'size': 24}
        },hoverlabel_font={'size': 18})
    return fig

def user_map(year,quarter):
    states_dict = get_geojson()
    df = sql_queries.users_state(year,quarter)
    df = df[(df['State'] !='ladakh') & (df['State'] !='telangana')]
    df['State'] = df['State'].apply(lambda x : x.replace('-'," "))

    df['id'] = df['State'].apply(lambda x: states_dict['states_id'][x])
    fig = px.choropleth_mapbox(
            df,
            locations="id",
            geojson=states_dict['states_data'],
            color="Registered Users",
            hover_name="State",
            hover_data=['Registered Users','AppOpens'],
            title=f"PhonePe Users in Q{quarter} of {year}",
            mapbox_style="carto-positron",
            center={"lat": 24, "lon": 79},
            color_continuous_scale="Viridis",
            range_color=(0, 50000000),
            zoom=3.6,
            width=800, 
            height=800
        ) 
    fig.update_layout(coloraxis_colorbar=dict(title=' ', showticklabels=True),title={
            'font': {'size': 24}
        },hoverlabel_font={'size': 18})
    return fig

def ques1(df):
    fig = px.line(df,
                    x='year',
                    y='transactions',
                    labels={'transactions': 'Transaction Count (in Billions)'},
                    title='Transactions by Year',
                )
    return fig

def ques2(df):
    fig = px.bar(df,
            x='State',
            y='Registered Users',
            color='State',
            title='Top Registered Users',
            )
    return fig

def ques3(df):
    fig = px.line(df,
                    x='Year',
                    y='Registered Users',
                    title='Registered Users',
                )
    return fig

def ques4(df):
    fig = px.pie(df,
            names='Transaction Type',
            values='Transaction Count',
            title='Transaction Type',
            )
    return fig

def ques5(df):
    fig = px.bar(df,
            x='Year',
            y='App Opens',
            color='App Opens',
            title='App Open rates',
            )
    return fig

def ques6(df):
    fig = px.bar(df,
            x='State',
            y='Average',
            color='State',
            title='Average Spending',
            )
    return fig

def ques7(df):
    fig = px.bar(df,
            x='State',
            y='Transaction Value',
            color='State',
            title='Transaction Value',
            )
    return fig

def ques8(df):
    fig = px.bar(df,
            x='State',
            y='Transaction Value',
            color='State',
            title='Merchant Payments',
            )
    return fig

def ques9(df):
    fig = px.bar(df,
            x='State',
            y='App Opens',
            color='State',
            title='App Opens',
            )
    return fig