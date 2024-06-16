import streamlit as st
import pandas as pd
import plotly.express as px

# Function to load data from the Excel file
def load_data():
    excel_file = 'euro-calcs.xlsx'
    return pd.read_excel(excel_file, sheet_name='Blad1')

# Title of the app
st.title("EK Prono 2024")

# Load data from the specific sheet 'Blad1' in the Excel file
dfs = load_data()

# Extract player names from the columns
players = dfs.columns.tolist()

# Get the latest scores (assuming the last row has the latest scores)
latest_scores = dfs.iloc[-1].tolist()

# Analyze data to determine the top three players
total_scores = dfs.sum().reset_index()
total_scores.columns = ['Player', 'Score']
top_three_players = total_scores.nlargest(3, 'Score')

# Display top three players and their scores with enhanced visual appeal
st.subheader("Top Three Players")
cols = st.columns(3)
for rank, (index, row) in enumerate(top_three_players.iterrows(), start=1):
    with cols[rank - 1]:
        st.markdown(f"""
            <div style="text-align: center; padding: 10px; border-radius: 10px; background-color: #f9f9f9; margin: 5px;">
                <h2>{rank}. {row['Player']}</h2>
                <h3 style="color: #4CAF50;">Score: {row['Score']}</h3>
            </div>
        """, unsafe_allow_html=True)

# Create DataFrame for latest scores
data_latest = pd.DataFrame({
    'Player': players,
    'Score': latest_scores
})

# State to keep track of sorting
if 'is_sorted' not in st.session_state:
    st.session_state.is_sorted = False

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
    # Reload the data to ensure it reflects the latest changes
    dfs = load_data()
    total_scores = dfs.sum().reset_index()
    total_scores.columns = ['Player', 'Score']
    total_scores_sorted = total_scores.sort_values(by='Score', ascending=False)
    st.subheader("Sorted Total Scores")
    create_bar_chart(total_scores_sorted, 'Total Scores of Players')
else:
    st.subheader("Latest Scores")
    create_bar_chart(data_latest, 'Scores of Players')

# Button to show score progression
if st.button('Show Score Progression'):
    # Reload the data to ensure it reflects the latest changes
    dfs = load_data()
    # Prepare data for progression chart
    dfs['Gameweek'] = dfs.index + 1  # Add a Gameweek column for reference
    data_progression = dfs.melt(id_vars=['Gameweek'], var_name='Player', value_name='Score')
    
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
