import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def gen_analysis():
    st.title('General Analysis')

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Top 5 batsman with highest runs")
        df = pd.read_csv('dataset/total_data.csv')
        df = df[['Name', 'runs', 'strike_rate']]
        df = df.set_index('Name').head()
        st.dataframe(df)

    with col2:
        st.markdown("### Top 5 batsman with highest Stike Rate")
        df = pd.read_csv('dataset/total_data.csv')
        df = df[df['runs'] >= 500]
        df = df.sort_values(by='strike_rate', ascending=False)
        df = df[['Name', 'strike_rate', 'runs']]
        df = df.set_index('Name').head()
        st.dataframe(df)

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("### Top 5 batsman with highest Sixes")
        df = pd.read_csv('dataset/total_data.csv')
        df = df.sort_values(by='sixes', ascending=False)
        df = df[['Name', 'sixes', 'strike_rate']]
        df = df.set_index('Name').head()
        st.dataframe(df)

    with col4:
        st.markdown("### Top 5 batsman with highest Fours")
        df = pd.read_csv('dataset/total_data.csv')
        df = df.sort_values(by='fours', ascending=False)
        df = df[['Name', 'fours', 'strike_rate']]
        df = df.set_index('Name').head()
        st.dataframe(df)

    st.markdown("### Top 5 batsman with most ducks")
    ducks = pd.read_csv('dataset/goldenduck.csv')
    ducks = ducks[['batter', 'ducks']]
    ducks = ducks.sort_values(by='ducks', ascending=False)
    ducks = ducks.set_index('batter').head()
    st.dataframe(ducks)

    st.markdown('## Bowler General Analysis')

    col5, col6 = st.columns(2)

    with col5:
        st.markdown('### Top 5 bowler with most wickets')
        bowler = pd.read_csv("dataset/bowler_data.csv")
        bowler = bowler[['bowler', 'wickets', 'matches_played']]
        bowler = bowler.set_index('bowler').head()
        st.dataframe(bowler)
    
    with col6:
        st.markdown('### Top 5 bowler with least economy')
        bowler = pd.read_csv('dataset/bowler_data.csv')
        bowler = bowler[bowler['wickets'] >= 50]
        bowler = bowler.sort_values(by='economy')
        bowler = bowler[['bowler', 'economy', 'wickets']].set_index('bowler').head()
        st.dataframe(bowler)

    col7, col8 = st.columns(2)

    with col7:
        st.markdown("### Top 5 bowlers with most economy and extra runs conceded")
        bowler = pd.read_csv('dataset/bowler_data.csv')
        bowler = bowler[bowler['matches_played'] >= 25]
        bowler = bowler.sort_values(by=['economy', 'extra_runs'], ascending=False)
        bowler = bowler[['bowler', 'economy', 'extra_runs']].set_index('bowler').head()
        st.dataframe(bowler)


    


