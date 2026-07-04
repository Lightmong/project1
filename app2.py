import streamlit as st
import random

st.set_page_config(
    page_title="가위바위보 게임",
    page_icon="✊",
    layout="centered"
)

# 상태 초기화
if "game_started" not in st.session_state:
    st.session_state.game_started = False

if "result" not in st.session_state:
    st.session_state.result = None

# CSS
st.markdown("""
<style>
.stApp{
    background-color:#F5F7FA;
}

.title{
    text-align:center;
    font-size:50px;
    font-weight:bold;
    color:#333333;
    margin-top:50px;
    margin-bottom:40px;
}

.result{
    text-align:center;
    font-size:40px;
    font-weight:bold;
    color:#2E7D32;
    margin-top:30px;
}

.info{
    text-align:center;
    font-size:26px;
    margin-top:15px;
}

div.stButton > button{
    width:100%;
    font-size:22px;
    font-weight:bold;
    padding:12px;
    border-radius:12px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">✊ 가위바위보 게임 ✋</div>', unsafe_allow_html=True)

# 게임 시작 버튼
if not st.session_state.game_started:
    if st.button("🎮 게임시작"):
        st.session_state.game_started = True
        st.rerun()

# 게임 진행
else:

    st.subheader("가위, 바위, 보 중 하나를 선택하세요!")

    col1, col2, col3 = st.columns(3)

    user_choice = None

    with col1:
        if st.button("✌️ 가위"):
            user_choice = "가위"

    with col2:
        if st.button("✊ 바위"):
            user_choice = "바위"

    with col3:
        if st.button("✋ 보"):
            user_choice = "보"

    if user_choice:

        computer_choice = random.choice(["가위", "바위", "보"])

        if user_choice == computer_choice:
            result = "🤝 무승부!"
        elif (
            (user_choice == "가위" and computer_choice == "보") or
            (user_choice == "바위" and computer_choice == "가위") or
            (user_choice == "보" and computer_choice == "바위")
        ):
            result = "🎉 승리!"
        else:
            result = "😢 패배!"

        st.markdown(
            '<div class="result">🎯 게임결과</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="info">🙋 나의 선택 : <b>{user_choice}</b></div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="info">🤖 상대의 선택 : <b>{computer_choice}</b></div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="info"><h2>{result}</h2></div>',
            unsafe_allow_html=True
        )

        st.divider()

        if st.button("🏠 처음으로"):
            st.session_state.game_started = True
            st.rerun()
