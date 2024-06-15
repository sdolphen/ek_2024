import streamlit as st
import pandas as pd
import plotly.express as px

# Title of the app
st.title("European Championship 2024 Prediction Game")

# Description
st.write("Visualizing the scores of the players")

# Placeholder for actual player names and scores to be copied from Excel
players = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy", "Karl", "Laura", "Mallory", "Nina", "Oscar", "Peggy", "Quentin"]
latest_scores = [10, 5, 3, 8, 12, 7, 6, 11, 4, 15, 9, 2, 14, 1, 13, 16, 17]
previous_scores_1 = [9, 4, 2, 7, 11, 6, 5, 10, 3, 14, 8, 1, 13, 0, 12, 15, 16]
previous_scores_2 = [8, 3, 1, 6, 10, 5, 4, 9, 2, 13, 7, 0, 12, -1, 11, 14, 15]

# Create DataFrame for latest scores
data_latest = pd.DataFrame({
    'Player': players,
    'Score': latest_scores
})

# Sort the DataFrame by score in descending order
data_latest = data_latest.sort_values(by='Score', ascending=False)

# Create a bar chart using Plotly with enhanced style
fig = px.bar(
    data_latest, 
    x='Player', 
    y='Score', 
    title='Scores of Players',
    labels={'Player': 'Players', 'Score': 'Scores'},
    color='Score',
    color_continuous_scale='Blues',
    template='plotly_white',
    text='Score'  # Add text labels to bars
)

# Customize layout for better mobile experience and aesthetics
fig.update_layout(
    title_font_size=24,
    xaxis_tickangle=-45,
    xaxis_title_font_size=16,
    yaxis_title_font_size=16,
    margin=dict(l=40, r=40, t=40, b=40),
    height=500
)

# Customize hover effects
fig.update_traces(
    texttemplate='%{text:.2s}', 
    textposition='outside',
    hoverinfo='text+name'
)

# Button to expand the chart
if st.button('Expand Chart'):
    fig.update_layout(height=800)
else:
    fig.update_layout(height=500)

# Display the bar chart in the Streamlit app
st.plotly_chart(fig, use_container_width=True)

# Button to show score progression
if st.button('Show Score Progression'):
    data_progression = pd.DataFrame({
        'Player': players,
        'Latest Score': latest_scores,
        'Previous Score 1': previous_scores_1,
        'Previous Score 2': previous_scores_2
    })
    
    data_progression = data_progression.melt(id_vars=['Player'], value_vars=['Latest Score', 'Previous Score 1', 'Previous Score 2'],
                                             var_name='Time', value_name='Score')
    
    fig_progression = px.line(
        data_progression,
        x='Player',
        y='Score',
        color='Time',
        title='Score Progression of Players',
        labels={'Player': 'Players', 'Score': 'Scores', 'Time': 'Time'},
        template='plotly_white'
    )
    
    fig_progression.update_layout(
        title_font_size=24,
        xaxis_tickangle=-45,
        xaxis_title_font_size=16,
        yaxis_title_font_size=16,
        margin=dict(l=40, r=40, t=40, b=40),
        height=600
    )
    
    st.plotly_chart(fig_progression, use_container_width=True)
