import streamlit as st
import pandas as pd
import random

# Load Questions from CSV
def load_questions():
    data = {
        "question": [
            "What is the output of 2 ** 3 in Python?",
            "Which of the following is NOT a programming language?",
            "What does HTML stand for?",
            "What is the time complexity of binary search?",
            "Which keyword is used to define a function in Python?"
        ],
        "options": [
            ["5", "6", "8", "10"],
            ["Python", "Java", "HTML", "C++"],
            ["Hyper Transfer Markup Language", "Hyper Text Markup Language", "High Text Machine Learning", "None of the above"],
            ["O(n)", "O(log n)", "O(n^2)", "O(1)"],
            ["func", "define", "def", "function"]
        ],
        "answer": ["8", "HTML", "Hyper Text Markup Language", "O(log n)", "def"]
    }
    return pd.DataFrame(data)

# Streamlit App Title
st.title("💻 Programming Quiz App")

# Load Questions
df = load_questions()

# Initialize Session State
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.current_question = 0
    st.session_state.quiz_completed = False

# Display Question
if st.session_state.current_question < len(df):
    question = df.iloc[st.session_state.current_question]
    st.subheader(f"Q{st.session_state.current_question + 1}: {question['question']}")

    selected_option = st.radio("Select your answer:", question["options"])

    if st.button("Submit"):
        if selected_option == question["answer"]:
            st.session_state.score += 1
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Wrong! The correct answer is: {question['answer']}")

        st.session_state.current_question += 1
        
else:
    st.session_state.quiz_completed = True

# Show Final Score
if st.session_state.quiz_completed:
    st.subheader("🎉 Quiz Completed!")
    st.write(f"Your final score: {st.session_state.score}/{len(df)}")
    if st.button("Restart Quiz"):
        st.session_state.score = 0
        st.session_state.current_question = 0
        st.session_state.quiz_completed = False
