import streamlit as st
from datetime import datetime
import pytz
import time

# -------------------------
# 한국 시간 설정
# -------------------------
KST = pytz.timezone("Asia/Seoul")


def get_kst_time():
    return datetime.now(KST)


# -------------------------
# 상태 초기화
# -------------------------
if "alarm_time" not in st.session_state:
    st.session_state.alarm_time = None

if "alarm_triggered" not in st.session_state:
    st.session_state.alarm_triggered = False


# -------------------------
# UI
# -------------------------
st.title("⏰ 알람 앱 (한국 시간 기준)")

alarm_input = st.text_input("알람 시간 입력 (예: 14:30)")

if st.button("알람 설정"):
    st.session_state.alarm_time = alarm_input
    st.session_state.alarm_triggered = False
    st.success(f"알람 설정 완료: {alarm_input}")


# -------------------------
# 현재 한국 시간
# -------------------------
now = get_kst_time().strftime("%H:%M:%S")
st.markdown(f"### 🕒 현재 한국 시간: {now}")


# -------------------------
# 알람 체크
# -------------------------
if st.session_state.alarm_time:

    current_time = get_kst_time().strftime("%H:%M")

    st.markdown(f"### ⏰ 설정된 알람: {st.session_state.alarm_time}")

    if current_time == st.session_state.alarm_time and not st.session_state.alarm_triggered:

        st.session_state.alarm_triggered = True

        st.balloons()
        st.error("🔔 알람 울림!")
        st.success("⏰ 설정한 시간이 되었습니다!")


# -------------------------
# 자동 새로고침
# -------------------------
time.sleep(1)
st.rerun()
