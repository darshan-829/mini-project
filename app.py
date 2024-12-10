import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(layout='wide', page_title='IPL Data Analytics')
st.title("IPL Data Analytics")

new_df = pd.read_csv("ipldata.csv")
matches = pd.read_csv("matches.csv")
player_data = pd.read_csv('total_data.csv')
highest_score = pd.read_csv('highest_score.csv')
duck = pd.read_csv('goldenduck.csv')


batsman_runs_per_match = new_df.groupby(['season', 'match_id', 'batter'])['batsman_runs'].sum().reset_index()
        
batsman_run_ge50 = batsman_runs_per_match[(batsman_runs_per_match['batsman_runs'] >= 50) & (batsman_runs_per_match['batsman_runs'] < 100)]
batsman_run_ge100 = batsman_runs_per_match[(batsman_runs_per_match['batsman_runs'] >= 100)]
batsman_run_ge30 = batsman_runs_per_match[(batsman_runs_per_match['batsman_runs'] >= 30) & (batsman_runs_per_match['batsman_runs'] < 50)]

## variables
is_half_century = 2
is_pom = 2
century_hai = 2
is_thirty_plus = 2

player_list = ['A Badoni', 'A Mishra', 'AB de Villiers', 'AD Russell', 'AK Markram', 'AM Rahane', 'AR Patel', 'AT Rayudu', 'Abdul Samad', 'Abhishek Sharma', 'B Sai Sudharsan', 'BB McCullum', 'C Green', 'CH Gayle', 'D Padikkal', 'DA Miller', 'DA Warner', 'DJ Hooda', 'DP Conway', 'EJG Morgan', 'F du Plessis', 'G Gambhir', 'GJ Maxwell', 'Gurkeerat Singh', 'H Klaasen', 'HH Pandya', 'Ishan Kishan', 'JC Buttler', 'JJ Roy', 'JM Bairstow', 'JM Sharma', 'KA Pollard', 'KD Karthik', 'KH Pandya', 'KK Nair', 'KL Rahul', 'KM Jadhav', 'KS Williamson', 'KV Sharma', 'LS Livingstone', 'Lalit Yadav', 'M Shahrukh Khan', 'MA Agarwal', 'MC Henriques', 'MK Lomror', 'MK Pandey', 'MK Tiwary', 'MM Ali', 'MP Stoinis', 'MR Marsh', 'MS Bisla', 'MS Dhoni', 'Mandeep Singh', 'N Pooran', 'N Rana', 'P Simran Singh', 'PA Patel', 'PD Salt', 'PJ Cummins', 'PP Shaw', 'Q de Kock', 'R Ashwin', 'R Dravid', 'R Parag', 'R Tewatia', 'RA Jadeja', 'RA Tripathi', 'RD Gaikwad', 'RG Sharma', 'RK Singh', 'RM Patidar', 'RR Pant', 'RR Rossouw', 'RV Uthappa', 'Rashid Khan', 'S Dhawan', 'S Dube', 'SA Yadav', 'SC Ganguly', 'SK Raina', 'SM Curran', 'SN Khan', 'SO Hetmyer', 'SP Narine', 'SR Tendulkar', 'SS Iyer', 'SS Tiwary', 'SV Samson', 'Shahbaz Ahmed', 'Shubman Gill', 'TH David', 'TM Head', 'Tilak Varma', 'V Kohli', 'V Sehwag', 'V Shankar', 'VR Iyer', 'WP Saha', 'Washington Sundar', 'YBK Jaiswal', 'Yuvraj Singh']


st.sidebar.title("IPL Data Analytics")
option = st.sidebar.selectbox('Select One', ['Batsman'])

def load_batsman_details(batsman):
    st.title(batsman)
    col111, col112 = st.columns(2)
    with col111:
        st.image(f'players/{batsman}.png', width=400)
        run_against_teams = new_df.pivot_table(index='batter', columns='bowling_team', values='batsman_runs', aggfunc='sum').loc[batsman].sort_values(ascending=False)
        season_wise_data = new_df.pivot_table(index='batter', columns='season', values='batsman_runs', aggfunc='sum').loc[batsman]
    
    with col112:
        st.title("IPL Career Analysis")
        col17,col18,col19 = st.columns(3)
        player = player_data[player_data['Name'] == batsman]
    
        with col17:
            st.metric('Total Runs',str(player['runs'].values[0]))
        with col18:
            st.metric('Fours', str(player['fours'].values[0]))

        with col19:
            st.metric('Sixes', str(player['sixes'].values[0]))

        col20, col21, col22 = st.columns(3)
        with col20:
            st.metric('Strike Rate', str(round(player['strike_rate'].values[0], 2)))
        with col21:
            try:
                pom = matches.groupby(['player_of_match', 'season'])['id'].count().reset_index(level='season').loc[batsman]
                is_series_pom = 1
            except:
                st.metric("Total Man of Match Award",'0')
            else:
                if is_series_pom:
                    st.metric('Total Man of Match Award', str(pom['id']))
                else:  
                    st.metric('Total Man of Match Award', str(pom['id'].values.sum()))
        with col22:
            try:
                player_no_of_50 = batsman_run_ge50.groupby(['season', 'batter'])['batsman_runs'].count().reset_index(level='season').loc[batsman]
                is_series_50 = player_no_of_50.shape[1]
            except:
                st.metric("Half Centuries", '0')
            else:
                global is_half_century
                is_half_century = 1
                if is_series_50:
                    st.metric("Half Centuries", str(player_no_of_50['batsman_runs']))
                else:
                    st.metric("Half Centuries", str(player_no_of_50['batsman_runs'].values.sum()))

        col23, col24, col25, col26 = st.columns(4)
        
        with col23:
            try:
                player_no_of_100 = batsman_run_ge100.groupby(['season', 'batter'])['batsman_runs'].count().reset_index(level='season').loc[batsman]
                is_series_100 = player_no_of_50.shape[1]
            except:
                st.metric("Centuries", '0')
            else:
                global century_hai
                century_hai = 1
                if is_series_50:
                    st.metric("Half Centuries", str(player_no_of_100['batsman_runs']))
                else:
                    st.metric("Half Centuries", str(player_no_of_100['batsman_runs'].values.sum()))


        with col24:
            # try:
            #     player_no_of_30 = batsman_run_ge30.groupby(['season', 'batter'])['batsman_runs'].count().reset_index(level='season').loc[batsman]
            #     is_series = player_no_of_30.shape[1]
            # except:
            #     st.metric('30+ Runs', '0')
            # else:
            #     global is_thirty_plus
            #     is_thirty_plus = 1
            #     if is_series == 1:
            #         st.metric('30+ Runs', str(player_no_of_30['batsman_runs']))
            #     else:
            #         st.metric('30+ Runs', str(player_no_of_30['batsman_runs'].values.sum()))
            st.metric('Ducks', str(duck[duck['batter'] == batsman]['batsman_runs'].values[0]))
        with col25:
            st.metric('High Score', str(highest_score[highest_score['batter'] == batsman]['batsman_runs'].values[0]))

            
    col1, col2 = st.columns(2)

    with col1:
        
        fig, ax = plt.subplots()
        ax.bar(run_against_teams.index, run_against_teams.values)
        plt.title(f"'{batsman}' Runs Against Each Team")
        plt.xticks(rotation=45)
        ax.set_xlabel('Team Name')
        ax.set_ylabel('Total Runs')
        plt.show()
        st.pyplot(fig)

    with col2:
        fig2, ax2 = plt.subplots()
        plt.plot(season_wise_data.index, season_wise_data.values, marker='o')
        plt.title(f"Year Wise '{batsman}' Total Runs")
        ax2.set_xlabel("Year")
        ax2.set_ylabel("Runs Scored")
        plt.xticks(rotation=90)
        plt.show()
        st.pyplot(fig2)

    col3, col4 = st.columns(2)

    with col3:
        df_batter_season = new_df[new_df['batter']  == batsman]
        runs = df_batter_season.groupby('season')['batsman_runs'].sum()
        balls = df_batter_season.groupby(['season','match_id'])['batsman_runs'].count().reset_index().groupby('season')['batsman_runs'].sum()
        runs = runs.reset_index()
        new_data = runs.merge(balls, on='season')
        new_data['strike_rate'] = (new_data['batsman_runs_x']/new_data['batsman_runs_y']) * 100
        fig3, ax3 = plt.subplots()
        plt.plot(new_data['season'], new_data['strike_rate'], marker='o')
        plt.title(f"{batsman}'s Strike Rate Over Years")
        plt.xticks(rotation=45)
        ax3.set_xlabel('Year')
        ax3.set_ylabel('Strike Rate')
        plt.show()
        st.pyplot(fig3)

    with col4:
        
        if is_half_century == 1:
            fig4, ax4 = plt.subplots()
            plt.bar(player_no_of_50['season'], player_no_of_50['batsman_runs'])
            plt.title(f"{batsman}'s 50+ runs over years")
            ax4.set_xlabel('Year')
            ax4.set_ylabel("No of 50's")
            plt.xticks(rotation=45)
            plt.show()
            st.pyplot(fig4)
        else:
            st.markdown(f"# No Half Centuries by {batsman}")
        

    col5, col6 = st.columns(2)

    with col5:

        if century_hai == 1:
            fig5, ax5 = plt.subplots()
            plt.bar(player_no_of_100['season'], player_no_of_100['batsman_runs'])
            plt.title(f"{batsman}'s 100+ runs over years")
            ax5.set_xlabel('Year')
            ax5.set_ylabel("No of 100's")
            plt.xticks(rotation=45)
            plt.show()
            st.pyplot(fig5)
        else:
            st.markdown(f'# 0 centuries hit by {batsman} in IPL Career')
        
    
    with col6:
        if is_thirty_plus == 1:
            fig6, ax6 = plt.subplots()
            plt.bar(player_no_of_30['season'], player_no_of_30['batsman_runs'])
            plt.title(f"{batsman}'s 30+ runs over years")
            ax6.set_xlabel('Year')
            ax6.set_ylabel("No of 30's")
            plt.xticks(rotation=45)
            plt.show()
            st.pyplot(fig6)
        else:
            st.markdown(f'# 0 runs between 30 and 49 hit by {batsman} in IPL Career')


    col7, col8 = st.columns(2)

    with col7:
        try:
            total_run_in_each_over = new_df.pivot_table(index=['batter'], columns=['over'], values='batsman_runs', aggfunc='sum').loc[batsman]
            total_run_in_each_over.fillna(0, inplace=True)
            
            max_index = total_run_in_each_over.idxmax()

            explode = [0.2 if i == max_index else 0 for i in range(1, len((total_run_in_each_over.values)) + 1)]

        except:
            st.markdown(f"{batsman}'s has not scored runs")
        else:
            fig7, ax = plt.subplots()
            ax.pie(total_run_in_each_over.values, labels=total_run_in_each_over.index, autopct='%1.1f%%', explode=explode)
            ax.axis('equal')
            plt.title(f"{batsman}'s runs distribution in each over" )
            plt.show()
            st.pyplot(fig7)
            
    with col8:
        try:
            season_fours = pd.pivot_table(new_df, values='batsman_runs',index='batter', columns='season', aggfunc=lambda x: (x == 4).sum()).loc[batsman]
        except:
            st.markdwon(f"0 Fours hit by {batsman} in IPL Career")
        else:
            fig8, ax = plt.subplots()
            plt.plot(season_fours, marker='*')
            plt.title(f"{batsman}'s Fours in IPL Career")
            ax.set_ylabel('No of Fours')
            ax.set_xlabel('Year')
            plt.xticks(rotation=45)
            plt.show()
            st.pyplot(fig8)

    col9, col10 = st.columns(2)

    with col9:
        try:
            season_sixes = pd.pivot_table(new_df, values='batsman_runs',index='batter', columns='season', aggfunc=lambda x: (x == 6).sum()).loc[batsman]
        except:
            st.markdown(f"0 sixes by {batsman} in IPL Career")
        else:
            fig9, ax = plt.subplots()
            plt.plot(season_sixes, marker='*')
            plt.title(f"{batsman} Sixes in IPL Carrer")
            plt.ylabel('No of sixes')
            plt.xlabel('Year')
            plt.xticks(rotation=45)
            plt.show()
            st.pyplot(fig9)

    with col10:
        try:
            label_sixes = pd.pivot_table(new_df, values='batsman_runs',index='batter', columns='over_label', aggfunc=lambda x: (x == 6).sum()).loc[batsman]
            label_sixes.fillna(0, inplace=True)
            max_index = label_sixes.idxmax()
            explode = [0.05 if i == max_index else 0 for i in ['death_over', 'middle_over', 'power_play', ]]
        except:
            st.markdwon(f"0 sixes by {batsman} in Each Category")
        else:
            fig10, ax = plt.subplots()
            ax.pie(label_sixes.values,labels=label_sixes.index, autopct='%1.1f%%', explode=explode)
            plt.title(f'{label_sixes.name} Sixes in each Category')
            plt.show()
            st.pyplot(fig10)

    col11, col12 = st.columns(2)

    with col11:
        try:
            label_fours = pd.pivot_table(new_df, values='batsman_runs',index='batter', columns='over_label', aggfunc=lambda x: (x == 4).sum()).loc[batsman]
            label_fours.fillna(0, inplace=True)
            max_index = label_fours.idxmax()
        except:
            st.markdwon(f"# 0 Fours by {batsman} in Each Category")
        else:
            fig11, ax = plt.subplots()
            explode = [0.05 if i == max_index else 0 for i in ['death_over', 'middle_over', 'power_play', ]]
            ax.pie(label_fours.values,labels=label_fours.index, autopct='%1.1f%%', explode=explode)
            plt.title(f'{label_fours.name} Fours in each category')
            plt.show()
            st.pyplot(fig11)
        
    with col12:
        try:
            total_four_per_over = pd.pivot_table(new_df, values='batsman_runs',index='batter', columns='over', aggfunc=lambda x: (x == 4).sum()).loc[batsman]
            total_four_per_over.fillna(0, inplace=True)
            max_index = total_four_per_over.idxmax()
            explode = [0.2 if i == max_index else 0 for i in range(1, len((total_four_per_over.values)) + 1)]
        except:
            st.markdown(f"0 fours in each over by {batsman}")
        else:
            fig12, ax = plt.subplots()
            plt.title(f'{batsman}\'s Fours in each Over')
            plt.pie(total_four_per_over.values, labels=total_four_per_over.index, autopct='%1.1f%%', explode=explode)
            plt.show()
            st.pyplot(fig12)

    col13, col14 = st.columns(2)

    with col13:
        try:
            total_sixes_per_over = pd.pivot_table(new_df, values='batsman_runs',index='batter', columns='over', aggfunc=lambda x: (x == 6).sum()).loc[batsman]
            total_sixes_per_over.fillna(0, inplace=True)
            max_index = total_sixes_per_over.idxmax()
            explode = [0.2 if i == max_index else 0 for i in range(1, len((total_sixes_per_over.values)) + 1)]
        except:
            st.markdown(f"0 sixes in each over by {batsman}")
        else:
            fig13, ax = plt.subplots()
            ax.pie(total_sixes_per_over.values, labels=total_sixes_per_over.index, autopct='%1.1f%%', explode=explode)
            plt.title(f"{batsman}'s total sixes distribution in each over")
            plt.show()
            st.pyplot(fig13)

    with col14:
        try:
            over_label_anlysis =  new_df.pivot_table(index='batter', columns='over_label', values='batsman_runs', aggfunc='sum').loc[batsman]
            over_label_anlysis.fillna(0, inplace=True)
            max_index = over_label_anlysis.idxmax()
            explode = [0.05 if i == max_index else 0 for i in ['death_over', 'middle_over', 'power_play', ]]
        except:
            st.markdwon(f"{batsman} has not played batting")
        else:
            fig14, ax = plt.subplots()
            ax.pie(over_label_anlysis.values, labels=over_label_anlysis.index, autopct='%1.1f%%', explode=explode)
            plt.title(f"{batsman}'s distribution of runs in each category")
            plt.show()
            st.pyplot(fig14)

    col15, col16 = st.columns(2)

    with col15:
        try:
            pom = matches.groupby(['player_of_match', 'season'])['id'].count().reset_index(level='season').loc[batsman]
        except:
            st.markdown(f"# 0 Man of the Match Award for {batsman}")
            
        else:
            fig15, ax = plt.subplots()
            ax.bar(pom['season'], pom['id'])
            plt.title(f"{batsman}'s player of match award in IPL Career across years")
            ax.set_xlabel('Year')
            ax.set_ylabel("No of POM Award")
            plt.xticks(rotation=45)
            plt.show()
            st.pyplot(fig15)
        

if option == 'Batsman':
    selected_batsman = st.sidebar.selectbox('Select Batsman', player_list)
    # sorted(list(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button(f'Find {selected_batsman} Details')

    if btn2:
        load_batsman_details(selected_batsman)
       
# elif option == 'Bowler':
#     # selected_investor = st.sidebar.selectbox('Select Startup',sorted(list(set(df['investors'].str.split(',').sum()))))
#     # btn2 = st.sidebar.button('Find Investor Details')

#     # if btn2:
#     #     # load_investor_details(selected_investor)
#     st.title('Bowler')