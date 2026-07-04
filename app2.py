import streamlit as st
import random

# -----------------------
# 초기 상태
# -----------------------
if "game_started" not in st.session_state:
    st.session_state.game_started = False

if "user_score" not in st.session_state:
    st.session_state.user_score = 0

if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

if "game_over" not in st.session_state:
    st.session_state.game_over = False


# -----------------------
# 초기화 함수
# -----------------------
def reset_game():
    st.session_state.game_started = False
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.game_over = False


# =======================
# 1. 시작 화면
# =======================
if not st.session_state.game_started:

    st.title("✊ 가위바위보 (3판 2선승제)")

    if st.button("🎮 게임시작"):
        st.session_state.game_started = True
        st.rerun()


# =======================
# 2. 게임 화면
# =======================
else:

    st.markdown(f"### 🙋 나: {st.session_state.user_score} | 🤖 컴퓨터: {st.session_state.computer_score}")

    if st.session_state.game_over:
        st.success("🏆 게임 종료!")

        if st.session_state.user_score > st.session_state.computer_score:
            st.balloons()
            st.markdown("## 🎉 최종 승리!")
        else:
            st.markdown("## 😢 최종 패배!")

    else:
        st.subheader("가위 / 바위 / 보 선택!")

        user_choice = None

        col1, col2, col3 = st.columns(3)

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
                result = "무승부"
            elif (user_choice == "가위" and computer_choice == "보") or \
                 (user_choice == "바위" and computer_choice == "가위") or \
                 (user_choice == "보" and computer_choice == "바위"):
                result = "승리"
                st.session_state.user_score += 1
            else:
                result = "패배"
                st.session_state.computer_score += 1

            st.markdown("## 🎯 결과")
            st.write(f"🙋 나: {user_choice}")
            st.write(f"🤖 컴퓨터: {computer_choice}")
            st.write(f"### {result}")

            # 2선승 체크
            if st.session_state.user_score == 2 or st.session_state.computer_score == 2:
                st.session_state.game_over = True

    # -----------------------
    # 처음으로 버튼 (항상 존재)
    # -----------------------
    st.divider()

    if st.button("🏠 처음으로"):
        reset_game()
        st.rerun()
