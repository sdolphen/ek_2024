import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit.components.v1 as components

# Title of the app
st.title("European Championship 2024 Prediction Game")

# Description
st.write("Visualizing the scores of the players")

# Placeholder for actual player names and scores to be copied from Excel
players = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy", "Karl", "Laura", "Mallory", "Nina", "Oscar", "Peggy", "Quentin"]
scores = [10, 5, 3, 8, 12, 7, 6, 11, 4, 15, 9, 2, 14, 1, 13, 16, 17]

# Create a DataFrame
data = pd.DataFrame({
    'Player': players,
    'Score': scores
})

# Sort the DataFrame by score in descending order
data = data.sort_values(by='Score', ascending=False)

# Create a bar chart using Plotly with enhanced style
fig = px.bar(
    data, 
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

# Display the bar chart in the Streamlit app
st.plotly_chart(fig, use_container_width=True)

# Add the tweet below the bar chart using iframe
tweet_url = "https://x.com/EURO2024/status/1801255704197533986"  # Replace with your tweet URL
tweet_embed_url = f"https://twitframe.com/show?url={tweet_url}"
components.iframe(tweet_embed_url, height=600)
