import streamlit as st
import math

# -------------------------
# 상태
# -------------------------
if "expr" not in st.session_state:
    st.session_state.expr = ""

if "result" not in st.session_state:
    st.session_state.result = ""


# -------------------------
# 🔥 안전 + 괄호 자동 보정 계산기
# -------------------------
def safe_eval(expr):
    try:
        expr = expr.replace("^", "**")

        # -------------------------
        # 괄호 자동 보정
        # -------------------------
        open_count = expr.count("(")
        close_count = expr.count(")")

        if open_count > close_count:
            expr += ")" * (open_count - close_count)

        # 허용 함수
        allowed = {
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "log": math.log10,
            "ln": math.log,
            "sqrt": math.sqrt,
            "pi": math.pi,
            "e": math.e,
            "abs": abs
        }

        return eval(expr, {"__builtins__": None}, allowed)

    except:
        return "Error"


# -------------------------
# UI 스타일
# -------------------------
st.markdown("""
<style>
.stApp {
    background-color: #E3F2FD;
}

.calculator {
    width: 430px;
    margin: auto;
    margin-top: 40px;
    padding: 20px;
    background: white;
    border-radius: 20px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.15);
}

.display {
    background: #111;
    color: #00ff99;
    padding: 20px;
    font-size: 28px;
    border-radius: 12px;
    text-align: right;
    min-height: 80px;
    word-wrap: break-word;
}

button {
    height: 55px !important;
    font-size: 18px !important;
    border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)


# -------------------------
# 기능 함수
# -------------------------
def press(val):
    st.session_state.expr += str(val)

def clear():
    st.session_state.expr = ""
    st.session_state.result = ""

def equal():
    st.session_state.result = str(safe_eval(st.session_state.expr))


# -------------------------
# UI 시작
# -------------------------
st.markdown('<div class="calculator">', unsafe_allow_html=True)

# 디스플레이
st.markdown(f"""
<div class="display">
{st.session_state.expr if st.session_state.expr else "0"}
<br>
<span style="font-size:20px;">
{st.session_state.result}
</span>
</div>
""", unsafe_allow_html=True)

st.write("")

# -------------------------
# 숫자 / 연산
# -------------------------
row1 = st.columns(4)
row2 = st.columns(4)
row3 = st.columns(4)
row4 = st.columns(4)

with row1[0]: st.button("7", on_click=press, args=("7",))
with row1[1]: st.button("8", on_click=press, args=("8",))
with row1[2]: st.button("9", on_click=press, args=("9",))
with row1[3]: st.button("/", on_click=press, args=("/"))

with row2[0]: st.button("4", on_click=press, args=("4",))
with row2[1]: st.button("5", on_click=press, args=("5",))
with row2[2]: st.button("6", on_click=press, args=("6",))
with row2[3]: st.button("*", on_click=press, args=("*",))

with row3[0]: st.button("1", on_click=press, args=("1",))
with row3[1]: st.button("2", on_click=press, args=("2",))
with row3[2]: st.button("3", on_click=press, args=("3",))
with row3[3]: st.button("-", on_click=press, args=("-"))

with row4[0]: st.button("0", on_click=press, args=("0",))
with row4[1]: st.button(".", on_click=press, args=("."))
with row4[2]: st.button("=", on_click=equal)
with row4[3]: st.button("+", on_click=press, args=("+",))

st.write("---")

# -------------------------
# 공학 기능
# -------------------------
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.button("sin", on_click=press, args=("sin(",))

with c2:
    st.button("cos", on_click=press, args=("cos(",))

with c3:
    st.button("tan", on_click=press, args=("tan(",))

with c4:
    st.button("√", on_click=press, args=("sqrt(",))

c5, c6, c7, c8 = st.columns(4)

with c5:
    st.button("log", on_click=press, args=("log(",))

with c6:
    st.button("ln", on_click=press, args=("ln(",))

with c7:
    st.button("π", on_click=press, args=("pi",))

with c8:
    st.button("e", on_click=press, args=("e",))

st.write("---")

st.button("C (초기화)", on_click=clear)

st.markdown('</div>', unsafe_allow_html=True)
