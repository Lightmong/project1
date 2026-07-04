import streamlit as st

st.set_page_config(
    page_title="첫 웹페이지",
    page_icon="👋",
    layout="centered"
)

# 상태 초기화
if "page" not in st.session_state:
    st.session_state.page = "main"

if "balloons_shown" not in st.session_state:
    st.session_state.balloons_shown = False

# CSS
st.markdown("""
<style>
.stApp {
    background-color: #2B2B2B;
    color: white;
}

.title {
    text-align: center;
    font-size: 60px;
    font-weight: bold;
    margin-top: 120px;
    margin-bottom: 60px;
}

.success {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #FFD54F;
    margin-top: 120px;
    margin-bottom: 50px;
}

div.stButton > button {
    width: 100%;
    background-color: #FFD54F;
    color: black;
    font-size: 22px;
    font-weight: bold;
    border-radius: 12px;
    border: none;
    padding: 14px;
}

div.stButton > button:hover {
    background-color: #FFE082;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# 메인 화면
# -------------------------
if st.session_state.page == "main":

    st.markdown(
        '<div class="title">👋 안녕하세요 👋</div>',
        unsafe_allow_html=True
    )

    if st.button("나도 인사하기"):
        st.session_state.page = "success"
        st.session_state.balloons_shown = False

# -------------------------
# 축하 화면
# -------------------------
else:

    # 풍선은 한 번만 실행
    if not st.session_state.balloons_shown:
        st.balloons()
        st.session_state.balloons_shown = True

    st.markdown(
        '<div class="success">🎉 첫 웹페이지 제작을 축하해요! 🎉</div>',
        unsafe_allow_html=True
    )

    if st.button("돌아가기"):
        st.session_state.page = "main"
        st.session_state.balloons_shown = False
        st.rerun()
