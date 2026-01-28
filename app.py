import streamlit as st

st.set_page_config(page_title="OneClick Factory", layout="centered")

st.title("🎬 OneClick Factory")
st.write("대본만 넣고 버튼 한 번 누르면 끝")

script = st.text_area("대본 입력", height=150)

if st.button("🎬 딸깍! 영상 만들기"):
    if script.strip() == "":
        st.warning("대본을 입력하세요")
    else:
        st.success("✅ 딸깍 완료 (다음 단계에서 영상 자동화 연결)")
