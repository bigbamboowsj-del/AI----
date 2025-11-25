import streamlit as st

st.set_page_config(page_title="AIみんはや", layout="wide")


# -----------------------------
# カード UI（背景・丸角・余白付き）
# -----------------------------
def card(text, bg="#f5f6ff", font_size="18px", padding="0.8rem"):
    st.markdown(
        f"""
        <div style="
            background-color:{bg};
            border-radius:12px;
            padding:{padding};
            font-size:{font_size};
            text-align:center;
            margin-bottom:0.6rem;
        ">
            {text}
        </div>
        """,
        unsafe_allow_html=True,
    )


# -----------------------------
# 初期化（session_state）
# -----------------------------
if "game_started" not in st.session_state:
    st.session_state.game_started = False

if "selected_answer" not in st.session_state:
    st.session_state.selected_answer = None

if "show_tips" not in st.session_state:
    st.session_state.show_tips = False

if "final_answer" not in st.session_state:
    st.session_state.final_answer = None


# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.write("### sidebar")
    card("難易度を設定しよう", bg="#eef6ff")

    tab1, tab2, tab3 = st.tabs(["正解率：低", "正解率：中", "正解率：高"])
    with tab1:
        st.radio("正解率（50%以下）", ["選択"], index=0)

    with tab2:
        st.radio("正解率（50〜80%）", ["選択"], index=0)

    with tab3:
        st.radio("正解率（80%以上）", ["選択"], index=0)

    st.markdown(
        """
        <div style="
            position: fixed;
            bottom: 20px;
            left: 20px;
            font-size: 28px;
        ">⚙️</div>
        """,
        unsafe_allow_html=True
    )


# -----------------------------
# Main UI
# -----------------------------

# ---- タイトル行（Title + New game） ----
title_col, newgame_col = st.columns([6, 1])

with title_col:
    card("AIみんはや", bg="#e9f0ff", font_size="32px", padding="1rem")

with newgame_col:
    if st.button("New game!", use_container_width=True):
        st.session_state.game_started = True
        st.session_state.selected_answer = None
        st.session_state.show_tips = False
        st.session_state.final_answer = None


# ---- サブタイトル & 説明 ----
card("〜難易度に応じた4択問題に挑戦！！〜", font_size="20px")
card(
    "ヒントが欲しい場合は「Tips」を押してね！<br>"
    "新しい問題に挑戦したいときは「New game」を押してね！",
    font_size="15px"
)


# ここから下は New game を押した後だけ表示
if st.session_state.game_started:

    # ---- Q1 + 問題文 ----
    q_col, question_col = st.columns([1, 6])

    with q_col:
        card("Q1", bg="#f0f7ff", font_size="20px", padding="0.6rem")

    with question_col:
        card("この動物の名前はなんでしょう？？", font_size="20px", padding="0.8rem")

    st.write("")

    # ---- 4択ボタン ----
    colA, colB = st.columns(2)
    colC, colD = st.columns(2)

    with colA:
        if st.button("A. アルパカ", use_container_width=True):
            st.session_state.selected_answer = "A"

    with colB:
        if st.button("B. ラマ", use_container_width=True):
            st.session_state.selected_answer = "B"

    with colC:
        if st.button("C. ヒツジ", use_container_width=True):
            st.session_state.selected_answer = "C"

    with colD:
        if st.button("D. ヤギ", use_container_width=True):
            st.session_state.selected_answer = "D"

    st.markdown("<hr>", unsafe_allow_html=True)

    # ---- Tips ボタン ----
    tips_col, final_col = st.columns([1.2, 3])

    with tips_col:
        if st.button("Tips", use_container_width=True):
            st.session_state.show_tips = True

    with final_col:
        if st.button("Final Answer", use_container_width=True):
            st.session_state.final_answer = st.session_state.selected_answer

    # ---- Tips 表示 ----
    if st.session_state.show_tips:
        card("ヒント：首の長さが特徴だよ！", bg="#fff9e6")

    # ---- Final Answer 表示 ----
    if st.session_state.final_answer:
        card(f"あなたの回答：{st.session_state.final_answer}", bg="#eef9ff")

        # 正解例
        card("正解：A. アルパカ", bg="#e0ffe7")

        # 解説
        card("解説：アルパカは南米原産のラクダ科の動物です。", bg="#f7f7ff")
