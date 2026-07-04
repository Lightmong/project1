import streamlit as st

st.set_page_config(
    page_title="첫 웹페이지",
    page_icon="👋",
    layout="centered"
)

# 상태 초기화
if "clicked" not in st.session_state:
    st.session_state.clicked = False

# CSS
st.markdown("""
<style>
.stApp{
    background-color:#121212;
    color:white;
}

.main-title{
    text-align:center;
    font-size:60px;
    font-weight:bold;
    margin-top:120px;
    margin-bottom:50px;
}

div.stButton > button{
    width:100%;
    background-color:#FFD54F;
    color:black;
    font-size:22px;
    font-weight:bold;
    border:none;
    border-radius:12px;
    padding:14px;
}

div.stButton > button:hover{
    background-color:#FFE082;
}

.success-msg{
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:#FFD54F;
    margin-top:120px;
}
</style>
""", unsafe_allow_html=True)


# 메인 화면
if not st.session_state.clicked:

    st.markdown(
        '<div class="main-title">👋 안녕하세요 👋</div>',
        unsafe_allow_html=True
    )

    if st.button("나도 인사하기"):
        st.session_state.clicked = True
        st.balloons()
        st.rerun()

# 결과 화면
else:

    st.markdown(
        '<div class="success-msg">🎉 첫 웹페이지 제작을 축하해요! 🎉</div>',
        unsafe_allow_html=True
    )

    if st.button("돌아가기"):
        st.session_state.clicked = False
        st.rerun()
