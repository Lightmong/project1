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

if "last_user" not in st.session_state:
    st.session_state.last_user = None

if "last_computer" not in st.session_state:
    st.session_state.last_computer = None

if "last_result" not in st.session_state:
    st.session_state.last_result = None

if "game_over" not in st.session_state:
    st.session_state.game_over = False


# -----------------------
# 초기화
# -----------------------
def reset_game():
    st.session_state.game_started = False
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.last_user = None
    st.session_state.last_computer = None
    st.session_state.last_result = None
    st.session_state.game_over = False


# -----------------------
# 승패 판단 함수
# -----------------------
def judge(user, computer):
    if user == computer:
        return "무승부"
    elif (user == "가위" and computer == "보") or \
         (user == "바위" and computer == "가위") or \
         (user == "보" and computer == "바위"):
        return "승리"
    else:
        return "패배"


# =======================
# 시작 화면
# =======================
if not st.session_state.game_started:

    st.title("✊ 가위바위보 ")

    if st.button("🎮 게임시작"):
        st.session_state.game_started = True
        st.rerun()


# =======================
# 게임 화면
# =======================
else:

    st.markdown(f"### 🙋 나 {st.session_state.user_score} : 🤖 {st.session_state.computer_score}")

    # 게임 종료
    if st.session_state.game_over:
        st.success("🏆 게임 종료!")

        if st.session_state.user_score > st.session_state.computer_score:
            st.balloons()
            st.markdown("## 🎉 최종 승리!")
        else:
            st.markdown("## 😢 최종 패배!")

    # 게임 진행
    else:

        st.subheader("가위 / 바위 / 보 선택!")

        col1, col2, col3 = st.columns(3)

        def play(user_choice):
            computer_choice = random.choice(["가위", "바위", "보"])
            result = judge(user_choice, computer_choice)

            st.session_state.last_user = user_choice
            st.session_state.last_computer = computer_choice
            st.session_state.last_result = result

            # 점수 즉시 반영
            if result == "승리":
                st.session_state.user_score += 1
            elif result == "패배":
                st.session_state.computer_score += 1

            # 2선승 체크
            if st.session_state.user_score == 2 or st.session_state.computer_score == 2:
                st.session_state.game_over = True

            st.rerun()


        with col1:
            st.button("✌️ 가위", on_click=play, args=("가위",))

        with col2:
            st.button("✊ 바위", on_click=play, args=("바위",))

        with col3:
            st.button("✋ 보", on_click=play, args=("보",))


        # -----------------------
        # 결과 즉시 표시
        # -----------------------
        if st.session_state.last_user:

            st.divider()
            st.markdown("## 🎯 이번 라운드 결과")

            st.write(f"🙋 나: {st.session_state.last_user}")
            st.write(f"🤖 컴퓨터: {st.session_state.last_computer}")
            st.write(f"### {st.session_state.last_result}")


    # -----------------------
    # 처음으로
    # -----------------------
    st.divider()

    if st.button("🏠 처음으로"):
        reset_game()
        st.rerun()
