# bowling data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


bowler_data = pd.read_csv('dataset/bowler_data.csv').set_index('bowler')
wicket_over = pd.read_csv("dataset/wicket_over_over.csv").set_index('bowler')
wicket_season = pd.read_csv("dataset/wickets_over_years.csv").set_index('bowler')
run_season = pd.read_csv("dataset/runs_conceded_season.csv").set_index('bowler')
runs_over = pd.read_csv("dataset/runs_conceded_over.csv").set_index('bowler')

def load_bowler_details(bowler):
    st.title(bowler)
    col11, col12 = st.columns(2)
    with col11:
        st.image(f'players/imagenotfound.png', width=400)
    
    with col12:
        st.title("IPL Career Analysis")
        col121,col122,col123 = st.columns(3)
        bowler_d = bowler_data.loc[bowler]
        with col121:
            st.metric('Total Wickets',str(int(bowler_d.loc['wickets'])))
        with col122:
            st.metric('Economy', str(bowler_d.loc['economy']))
        with col123:
            st.metric('Total Match Played', str((bowler_d.loc['matches_played'])))
        
        col124, col125 = st.columns(2)
        
        with col124:
            st.metric('Total Run Conceded', str(int(bowler_d.loc['total_concede'])))
        
        with col125:
            st.metric('Extra Runs Conceded', str(int(bowler_d.loc['extra_runs'])))

    col1, col2 = st.columns(2)
    with col1:
        season_wickets = wicket_season.loc[bowler]
        fig1, ax = plt.subplots()
        plt.plot(season_wickets.index, season_wickets.values, marker='*')
        plt.title(f"Wicket taken by '{bowler}' over years")
        ax.set_xlabel('Year')
        ax.set_ylabel('No of wickets')
        plt.xticks(rotation=45)
        plt.show()
        st.pyplot(fig1)

    
    with col2:
        season_runs = run_season.loc[bowler]
        fig2, ax = plt.subplots()
        plt.plot(season_runs.index, season_runs.values, marker='*')
        plt.title(f"Runs conceded by '{bowler}' over years")
        ax.set_xlabel('Year')
        ax.set_ylabel('Run Conceded')
        plt.xticks(rotation=45)
        plt.show()
        st.pyplot(fig2)
    
    col3, col4 = st.columns(2)

    with col3:
        l1 = []
        power_play = wicket_over[[str(i) for i in range(1, 7)]].loc[bowler].values.sum()
        middle_over = wicket_over[[str(i) for i in range(7, 16)]].loc[bowler].values.sum()
        death_over = wicket_over[[str(i) for i in range(16, 21)]].loc[bowler].values.sum()
        l1.append(power_play)
        l1.append(middle_over)
        l1.append(death_over)

        max_index = max(l1)
        explode = [0.1 if i == max_index else 0 for i in l1]
        fig3, ax = plt.subplots()
        plt.pie(l1, labels=['power_play', 'middle_overs', 'death_overs'], autopct='%1.1f%%', explode=explode)
        plt.title(f"Wicket taken by '{bowler}' in each category")
        plt.show()
        st.pyplot(fig3)
    
    with col4:
        over_wickets = wicket_over.loc[bowler]
        max_index = int(over_wickets.idxmax())
        explode = [0.2 if i == max_index else 0 for i in range(1, len((over_wickets.values)) + 1)]
        fig4, ax = plt.subplots()
        plt.pie(over_wickets.values, labels=over_wickets.index, autopct='%1.1f%%', explode=explode)
        plt.title(f"Wicket taken by '{bowler}' in each over")
        plt.show()
        st.pyplot(fig4)

    col5, col6 = st.columns(2)

    with col5:
        l = []
        power_play = runs_over[[str(i) for i in range(1, 7)]].loc[bowler].values.sum()
        middle_over = runs_over[[str(i) for i in range(7, 16)]].loc[bowler].values.sum()
        death_over = runs_over[[str(i) for i in range(16, 21)]].loc[bowler].values.sum()
        l.append(power_play)
        l.append(middle_over)
        l.append(death_over)

        max_index = max(l)
        explode = [0.1 if i == max_index else 0 for i in l]
        fig5, ax = plt.subplots()
        plt.pie(l, labels=['power_play', 'middle_overs', 'death_overs'], autopct='%1.1f%%', explode=explode)
        plt.title(f"Runs Conceded by '{bowler}' in each category")
        plt.show()
        st.pyplot(fig5)

    with col6:
        over_runs = runs_over.loc[bowler]
        max_index = int(over_runs.idxmax())
        explode = [0.2 if i == max_index else 0 for i in range(1, len((over_runs.values)) + 1)]
        fig6, ax = plt.subplots()
        plt.pie(over_runs.values, labels=over_runs.index, autopct='%1.1f%%', explode=explode)
        plt.title(f"Runs conceded by '{bowler}' in each over")
        plt.show()
        st.pyplot(fig6)