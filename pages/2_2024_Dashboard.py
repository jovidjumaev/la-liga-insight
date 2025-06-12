import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="La Liga 2024 Dashboard",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Metric Names and Explanations ---
metric_full_names = {
    'PrgP': 'Progressive Passes (PrgP)',
    'KP': 'Key Passes (KP)',
    'xA': 'Expected Assists (xA)',
    'Ast': 'Assists (Ast)',
    'Cmp%': 'Pass Completion % (Cmp%)',
    'Save%': 'Save Percentage (Save%)',
    'CS': 'Clean Sheets (CS)',
    'GA': 'Goals Against (GA)',
    'GA90': 'Goals Against per 90 (GA90)'
}

metric_explanations = {
    'PrgP': 'Progressive Passes (PrgP) are completed passes that move the ball significantly forward towards the opponent\'s goal.',
    'KP': 'Key Passes (KP) are passes that directly lead to a teammate taking a shot.',
    'xA': 'Expected Assists (xA) estimate the likelihood that a given pass will become a goal assist.',
    'Ast': 'Assists (Ast) are passes that directly result in a goal.',
    'Cmp%': 'Pass Completion % (Cmp%) is the percentage of attempted passes that are completed.',
    'Save%': 'Save Percentage (Save%) is the percentage of shots on target that the goalkeeper saves.',
    'CS': 'Clean Sheets (CS) are matches in which the team conceded zero goals.',
    'GA': 'Goals Against (GA) is the total number of goals conceded.',
    'GA90': 'Goals Against per 90 (GA90) is the average number of goals conceded per 90 minutes.'
}

# --- Load Data ---
table = pd.read_csv('data/2024_table.csv')
passing = pd.read_csv('data/2024_passing.csv', header=1)
goalkeeping = pd.read_csv('data/2024_goalkeeping.csv', header=1)
matches = pd.read_csv('data/2024_laliga_matches.csv')

table.columns = table.columns.str.strip()
passing.columns = passing.columns.str.strip()
goalkeeping.columns = goalkeeping.columns.str.strip()
matches.columns = matches.columns.str.strip()

st.title("La Liga 2024 General Dashboard")
st.markdown("> **Explore league-wide trends, efficiency, and style in La Liga 2024.**")

# --- Tabs for Main Categories ---
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "💭 My Thoughts", 
    "🏅 Overview", 
    "📈 Passing Analysis", 
    "🧤 Goalkeeping Analysis", 
    "📊 League Trends",
    "⚽ Barcelona Analysis"
])

with tab1:
    st.markdown("## 💭 My Thoughts on La Liga 2024")
    
    st.markdown("""
### 🔥 A Season to Remember
As a lifelong Barça fan, this season felt like a dream. 28 wins, 102 goals, and a +63 goal difference—this was more than stats, it was a statement. Under Flick, we found our identity again: fearless, fluid, and full of fire.
""")

    st.markdown("""
### 🏆 The Title Race
- We topped the league with 88 points, staying 4 clear of Madrid—sweet, right?
- Lewandowski led with 27 goals, proving he's still world-class
- Our defense? Rock solid—just 39 goals conceded all season
- Madrid pushed hard with Mbappé's 31 goals, but our consistency outshone them
""")

    st.markdown("""
### ⚽ The Barça Way Is Back
- 22,000+ completed passes at 86.8%—we controlled games like chess
- 2,200 progressive passes showed our direct intent, not just possession for show
- Full-backs bombing forward, midfielders threading magic—it was classic yet modern Barça
- 2,000+ passes into the final third? That's domination
""")

    st.markdown("""
### 📊 Numbers Don't Lie
- 91.5 xG → 102 goals = clinical finishing
- 72 assists = team chemistry at its best
- xGA of 41.9 shows defensive discipline
- +49.5 xGD tells the full story: total control
""")

    st.markdown("""
### 💙 What Made This Team Special
1. **Lethal Attack** – We didn't just create chances, we buried them  
2. **Strong Backline** – Rarely shaky, always focused  
3. **Midfield Control** – Pedri, Gavi, Frenkie? Pure poetry  
4. **Youth + Experience** – Yamal and Raphinha shined alongside our veterans
""")

    st.markdown("""
### 🚀 The Road Ahead
- Flick's system is working—players believe in it  
- Our young stars are stepping up big time  
- We've built a solid foundation, and Europe is the next frontier  
- We're no longer just pretty football—we're winners again
""")

    st.markdown("""
### 🗣️ My Barça Heart Speaks
This season reminded me why I love this club. The style, the passion, the unity—it all clicked. Watching Yamal dance down the wing, Lewa doing Lewa things, and Flick masterminding from the sidelines made every match worth it.

We didn't just win—we won our way.
""")

    st.divider()

    st.markdown("""
*Just my thoughts as a passionate Barça fan who's been cheering, stressing, and celebrating through every minute this season. The data supports it—but the feeling says it all.*
""")


with tab2:
    st.markdown("## 🏅 La Liga 2024 Overview")
    st.markdown("### Key Records")
    # Prepare all 9 key records
    key_cards = []
    # 1. Most Wins
    key_cards.append(("Most Wins", table.loc[table['W'].idxmax(), 'Squad'], f"{table['W'].max()} wins"))
    # 2. Most Goals For
    key_cards.append(("Most Goals For", table.loc[table['GF'].idxmax(), 'Squad'], f"{table['GF'].max()} goals"))
    # 3. Fewest Goals Against
    key_cards.append(("Fewest Goals Against", table.loc[table['GA'].idxmin(), 'Squad'], f"{table['GA'].min()} goals"))
    # 4. Most Draws
    key_cards.append(("Most Draws", table.loc[table['D'].idxmax(), 'Squad'], f"{table['D'].max()} draws"))
    # 5. Best Goal Difference
    key_cards.append(("Best Goal Difference", table.loc[table['GD'].idxmax(), 'Squad'], f"{table['GD'].max()} GD"))
    # 6. Most Losses
    key_cards.append(("Most Losses", table.loc[table['L'].idxmax(), 'Squad'], f"{table['L'].max()} losses"))
    # 7. Worst Goal Difference
    key_cards.append(("Worst Goal Difference", table.loc[table['GD'].idxmin(), 'Squad'], f"{table['GD'].min()} GD"))
    # 8. Most Clean Sheets
    if 'CS' in goalkeeping.columns:
        most_cs_team = goalkeeping.loc[goalkeeping['CS'].astype(float).idxmax(), 'Squad']
        most_cs = int(goalkeeping['CS'].astype(float).max())
        key_cards.append(("Most Clean Sheets", most_cs_team, f"{most_cs} clean sheets"))
    else:
        key_cards.append(("Most Clean Sheets", '-', '-'))
    # 9. Most Red Cards (or fallback to Fewest Losses)
    if 'CrdR' in table.columns:
        most_red_team = table.loc[table['CrdR'].astype(float).idxmax(), 'Squad']
        most_red = int(table['CrdR'].astype(float).max())
        key_cards.append(("Most Red Cards", most_red_team, f"{most_red} red cards"))
    elif 'CrdY' in table.columns:
        most_yellow_team = table.loc[table['CrdY'].astype(float).idxmax(), 'Squad']
        most_yellow = int(table['CrdY'].astype(float).max())
        key_cards.append(("Most Yellow Cards", most_yellow_team, f"{most_yellow} yellow cards"))
    else:
        fewest_losses_team = table.loc[table['L'].astype(float).idxmin(), 'Squad']
        fewest_losses = int(table['L'].astype(float).min())
        key_cards.append(("Fewest Losses", fewest_losses_team, f"{fewest_losses} losses"))
    # Display in 3x3 grid
    for i in range(0, 9, 3):
        cols = st.columns(3)
        for j in range(3):
            label, team, stat = key_cards[i+j]
            cols[j].markdown(f"""
                <div style='background-color:#2c3e50; border-radius:8px; padding:0.7em; text-align:center; transition: transform 0.3s ease;'>
                    <b style='color:#fff;'>{label}</b><br>
                    <span style='font-size:1.2em; color:#3498db;'><b>{team}</b></span><br>
                    <span style='color:#eceff1;'>{stat}</span>
                </div>
            """, unsafe_allow_html=True)
    st.divider()
    st.markdown("### League Table")
    st.dataframe(
        table[['Rk', 'Squad', 'Pts', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'xG', 'xGA', 'xGD']].sort_values('Rk'),
        use_container_width=True,
        hide_index=True,
        height=600
    )
    st.caption("This table summarizes the final league standings and key stats for each team in La Liga 2024.")
    st.divider()
    matches['result'] = np.where(
        matches['score.fullTime.home'] > matches['score.fullTime.away'], 'Home Win',
        np.where(matches['score.fullTime.home'] < matches['score.fullTime.away'], 'Away Win', 'Draw')
    )
    most_common_result = matches['result'].value_counts().idxmax()
    # More league facts
    total_goals = int(table['GF'].sum())
    avg_goals = total_goals / (len(table) * 38)
    matches['total_goals'] = matches['score.fullTime.home'].astype(float) + matches['score.fullTime.away'].astype(float)
    highest_scoring = matches.loc[matches['total_goals'].idxmax()]
    most_common_score = matches.groupby(['score.fullTime.home', 'score.fullTime.away']).size().idxmax()
    st.info(f"Most common result: {most_common_result}")
    st.success(f"Total goals: {total_goals} | Avg goals per team per match: {avg_goals:.2f}")
    st.info(f"Highest scoring match: {highest_scoring['homeTeam.name']} {int(highest_scoring['score.fullTime.home'])} - {int(highest_scoring['score.fullTime.away'])} {highest_scoring['awayTeam.name']} ({int(highest_scoring['total_goals'])} goals)")
    st.info(f"Most common scoreline: {most_common_score[0]} - {most_common_score[1]}")
    st.caption("All stats and records are for the 2024 La Liga season. Explore other tabs for deeper insights!")

with tab3:
    st.header("Passing Trends")
    passing_metrics = ['PrgP', 'KP', 'xA', 'Ast', 'Cmp%']
    passing_options = [metric_full_names[m] for m in passing_metrics]
    selected_full = st.selectbox("Select passing metric to rank teams:", passing_options)
    selected_metric = passing_metrics[passing_options.index(selected_full)]
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=passing.sort_values(selected_metric, ascending=False), x=selected_metric, y='Squad', palette='viridis', ax=ax)
    ax.set_title(f'{metric_full_names[selected_metric]} by Team')
    ax.set_xlabel(metric_full_names[selected_metric])
    ax.set_ylabel('Team')
    st.pyplot(fig)
    st.caption(f"This bar chart shows which teams led La Liga in {metric_full_names[selected_metric]} during the 2024 season. {metric_explanations[selected_metric]}")
    with st.expander("Distribution of Pass Completion %"):
        fig2, ax2 = plt.subplots(figsize=(8, 4))
        sns.histplot(passing['Cmp%'].astype(float), bins=10, kde=True, color='dodgerblue', ax=ax2)
        ax2.set_title('Distribution of Pass Completion % (Cmp%)')
        ax2.set_xlabel('Pass Completion % (Cmp%)')
        st.pyplot(fig2)
        st.caption("This histogram displays how pass completion rates are distributed across all teams. Pass Completion % (Cmp%) is the percentage of attempted passes that are completed.")
    with st.expander("Passing Impact Analysis"):
        df = pd.merge(passing, table, on='Squad', suffixes=('_pass', '_table'))
        for col in ['PrgP', 'KP', 'xA', 'Ast', 'Cmp%', 'GF', 'Pts', 'xG']:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        fig3, ax3 = plt.subplots(figsize=(10,6))
        sns.scatterplot(data=df, x='PrgP', y='GF', s=100, hue='Pts', palette='viridis', ax=ax3)
        for i, row in df.iterrows():
            ax3.text(row['PrgP'], row['GF'], row['Squad'], fontsize=9, ha='right')
        ax3.set_title('Progressive Passes (PrgP) vs. Goals Scored (GF)')
        ax3.set_xlabel('Progressive Passes (PrgP)')
        ax3.set_ylabel('Goals Scored (GF)')
        st.pyplot(fig3)
        st.caption("This scatter plot explores the relationship between Progressive Passes (PrgP) and Goals Scored (GF), colored by total points. Progressive Passes are completed passes that move the ball significantly forward.")
        fig4, ax4 = plt.subplots(figsize=(10,6))
        sns.scatterplot(data=df, x='PrgP', y='Pts', s=100, hue='GF', palette='magma', ax=ax4)
        for i, row in df.iterrows():
            ax4.text(row['PrgP'], row['Pts'], row['Squad'], fontsize=9, ha='right')
        ax4.set_title('Progressive Passes (PrgP) vs. Points (Pts)')
        ax4.set_xlabel('Progressive Passes (PrgP)')
        ax4.set_ylabel('Points (Pts)')
        st.pyplot(fig4)
        st.caption("This scatter plot shows how Progressive Passes (PrgP) relate to total Points (Pts), with color indicating Goals Scored (GF).")
        st.markdown("**Tip:** Hover over points to see team names.")
    with st.expander("Key Passes, Expected Assists, and Assists by Team"):
        fig5, axes = plt.subplots(1, 3, figsize=(24, 7))
        sns.barplot(data=passing.sort_values('KP', ascending=False), x='KP', y='Squad', ax=axes[0], palette='crest')
        axes[0].set_title('Key Passes (KP) by Team')
        axes[0].set_xlabel('Key Passes (KP)')
        axes[0].set_ylabel('Team')
        sns.barplot(data=passing.sort_values('xA', ascending=False), x='xA', y='Squad', ax=axes[1], palette='viridis')
        axes[1].set_title('Expected Assists (xA) by Team')
        axes[1].set_xlabel('Expected Assists (xA)')
        axes[1].set_ylabel('')
        sns.barplot(data=passing.sort_values('Ast', ascending=False), x='Ast', y='Squad', ax=axes[2], palette='magma')
        axes[2].set_title('Assists (Ast) by Team')
        axes[2].set_xlabel('Assists (Ast)')
        axes[2].set_ylabel('')
        st.pyplot(fig5)
        st.caption("These bar charts compare teams by Key Passes (KP), Expected Assists (xA), and actual Assists (Ast). Key Passes are passes leading to a shot; Expected Assists estimate the likelihood a pass becomes a goal.")

with tab4:
    st.header("Goalkeeping Trends")
    gk_metrics = ['Save%', 'CS', 'GA', 'GA90']
    gk_options = [metric_full_names[m] for m in gk_metrics]
    selected_gk_full = st.selectbox("Select goalkeeping metric to rank teams:", gk_options)
    selected_gk_metric = gk_metrics[gk_options.index(selected_gk_full)]
    goalkeeping[selected_gk_metric] = pd.to_numeric(goalkeeping[selected_gk_metric], errors='coerce')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=goalkeeping.sort_values(selected_gk_metric, ascending=False), x=selected_gk_metric, y='Squad', palette='crest', ax=ax)
    ax.set_title(f'{metric_full_names[selected_gk_metric]} by Team')
    ax.set_xlabel(metric_full_names[selected_gk_metric])
    ax.set_ylabel('Team')
    st.pyplot(fig)
    st.caption(f"This bar chart shows which teams led La Liga in {metric_full_names[selected_gk_metric]} during the 2024 season. {metric_explanations[selected_gk_metric]}")

with tab5:
    st.header("Match & League Trends")
    st.markdown("### League-wide Goal Trends")
    if 'matchday' in matches.columns:
        goals_per_matchday = matches.groupby('matchday').apply(
            lambda x: x['score.fullTime.home'].astype(float).sum() + x['score.fullTime.away'].astype(float).sum()
        )
        fig, ax = plt.subplots(figsize=(12, 4))
        ax.plot(goals_per_matchday.index, goals_per_matchday.values, marker='o', color='#1f77b4')
        ax.set_title('Total Goals per Matchday')
        ax.set_xlabel('Matchday')
        ax.set_ylabel('Goals')
        st.pyplot(fig)
        st.caption("This line chart shows the total number of goals scored in each matchday across the league.")

        # Interactive matchday selector
        matchday = st.slider("Select a matchday to view details:", int(goals_per_matchday.index.min()), int(goals_per_matchday.index.max()), int(goals_per_matchday.index.min()))
        md_matches = matches[matches['matchday'] == matchday][['homeTeam.name', 'score.fullTime.home', 'awayTeam.name', 'score.fullTime.away', 'status']].copy()
        md_matches.columns = ['Home Team', 'Home Goals', 'Away Team', 'Away Goals', 'Status']

        # Team name mapping for consistency with league table
        team_name_map = {
            'Athletic Club': 'Athletic Club',
            'CA Osasuna': 'Osasuna',
            'Club Atlético de Madrid': 'Atlético Madrid',
            'Cádiz CF': 'Cádiz',
            'Deportivo Alavés': 'Alavés',
            'Getafe CF': 'Getafe',
            'Girona FC': 'Girona',
            'Granada CF': 'Granada',
            'RC Celta de Vigo': 'Celta Vigo',
            'RCD Mallorca': 'Mallorca',
            'Rayo Vallecano de Madrid': 'Rayo Vallecano',
            'Real Betis Balompié': 'Betis',
            'Real Madrid CF': 'Real Madrid',
            'Real Sociedad de Fútbol': 'Real Sociedad',
            'Sevilla FC': 'Sevilla',
            'UD Almería': 'Almería',
            'UD Las Palmas': 'Las Palmas',
            'Valencia CF': 'Valencia',
            'Villarreal CF': 'Villarreal'
        }
        md_matches['Home Team'] = md_matches['Home Team'].map(team_name_map).fillna(md_matches['Home Team'])
        md_matches['Away Team'] = md_matches['Away Team'].map(team_name_map).fillna(md_matches['Away Team'])
        md_matches.index = np.arange(1, len(md_matches) + 1)
        st.markdown(f"#### Matchday {matchday} Results")
        st.dataframe(md_matches)
        st.caption("See all results for the selected matchday. Team names are now consistent with the League Table, and indexing starts from 1.")

    st.markdown("### Distribution of Goals per Match")
    matches['total_goals'] = matches['score.fullTime.home'].astype(float) + matches['score.fullTime.away'].astype(float)
    fig2, ax2 = plt.subplots(figsize=(8, 4))
    sns.histplot(matches['total_goals'], bins=range(0, int(matches['total_goals'].max())+2), kde=False, color='#ff7f0e', ax=ax2)
    ax2.set_title('Distribution of Total Goals per Match')
    ax2.set_xlabel('Total Goals in Match')
    ax2.set_ylabel('Number of Matches')
    st.pyplot(fig2)
    st.caption("This histogram shows how many matches had a given number of total goals.")

    st.markdown("### Most and Least Entertaining Matches")
    most_goals = matches.loc[matches['total_goals'].idxmax()]
    least_goals = matches.loc[matches['total_goals'].idxmin()]
    st.info(f"**Most goals in a match:** {most_goals['homeTeam.name']} {int(most_goals['score.fullTime.home'])} - {int(most_goals['score.fullTime.away'])} {most_goals['awayTeam.name']} (Total: {int(most_goals['total_goals'])})")
    st.info(f"**Fewest goals in a match:** {least_goals['homeTeam.name']} {int(least_goals['score.fullTime.home'])} - {int(least_goals['score.fullTime.away'])} {least_goals['awayTeam.name']} (Total: {int(least_goals['total_goals'])})")

    st.markdown("### League-wide Result Rates")
    total_matches = len(matches)
    draws = (matches['score.fullTime.home'] == matches['score.fullTime.away']).sum()
    home_wins = (matches['score.fullTime.home'] > matches['score.fullTime.away']).sum()
    away_wins = (matches['score.fullTime.home'] < matches['score.fullTime.away']).sum()
    st.success(f"Draw rate: {draws/total_matches:.1%} | Home win rate: {home_wins/total_matches:.1%} | Away win rate: {away_wins/total_matches:.1%}")

    st.markdown("### Correlation Matrix: Passing, Goals, Points")
    with st.expander("Show Correlation Matrix"):
        df = pd.merge(passing, table, on='Squad', suffixes=('_pass', '_table'))
        corr_cols = ['PrgP', 'KP', 'xA', 'Ast', 'Cmp%', 'GF', 'Pts', 'xG']
        for col in corr_cols:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        corr = df[corr_cols].corr()
        fig3, ax3 = plt.subplots(figsize=(8, 6))
        sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', ax=ax3)
        ax3.set_title('Correlation Matrix: Passing, Goals, Points')
        st.pyplot(fig3)
        st.caption("This heatmap visualizes the correlations between key passing, scoring, and points metrics across all teams.")

with tab6:
    st.markdown("## ⚽ Barcelona Analysis")
    st.markdown("### My Favorite Team's Performance")
    
    # --- Prepare Barcelona match data at the very top of the tab ---
    barca_matches = matches[
        (matches['homeTeam.name'] == 'FC Barcelona') | 
        (matches['awayTeam.name'] == 'FC Barcelona')
    ].copy()
    
    barca_matches['matchday'] = pd.to_numeric(barca_matches['matchday'])
    barca_matches = barca_matches.sort_values('matchday')
    
    def get_result(row):
        if row['homeTeam.name'] == 'FC Barcelona':
            if row['score.fullTime.home'] > row['score.fullTime.away']:
                return 'W'
            elif row['score.fullTime.home'] < row['score.fullTime.away']:
                return 'L'
            else:
                return 'D'
        else:
            if row['score.fullTime.away'] > row['score.fullTime.home']:
                return 'W'
            elif row['score.fullTime.away'] < row['score.fullTime.home']:
                return 'L'
            else:
                return 'D'
    
    def get_opponent(row):
        if row['homeTeam.name'] == 'FC Barcelona':
            return row['awayTeam.name']
        else:
            return row['homeTeam.name']
    
    barca_matches['Result'] = barca_matches.apply(get_result, axis=1)
    barca_matches['Opponent'] = barca_matches.apply(get_opponent, axis=1)
    barca_matches['GF'] = barca_matches.apply(lambda x: x['score.fullTime.home'] if x['homeTeam.name'] == 'FC Barcelona' else x['score.fullTime.away'], axis=1)
    barca_matches['GA'] = barca_matches.apply(lambda x: x['score.fullTime.away'] if x['homeTeam.name'] == 'FC Barcelona' else x['score.fullTime.home'], axis=1)
    barca_matches['Points'] = barca_matches['Result'].map({'W': 3, 'D': 1, 'L': 0})

    # Get Barcelona's data
    barca_data = table[table['Squad'] == 'Barcelona'].iloc[0]
    barca_passing = passing[passing['Squad'] == 'Barcelona'].iloc[0]
    barca_gk = goalkeeping[goalkeeping['Squad'] == 'Barcelona'].iloc[0]
    
    # Key Performance Metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("League Position", f"{barca_data['Rk']}th", f"{barca_data['Pts']} points")
    with col2:
        st.metric("Goals Scored", barca_data['GF'], f"xG: {barca_data['xG']:.1f}")
    with col3:
        ga = float(barca_data['GA'])
        xga = float(barca_data['xGA'])
        if ga > xga:
            st.markdown(f"""
                <div style='text-align: center;'>
                    <div style='font-size: 0.8rem; font-weight: 200; color: #fff;'>Goals Against</div>
                    <div style='font-size: 2.2rem; font-weight: 100; color: #fff; line-height: 1.5;'>{ga:.0f}</div>
                    <div style='font-size: 1.1rem; color: red; font-weight: 300; line-height: 1.2;'>↓ xGA: {xga:.1f}</div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div style='text-align: center;'>
                    <div style='font-size: 0.8rem; font-weight: 200; color: #fff;'>Goals Against</div>
                    <div style='font-size: 2.2rem; font-weight: 100; color: #fff; line-height: 1.5;'>{ga:.0f}</div>
                    <div style='font-size: 1.1rem; color: green; font-weight: 300; line-height: 1.2;'>↑ xGA: {xga:.1f}</div>
                </div>
            """, unsafe_allow_html=True)
    
    st.divider()
    
    # --- Helper function for ranking arrows ---
    def rank_arrow(rank, total_teams, reverse=False):
        # Lower rank is better unless reverse=True
        if reverse:
            good = rank > total_teams // 2
        else:
            good = rank <= total_teams // 2
        if good:
            arrow = '↑'
            color = 'green'
        else:
            arrow = '↓'
            color = 'red'
        return f'<span style="color:{color}; font-weight:bold">{arrow} {int(rank)}th</span>'

    # --- Performance Analysis Rankings ---
    st.markdown("### Performance Analysis")
    total_teams = len(table)
    col1, col2, col3 = st.columns(3)
    # Define metrics before using them
    clinicality = float(barca_data['GF']) - float(barca_data['xG'])
    clinicality_rank = (table['GF'].astype(float) - table['xG'].astype(float)).rank(ascending=False).loc[table['Squad'] == 'Barcelona'].iloc[0]
    def_resilience = float(barca_data['xGA']) - float(barca_data['GA'])
    def_resilience_rank = (table['xGA'].astype(float) - table['GA'].astype(float)).rank(ascending=False).loc[table['Squad'] == 'Barcelona'].iloc[0]
    over_performance = float(barca_data['Pts']) / float(barca_data['xGD'])
    over_performance_rank = (table['Pts'].astype(float) / table['xGD'].astype(float)).rank(ascending=False).loc[table['Squad'] == 'Barcelona'].iloc[0]
    with col1:
        st.markdown(f"Clinicality: <b>{clinicality:+.1f}</b> {rank_arrow(clinicality_rank, total_teams)}", unsafe_allow_html=True)
    with col2:
        st.markdown(f"Defensive Resilience: <b>{def_resilience:+.1f}</b> {rank_arrow(def_resilience_rank, total_teams)}", unsafe_allow_html=True)
    with col3:
        st.markdown(f"Over/Underperformance: <b>{over_performance:.2f}x</b> {rank_arrow(over_performance_rank, total_teams)}", unsafe_allow_html=True)

    st.divider()

    # --- Passing Analysis Rankings ---
    st.markdown("### Passing Analysis")
    passing_metrics = {
        'Cmp%': 'Pass Completion %',
        'PrgP': 'Progressive Passes',
        'KP': 'Key Passes',
        'xA': 'Expected Assists',
        'Ast': 'Assists',
        '1/3': 'Final Third Passes',
        'PPA': 'Penalty Area Passes',
        'CrsPA': 'Crosses into Penalty Area',
        'PrgDist': 'Progressive Distance'
    }
    col1, col2 = st.columns(2)
    with col1:
        for metric, label in list(passing_metrics.items())[:4]:
            value = float(barca_passing[metric])
            rank = passing[metric].astype(float).rank(ascending=False).loc[passing['Squad'] == 'Barcelona'].iloc[0]
            st.markdown(f"{label}: <b>{value:.1f}</b> {rank_arrow(rank, total_teams)}", unsafe_allow_html=True)
    with col2:
        for metric, label in list(passing_metrics.items())[4:]:
            value = float(barca_passing[metric])
            rank = passing[metric].astype(float).rank(ascending=False).loc[passing['Squad'] == 'Barcelona'].iloc[0]
            st.markdown(f"{label}: <b>{value:.1f}</b> {rank_arrow(rank, total_teams)}", unsafe_allow_html=True)

    st.divider()

    # --- Goalkeeping Analysis Rankings ---
    st.markdown("### Goalkeeping Analysis")
    gk_metrics = {
        'CS': 'Clean Sheets',
        'Save%': 'Save %',
        'GA90': 'Goals Against/90',
        'SoTA': 'Shots on Target Against',
        'Saves': 'Total Saves',
        'PKsv': 'Penalty Kicks Saved'
    }
    col1, col2 = st.columns(2)
    with col1:
        for metric, label in list(gk_metrics.items())[:3]:
            value = float(barca_gk[metric])
            # For GA90, lower is better (so ascending=True)
            if metric == 'GA90':
                rank = goalkeeping[metric].astype(float).rank(ascending=True).loc[goalkeeping['Squad'] == 'Barcelona'].iloc[0]
            else:
                rank = goalkeeping[metric].astype(float).rank(ascending=False).loc[goalkeeping['Squad'] == 'Barcelona'].iloc[0]
            st.markdown(f"{label}: <b>{value:.1f}</b> {rank_arrow(rank, total_teams, reverse=(metric=='GA90'))}", unsafe_allow_html=True)
    with col2:
        for metric, label in list(gk_metrics.items())[3:]:
            value = float(barca_gk[metric])
            if metric == 'GA90':
                rank = goalkeeping[metric].astype(float).rank(ascending=True).loc[goalkeeping['Squad'] == 'Barcelona'].iloc[0]
            else:
                rank = goalkeeping[metric].astype(float).rank(ascending=False).loc[goalkeeping['Squad'] == 'Barcelona'].iloc[0]
            st.markdown(f"{label}: <b>{value:.1f}</b> {rank_arrow(rank, total_teams, reverse=(metric=='GA90'))}", unsafe_allow_html=True)

    st.divider()

    # --- Passing Profile Table ---
    st.markdown("#### Barcelona Passing Profile")
    barca_metrics_passing = ['Cmp%', 'PrgP', 'KP', 'xA', 'Ast']
    barca_profile = pd.DataFrame(barca_passing[barca_metrics_passing]).T
    barca_profile['GF'] = barca_data['GF']
    barca_profile['Pts'] = barca_data['Pts']
    barca_profile_display = barca_profile.rename(columns={
        'Cmp%': 'Pass Completion %',
        'PrgP': 'Progressive Passes',
        'KP': 'Key Passes',
        'xA': 'Expected Assists',
        'Ast': 'Assists',
        'GF': 'Goals For',
        'Pts': 'Points'
    })
    barca_profile_display['Team'] = 'Barcelona'
    barca_profile_display = barca_profile_display[['Team'] + [col for col in barca_profile_display.columns if col != 'Team']]
    st.table(barca_profile_display.reset_index(drop=True))

    # --- Top Teams Passing Comparison Table ---
    st.markdown("#### Top Teams Passing Comparison")
    top_teams = ['Real Madrid', 'Barcelona', 'Girona', 'Atlético Madrid', 'Athletic Club']
    top_df = passing[passing['Squad'].isin(top_teams)].set_index('Squad')
    top_df_table = table[table['Squad'].isin(top_teams)].set_index('Squad')
    top_df_combined = top_df[['Cmp%', 'PrgP', 'KP', 'xA', 'Ast']].copy()
    top_df_combined['GF'] = top_df_table['GF']
    top_df_combined['Pts'] = top_df_table['Pts']
    col_rename = {
        'Cmp%': 'Pass Completion %',
        'PrgP': 'Progressive Passes',
        'KP': 'Key Passes',
        'xA': 'Expected Assists',
        'Ast': 'Assists',
        'GF': 'Goals For',
        'Pts': 'Points'
    }
    top_df_combined_display = top_df_combined.rename(columns=col_rename)
    top_df_combined_display = top_df_combined_display.reset_index().rename(columns={'Squad': 'Team'})
    # Sort by Points in descending order
    top_df_combined_display = top_df_combined_display.sort_values('Points', ascending=False)
    st.dataframe(top_df_combined_display.reset_index(drop=True), use_container_width=True)

    # --- Pass Length Profile Table ---
    st.markdown("#### Barcelona Pass Length Profile")
    length_metrics = ['Cmp%', 'Cmp%.1', 'Cmp%.2', 'Cmp%.3', 'PrgDist', 'TotDist']
    barca_length = barca_passing[length_metrics]
    barca_length_display = pd.DataFrame([barca_length.values], columns=[
        'Total Pass Completion %',
        'Short Pass Completion %',
        'Medium Pass Completion %',
        'Long Pass Completion %',
        'Progressive Distance',
        'Total Distance'
    ])
    barca_length_display.index = ['Barcelona']
    st.dataframe(barca_length_display.reset_index(), use_container_width=True)

    # --- Top Teams Pass Length Comparison Table ---
    st.markdown("#### Top Teams Pass Length Comparison")
    top_df_length = top_df[length_metrics].rename(columns={
        'Cmp%': 'Total Cmp%',
        'Cmp%.1': 'Short Cmp%',
        'Cmp%.2': 'Medium Cmp%',
        'Cmp%.3': 'Long Cmp%',
        'PrgDist': 'Progressive Distance',
        'TotDist': 'Total Distance'
    })
    length_col_rename = {
        'Total Cmp%': 'Total Pass Completion %',
        'Short Cmp%': 'Short Pass Completion %',
        'Medium Cmp%': 'Medium Pass Completion %',
        'Long Cmp%': 'Long Pass Completion %',
        'PrgDist': 'Progressive Distance',
        'TotDist': 'Total Distance'
    }
    top_df_length_display = top_df_length.rename(columns=length_col_rename)
    top_df_length_display = top_df_length_display.reset_index().rename(columns={'Squad': 'Team'})
    # Sort by Total Pass Completion % in descending order
    top_df_length_display = top_df_length_display.sort_values('Total Pass Completion %', ascending=False)
    st.dataframe(top_df_length_display, use_container_width=True)

    # --- Points Won Against Each Opponent ---
    st.markdown("#### Points Won Against Each Opponent")
    st.markdown("""
    <span style='color:#bbb;'>This chart shows the total number of points Barcelona earned against each La Liga opponent during the season. 3 points for a win, 1 for a draw, 0 for a loss. It highlights which teams Barcelona performed best and worst against.</span>
    """, unsafe_allow_html=True)
    points_vs_opponent = barca_matches.groupby('Opponent')['Points'].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(8, 6))
    points_vs_opponent.plot(kind='barh', color='royalblue', ax=ax)
    ax.set_title('Points Won by Barcelona vs Each Opponent')
    ax.set_xlabel('Points')
    ax.set_ylabel('Opponent')
    st.pyplot(fig)

    # --- Barcelona Results Sequence ---
    st.markdown("#### Barcelona Results Sequence")
    st.markdown("""
    <span style='color:#bbb;'>This visual shows the sequence of Barcelona's match results throughout the season. Each bar represents a matchday: green for a win, orange for a draw, and red for a loss. It helps you quickly spot streaks and patterns in performance.</span>
    """, unsafe_allow_html=True)
    colors = barca_matches['Result'].map({'W': 'green', 'D': 'orange', 'L': 'red'})
    fig, ax = plt.subplots(figsize=(14, 1.5))
    ax.scatter(barca_matches['matchday'], np.ones_like(barca_matches['matchday']), c=colors, s=200, marker='|')
    ax.set_yticks([])
    ax.set_title('Barcelona Results Sequence (Green=Win, Orange=Draw, Red=Loss)')
    ax.set_xlabel('Matchday')
    st.pyplot(fig)

    # --- Barcelona Match-by-Match Results Table ---
    st.markdown("#### Barcelona Match-by-Match Results")
    barca_matches_sorted = barca_matches.sort_values('matchday')
    barca_matches_sorted_display = barca_matches_sorted.rename(columns={
        'matchday': 'Matchday',
        'Opponent': 'Opponent',
        'GF': 'Goals For',
        'GA': 'Goals Against',
        'Result': 'Result',
        'Points': 'Points'
    })
    # Sort by Matchday only, not by Points
    barca_matches_sorted_display = barca_matches_sorted_display.sort_values('Matchday', ascending=True)
    st.dataframe(barca_matches_sorted_display[['Matchday', 'Opponent', 'Goals For', 'Goals Against', 'Result', 'Points']].reset_index(drop=True), use_container_width=True)

    st.markdown("""
    ---
    *Dashboard by Jovid Jumaev. Built with Streamlit, pandas, matplotlib, seaborn.*
    """) 