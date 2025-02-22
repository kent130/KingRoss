import streamlit as st

st.set_page_config(page_title="KingBoss Cigars", layout="wide")

st.markdown("""
    <style>
        body {
            background-color: #1b1b1b;
            color: white;
            font-family: Arial, sans-serif;
        }
        .title {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            color: gold;
        }
        .search-box {
            text-align: center;
            padding: 20px;
            border-radius: 10px;
            background-color: #262626;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🔎 KingBoss Cigars Price Finder</div>", unsafe_allow_html=True)

cigar_name = st.text_input("Enter cigar name:", key="search_box")
if st.button("Find Best Prices"):
    st.success(f"Searching for {cigar_name}...")
