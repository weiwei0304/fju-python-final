def tryQuiz():
    score = 0
    inputQ1 = input('Q1. 你想離職的念頭有多久?\n1.至少數個月以上\n2.最近開始，瘋狂想辭職\n')
    if(inputQ1 == '1'):
        score = score + 1
    inputQ2 = input('Q2. 你身體是否開始出現狀況（如：睡不好、易有情緒、體重大幅上升或下降...等）?\n1.是，目前開始有健康狀況上\n2.否，目前身體尚未有異常狀況\n')
    if(inputQ2 == '1'):
        score = score + 1
    inputQ3 = input('Q3. 你的財務狀況如何?\n1.還可以，戶頭可用存款至少有三個月的生活費\n2.有點緊，戶頭可用存款小於三個月生活費\n')
    if(inputQ3 == '1'):
        score = score + 1

    return score

def render_quiz_ui():
    import streamlit as st
    st.markdown("請依序回答問題，按照自身狀況選擇選項：")
    st.markdown("---")
    
    # 問題 1
    q1_options = ["1. 至少數個月以上", "2. 最近開始，瘋狂想辭職"]
    q1 = st.radio(
        "Q1. 你想離職的念頭有多久?",
        options=q1_options,
        key="quiz_q1_radio",
        index=None  # 不預設選項
    )
    
    st.markdown("---")
    
    # 問題 2
    q2_options = ["1. 是，目前開始有健康狀況", "2. 否，目前身體尚未有異常狀況"]
    q2 = st.radio(
        "Q2. 你身體是否開始出現狀況（如：睡不好、易有情緒、體重大幅上升或下降...等）?",
        options=q2_options,
        key="quiz_q2_radio",
        index=None  # 不預設選項
    )
    
    st.markdown("---")
    
    # 問題 3
    q3_options = ["1. 還可以，戶頭可用存款至少有三個月的生活費", "2. 有點緊，戶頭可用存款小於三個月生活費"]
    q3 = st.radio(
        "Q3. 你的財務狀況如何?",
        options=q3_options,
        key="quiz_q3_radio",
        index=None  # 不預設選項
    )
    
    return q1, q2, q3

def calculate_quiz_score_from_answers(q1, q2, q3):
    score = 0
    if q1 and q1[0] == "1":
        score += 1
    if q2 and q2[0] == "1":
        score += 1
    if q3 and q3[0] == "1":
        score += 1
    return score
