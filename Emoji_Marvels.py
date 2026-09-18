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

    if u_ans1 == "spider man":
        st.success("✅ ข้อ 1: Excellent💯")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: 🤡🤡🤡 (คุณตอบ '{u_ans1}')")

  
    if u_ans2 == "captain america":
        st.success("✅ ข้อ 2: NICE 🤩")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: 😭😭😭 (คุณตอบ '{u_ans2}')")

    if u_ans3 == "thor":
       st.success("✅ ข้อ 3: Good job 😎😎😎")
       score += 1
    else:
        st.error(f"❌ ข้อ 3: 😔😔😔 (คุณตอบ '{u_ans3}')")
        
    if u_ans4 == "loki":
       st.success("✅ ข้อ 4 : Hodjadpre~😃😃😃")
       score += 1
    else:  
        st.error(f"❌ ข้อ 4: 😡😡😡 (คุณตอบ '{u_ans4}')")

    if u_ans5 == "dr.doom":
        st.success("✅ ข้อ 5: 👍GOOD😊💯")
        score += 1
    else:
        st.error(f"❌ ข้อ 5: Oh no 😭 (คุณตอบ '{u_ans5}')")

    if u_ans6 == "hawk eye":
        st.success("✅ ข้อ 6: That's right✅")
        score += 1
    else:
        st.error(f"❌ ข้อ 6: Try again 🤡🤡 (คุณตอบ '{u_ans6}')")

    if u_ans7 == "iron man":
       st.success("✅ ข้อ 7: Good 😊")
       score += 1
    else:
        st.error(f"❌ ข้อ 7: Nah uh 💩💩💩(คุณตอบ '{u_ans7}')")
      
    if u_ans8 == "black widow":
       st.success("✅ ข้อ 8: FR!? 🤯🤯🤯")
        
    else:  
        st.error(f"❌ ข้อ 8: Try again 🧐🧐🧐(คุณตอบ '{u_ans8}')")

    if u_ans9 == "hulk":
        st.success("✅ ข้อ 9: WoW😮😯😱")
        score += 1
    else:
        st.error(f"❌ ข้อ 9: Hell nah (คุณตอบ '{u_ans9}')")
        
    if u_ans10 == "falcon":
        st.success("✅ ข้อ 10: Amazing😍😈🥶")
        score += 1
    else:
        st.error(f"❌ ข้อ 10: 🥷☠️😭 (คุณตอบ '{u_ans10}')")

    st.info(f"🗿📊 TOTAL SCORE: {score} คะแนน🔥")

    if score == 10:
        st.success("👽🤴🗿God!!!")
    if 5 <= score <=9:
        st.warning("🤑🤩Pro🤠😞")
    if 1 <= score <=4:
        st.error ("🌚💀Noob👎🤡") 

st.button("🔥🔥START🔥🔥", on_click=reset_game)


if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(200 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

ans1 = st.text_input(
    "Q1. ❤️🕸️🕷️ ",
    value=st.session_state.ans1,
)
ans2 = st.text_input(
    "Q2. 🛡️ ⭐ ",
    value=st.session_state.ans2,
)
ans3 = st.text_input(
    "Q3. ⚡🔨💪  ",
    value=st.session_state.ans3,
)
ans4 = st.text_input(
    "Q4. ⏳ 👑🐍 ",
    value=st.session_state.ans4,
)
ans5 = st.text_input(
    "Q5. 👑🤖🟩 ",
    value=st.session_state.ans5,
)
ans6 = st.text_input(
    "Q6. 🦅🏹🎯   ",
    value=st.session_state.ans6,
)
ans7 = st.text_input(
    "Q7. ❤️‍🔥🦾🟥💛 ",
    value=st.session_state.ans7,
)
ans8 = st.text_input(
    "Q8.   🕷👩    ",
    value=st.session_state.ans8,
)
ans9 = st.text_input(
    "Q9. 💪💚☢️ ",
    value=st.session_state.ans9,
)
ans10 = st.text_input(
    "Q10. .🦅👩🏾‍🦲i ",
    value=st.session_state.ans10,
)

st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4
st.session_state.ans5_val = ans5
st.session_state.ans6_val = ans6
st.session_state.ans7_val = ans7
st.session_state.ans8_val = ans8
st.session_state.ans9_val = ans9
st.session_state.ans10_val = ans10

if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("Finished🔥🔥🔥"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    st.rerun()
if st.session_state.get("is_ended", False):
    show_result_dialog(ans1,ans2,ans3,ans4,ans5,ans6,ans7,ans8,ans9,ans10)

st.divider()
st.warning("พิมด้วยพิมเล็กทั้งหมดและเว้นวรรคด้วย***")

