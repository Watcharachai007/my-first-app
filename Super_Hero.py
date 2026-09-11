import time
import streamlit as st

st.title("🔥🦸‍♂️Emoji Marvels🐱‍🏍😎🕷🔥")


if "ans1" not in st.session_state:
    st.session_state.ans1 = ""
if "ans2" not in st.session_state:
    st.session_state.ans2 = ""
if "ans3" not in st.session_state:
    st.session_state.ans3 = ""
if "ans4" not in st.session_state:
    st.session_state.ans4 = ""
if "ans5" not in st.session_state:
    st.session_state.ans5 = ""
if "ans6" not in st.session_state:
    st.session_state.ans6 = ""
if "ans7" not in st.session_state:
    st.session_state.ans7 = ""
if "ans8" not in st.session_state:
    st.session_state.ans8 = ""
if "ans9" not in st.session_state:
    st.session_state.ans9 = ""
if "ans10" not in st.session_state:
    st.session_state.ans10 = ""

def reset_game():
    st.session_state.ans1 = "" 
    st.session_state.ans2 = "" 
    st.session_state.ans3 = "" 
    st.session_state.ans4 = "" 
    st.session_state.ans5 = "" 
    st.session_state.ans6 = "" 
    st.session_state.ans7 = "" 
    st.session_state.ans8 = "" 
    st.session_state.ans9 = "" 
    st.session_state.ans10 = "" 
    st.session_state.start = time.time() 
    st.session_state.is_ended = False 

@st.dialog("Result📊📌⭐⭐⭐⭐⭐")
def show_result_dialog(ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9, ans10):
    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()
    u_ans5 = ans5.strip().lower()
    u_ans6 = ans6.strip().lower()
    u_ans7 = ans7.strip().lower()
    u_ans8 = ans8.strip().lower()
    u_ans9 = ans9.strip().lower()
    u_ans10 = ans10.strip().lower()
   
  
