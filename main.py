import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit.components.v1 as components

# Title of the app
st.title("European Championship 2024 Prediction Game")

# Description
st.write("Visualizing the scores of the players")

# Load data from the specific sheet 'Blad1' in the Excel file
excel_file = 'euro-calcs.xlsx'
df = pd.read_excel(excel_file, sheet_name='Blad1')

# Extract player names from the columns
players = df.columns.tolist()

# Get the latest scores (assuming the last row has the latest scores)
latest_scores = df.iloc[-1].tolist()

# Create DataFrame for latest scores
data_latest = pd.DataFrame({
    'Player': players,
    'Score': latest_scores
})

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
    height=500,
    showlegend=False  # Hide the legend
)

# Customize hover effects
fig.update_traces(
    texttemplate='%{text}', 
    textposition='outside',
    hoverinfo='text+name'
)

# Display the bar chart in the Streamlit app
st.plotly_chart(fig, use_container_width=True)

# Button to show score progression
if st.button('Show Score Progression'):
    # Prepare data for progression chart
    df['Gameweek'] = df.index + 1  # Add a Gameweek column for reference
    data_progression = df.melt(id_vars=['Gameweek'], var_name='Player', value_name='Score')
    
    fig_progression = px.bar(
        data_progression,
        x='Player',
        y='Score',
        color='Gameweek',
        title='Score Progression of Players',
        labels={'Player': 'Players', 'Score': 'Scores', 'Gameweek': 'Gameweek'},
        template='plotly_white',
        text='Score'  # Add text labels to bars
    )

    # Customize layout for better mobile experience and aesthetics
    fig_progression.update_layout(
        barmode='stack',  # Stack the bars
        title_font_size=24,
        xaxis_tickangle=-45,
        xaxis_title_font_size=16,
        yaxis_title_font_size=16,
        margin=dict(l=40, r=40, t=40, b=40),
        height=600
    )
    
    st.plotly_chart(fig_progression, use_container_width=True)

# JavaScript for full-screen functionality
fullscreen_button = """
    <script>
    function fullScreen() {
        var elem = document.querySelector('.stPlotlyChart');
        if (elem.requestFullscreen) {
            elem.requestFullscreen();
        } else if (elem.mozRequestFullScreen) { /* Firefox */
            elem.mozRequestFullScreen();
        } else if (elem.webkitRequestFullscreen) { /* Chrome, Safari & Opera */
            elem.webkitRequestFullscreen();
        } else if (elem.msRequestFullscreen) { /* IE/Edge */
            elem.msRequestFullscreen();
        }
    }
    </script>
    <button onclick="fullScreen()">Expand Chart</button>
"""

# Display the button
components.html(fullscreen_button, height=50)
