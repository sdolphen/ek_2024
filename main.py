import streamlit as st
import pandas as pd

# Title of the app
st.title("European Championship 2024 Prediction Game")

# Description
st.write("Visualizing the scores of the players")

# Copy and paste the scores and player names from your Excel file
# Example:
# players = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy", "Karl", "Laura", "Mallory", "Nina", "Oscar", "Peggy", "Quentin"]
# scores = [10, 5, 3, 8, 12, 7, 6, 11, 4, 15, 9, 2, 14, 1, 13, 16, 17]

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

# Create a bar chart using Streamlit's built-in functionality
st.bar_chart(data.set_index('Player'))
