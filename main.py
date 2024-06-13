import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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

# Create a bar chart
fig, ax = plt.subplots()
bars = ax.bar(data['Player'], data['Score'], color=['blue' if i % 2 == 0 else 'white' for i in range(len(data))])
ax.set_xlabel('Players')
ax.set_ylabel('Scores')
ax.set_title('Scores of Players')

# Rotate the x labels for better readability
plt.xticks(rotation=45)

# Display the bar chart in the Streamlit app
st.pyplot(fig)
