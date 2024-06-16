import streamlit as st
import pandas as pd
import plotly.express as px

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

# Analyze data to determine the top three players
total_scores = df.sum().reset_index()
total_scores.columns = ['Player', 'Score']
top_three_players = total_scores.nlargest(3, 'Score')

# Display top three players and their scores with enhanced visual appeal
st.subheader("Top Three Players")
cols = st.columns(min(len(top_three_players), 3))
for index, row in top_three_players.iterrows():
    with cols[index]:
        st.markdown(f"""
            <div style="text-align: center; padding: 10px; border-radius: 10px; background-color: #f9f9f9; margin: 5px;">
                <h2>{index + 1}. {row['Player']}</h2>
                <h3 style="color: #4CAF50;">Score: {row['Score']}</h3>
            </div>
        """, unsafe_allow_html=True)

# Create DataFrame for latest scores
data_latest = pd.DataFrame({
    'Player': players,
    'Score': latest_scores
})

# Function to create and display the bar chart
def create_bar_chart(data, title):
    fig = px.bar(
        data, 
        x='Player', 
        y='Score', 
        title=title,
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
    
    st.plotly_chart(fig, use_container_width=True)

# Button to sort values based on total score
if st.button('Sort Scores by Total'):
    total_scores_sorted = total_scores.sort_values(by='Score', ascending=False)
    st.subheader("Sorted Total Scores")
    create_bar_chart(total_scores_sorted, 'Total Scores of Players')
else:
    st.subheader("Latest Scores")
    create_bar_chart(data_latest, 'Scores of Players')

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
