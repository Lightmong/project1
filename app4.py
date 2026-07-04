import streamlit as st
from datetime import datetime
import time

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
st.title("⏰ 알람 앱")

st.markdown("### 원하는 시간을 설정하세요 (24시간 형식)")

alarm_input = st.text_input("예: 14:30 또는 07:05")

if st.button("알람 설정"):
    st.session_state.alarm_time = alarm_input
    st.session_state.alarm_triggered = False
    st.success(f"알람 설정 완료: {alarm_input}")


# -------------------------
# 현재 시간
# -------------------------
now = datetime.now().strftime("%H:%M:%S")
st.markdown(f"### 🕒 현재 시간: {now}")


# -------------------------
# 알람 체크
# -------------------------
if st.session_state.alarm_time:

    st.markdown(f"### ⏰ 설정된 알람: {st.session_state.alarm_time}")

    current_time = datetime.now().strftime("%H:%M")

    if current_time == st.session_state.alarm_time and not st.session_state.alarm_triggered:

        st.session_state.alarm_triggered = True

        st.balloons()
        st.error("🔔 알람 울림!")
        st.warning("⏰ 시간이 되었습니다!")


# -------------------------
# 자동 새로고침 (핵심)
# -------------------------
st.markdown("⏳ 1초마다 자동 갱신")

time.sleep(1)
st.rerun()
