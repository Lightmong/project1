import streamlit as st
import math
import sympy as sp

# -----------------------------
# 상태 초기화
# -----------------------------
if "expr" not in st.session_state:
    st.session_state.expr = ""

if "result" not in st.session_state:
    st.session_state.result = ""


# -----------------------------
# CSS (중앙 카드 UI)
# -----------------------------
st.markdown("""
<style>
.stApp {
    background-color: #E3F2FD;
}

.calculator {
    width: 420px;
    margin: auto;
    margin-top: 60px;
    padding: 20px;
    background: white;
    border-radius: 20px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.1);
}

.display {
    background: #222;
    color: white;
    padding: 20px;
    border-radius: 12px;
    font-size: 28px;
    text-align: right;
    min-height: 60px;
}

.btn button {
    width: 100%;
    height: 60px;
    font-size: 20px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)


# -----------------------------
# 계산 함수
# -----------------------------
def calculate(expr):
    try:
        return eval(expr)
    except:
        return "Error"


# -----------------------------
# UI 시작
# -----------------------------
st.markdown('<div class="calculator">', unsafe_allow_html=True)

# =========================
# 결과 화면 (위쪽)
# =========================
st.markdown(f"""
<div class="display">
{st.session_state.expr if st.session_state.expr else "0"}
<br>
<span style="font-size:18px; color:#4CAF50;">
{st.session_state.result}
</span>
</div>
""", unsafe_allow_html=True)

st.write("")

# =========================
# 버튼 입력 함수
# =========================
def press(val):
    st.session_state.expr += str(val)

def clear():
    st.session_state.expr = ""
    st.session_state.result = ""

def equal():
    st.session_state.result = str(calculate(st.session_state.expr))


# =========================
# 버튼 UI
# =========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button("7", on_click=press, args=("7",))
    st.button("4", on_click=press, args=("4",))
    st.button("1", on_click=press, args=("1",))
    st.button("0", on_click=press, args=("0",))

with col2:
    st.button("8", on_click=press, args=("8",))
    st.button("5", on_click=press, args=("5",))
    st.button("2", on_click=press, args=("2",))
    st.button(".", on_click=press, args=(".",))

with col3:
    st.button("9", on_click=press, args=("9",))
    st.button("6", on_click=press, args=("6",))
    st.button("3", on_click=press, args=("3",))
    st.button("=", on_click=equal)

with col4:
    st.button("+", on_click=press, args=("+",))
    st.button("-", on_click=press, args=("-"))
    st.button("*", on_click=press, args=("*",))
    st.button("/", on_click=press, args=("/"))

st.write("---")

# =========================
# 고급 연산
# =========================

col5, col6, col7 = st.columns(3)

with col5:
    st.button("log", on_click=lambda: st.session_state.update(
        result=str(math.log(float(st.session_state.expr) or 1))
    ))

with col6:
    def diff():
        x = sp.Symbol('x')
        expr = sp.sympify(st.session_state.expr)
        st.session_state.result = str(sp.diff(expr, x))

    st.button("d/dx", on_click=diff)

with col7:
    st.button("C", on_click=clear)

st.markdown('</div>', unsafe_allow_html=True)
