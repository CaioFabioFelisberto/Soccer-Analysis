import pandas as pd
import plotly.express as px

def generate_playmakers_scatter():
    df = pd.read_csv('top5-players.csv')

    # 1 - Playmakers vs Dribblers

    df_playmakers = df[df['Pos'].str.contains('MF|FW', na=False)].copy()

    df_playmakers = df_playmakers[df_playmakers['90s'] > 5.0]

    df_playmakers['PrgP_90'] = df_playmakers['PrgP'] / df_playmakers['90s']
    df_playmakers['PrgP_90'] = df_playmakers['PrgP_90'].round(2)

    df_playmakers['PrgC_90'] = df_playmakers['PrgC'] / df_playmakers['90s']
    df_playmakers['PrgC_90'] = df_playmakers['PrgC_90'].round(2)

    df_playmakers['Score_Total_90'] = df_playmakers['PrgC_90'] + df_playmakers['PrgP_90']

    interest_columns = ['Player', 'Pos', '90s', 'PrgP_90', 'PrgC_90', 'Score_Total_90']

    playmakers = df_playmakers[interest_columns].sort_values(by='PrgP_90', ascending=False)
    dribblers = df_playmakers[interest_columns].sort_values(by='PrgC_90',ascending=False)
    top_players = df_playmakers[interest_columns].sort_values(by='Score_Total_90', ascending=False)

    fig = px.scatter(
        df_playmakers, 
        x='PrgP_90', 
        y='PrgC_90',
        trendline='ols',
        trendline_scope='overall',
        labels={'PrgP_90': 'Progressive Passes per 90', 'PrgC_90': 'Progressive Carries per 90'}, 
        color='Pos',    
        hover_name='Player', 
        title='Playmakers DNA: Passes vs Conduction (Europa Top 5 Leagues) 23/24' 
    )

    return fig.to_html(full_html=False, include_plotlyjs='cdn')

def generate_scorers_scatter():
    df = pd.read_csv('top5-players.csv')

    df_scorers = df[df['Gls'] > 0].copy()
    df_scorers = df_scorers[df_scorers['90s'] > 5.0]

    df_scorers['G-PK_90'] = (df_scorers['G-PK'] / df_scorers['90s']).round(2)
    df_scorers['npxG_90'] = (df_scorers['npxG'] / df_scorers['90s']).round(2)

    interest_columns = ['Player', 'Pos', '90s', 'Gls', 'G-PK_90', 'npxG_90']

    penalty_specialists = df_scorers[interest_columns].sort_values(by='Gls',ascending=True)
    killers = df_scorers[interest_columns].sort_values(by='Gls',ascending=False)

    fig = px.scatter(
        df_scorers, 
        x='G-PK_90', 
        y='npxG_90',
        trendline='ols',
        trendline_scope='overall',
        labels={'G-PK_90': 'Goals from PK per 90', 'npxG_90': 'Non-Penalty Expected Goals per 90'}, 
        color='Pos',    
        hover_name='Player', 
        title='Scorers DNA: Goals from PK vs Non-Penalty Expected Goals (Europa Top 5 Leagues) 23/24' 
    )
    return fig.to_html(full_html=False,include_plotlyjs='cdn')

def generate_wonderkid_bar():
    df = pd.read_csv('top5-players.csv')

    df_kids = df[(df['Age'] <= 21) & (df['npxG'] > 0) & (df['xAG'] > 0)].copy()

    df_kids['npxGxAG'] = ((df_kids['npxG'] + df_kids['xAG']) / 90).round(2)

    interest_columns = ['Player', 'Age', 'Born', 'Pos', '90s', 'Gls', 'Ast', 'npxGxAG']

    kids = df_kids[interest_columns].sort_values(by='npxGxAG',ascending=False)

    fig = px.bar(
        kids, 
        x='Player', 
        y='npxGxAG', 
        color='Pos', 
        hover_data=['Age', 'Born', '90s', 'Gls', 'Ast'], 
        title='Wonderkid Scouting: Non-Penalty Expected Goals + Expected Assists per 90 (Europa Top 5 Leagues) 23/24'
    )
    return fig.to_html(full_html=False, include_plotlyjs='cdn')

def generate_player_radar(player1,player2):

    df = pd.read_csv('top5-players.csv')

    df = df[df['90s'] >= 5.0].copy() 

    df['PrgP_90'] = df['PrgP'] / df['90s']
    df['PrgC_90'] = df['PrgC'] / df['90s']
    df['Gls_90'] = df['Gls'] / df['90s']
    df['Ast_90'] = df['Ast'] / df['90s']

    player_1 = player1
    player_2 = player2

    df_comparacao = df[df['Player'].isin([player_1, player_2])].copy()

    colunas_interesse = ['Player', 'PrgP_90', 'PrgC_90', 'Gls_90', 'Ast_90']
    df_radar_largo = df_comparacao[colunas_interesse]

    df_radar_longo = df_radar_largo.melt(id_vars=['Player'], var_name='Metrica', value_name='Valor')

    fig = px.line_polar(
        df_radar_longo,
        r='Valor',
        theta='Metrica',
        color='Player',
        line_close=True,
        title=f"Raio-X: {player_1} vs {player_2}"
    )
    return fig.to_html(full_html=False, include_plotlyjs='cdn')

def generate_reality_check_scatter():
    df = pd.read_csv('top5-players.csv')

    df_check = df[df['Gls'] > 0].copy()
    df_check = df_check[df_check['90s'] > 5.0]

    df_check['xG'] = (df_check['xG'] / df_check['90s']).round(2)
    df_check['Gls'] = (df_check['Gls'] / df_check['90s']).round(2)

    fig = px.scatter(
        df_check, 
        x='xG', 
        y='Gls',
        trendline='ols',
        trendline_scope='overall',
        labels={'xG': 'Expected Goals per 90', 'Gls': 'Actual Goals per 90'}, 
        color='Pos',    
        hover_name='Player', 
        title='Reality Check: Expected Goals vs Actual Goals (Europa Top 5 Leagues) 23/24' 
    )

    return fig.to_html(full_html=False,include_plotlyjs='cdn')

def generate_league_dna_boxplot():
    df = pd.read_csv('top5-players.csv')

    df_league = df[df['90s'] > 5.0].copy()

    df_league['PrgP_90'] = df_league['PrgP'] / df_league['90s']

    fig = px.box(
        df_league, 
        x='Comp', 
        y='PrgP_90', 
        color='Comp',
        hover_name='Player',
        labels={'PrgP_90': 'Progressive Passes per 90', 'Comp': 'League'},
        title='League DNA: Progressive Passes per 90 (Europa Top 5 Leagues) 23/24'
    )
    return fig.to_html(full_html=False, include_plotlyjs='cdn')