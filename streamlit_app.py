import streamlit as st
import random

# Define the result dictionary
results = {
    "rock": {
        "paper": False,
        "scr": True
    },
    "paper": {
        "rock": True,
        "scr": False
    },
    "scr": {
        "rock": False,
        "paper": True
    }
}

# Streamlit title
st.title("Rock Paper Scissors Game")

# Create a selection box for the user to pick rock, paper, or scissors
user_choice = st.selectbox("Select rock, paper, or scissors:", ["rock", "paper", "scr"])

# Create a button to start the game
if st.button("Play"):
    # Remove user choice from the list and let the computer pick a random choice
    arr = ["rock", "paper", "scr"]
    arr.remove(user_choice)
    computer_choice = random.choice(arr)
    
    # Get the result of the game
    status = results[user_choice][computer_choice]
    
    # Display the computer's choice
    st.write(f"Computer selected: {computer_choice}")
    
    # Display the result of the game
    if status:
        st.write("You won!")
    else:
        st.write("You lose!")
