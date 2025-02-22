import streamlit as st

def show_ui_page():
    st.markdown("""
        <style>
            .title {
                text-align: center;
                font-size: 36px;
                font-weight: bold;
                color: gold;
            }
            .container {
                text-align: center;
                padding: 20px;
                background-color: #1b1b1b;
                border-radius: 10px;
            }
            .button {
                background-color: gold;
                color: black;
                font-size: 18px;
                border-radius: 8px;
                padding: 10px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='title'>🔥 KingBoss Cigars UI 🔥</div>", unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1534113421730-78b4a69d60d3", caption="Luxury Cigar Lounge", use_column_width=True)

    st.markdown("<div class='container'><h2>🚬 Featured Cigar Deals</h2></div>", unsafe_allow_html=True)
    
    if st.button("Explore More", key="explore_button"):
        st.success("More features coming soon!")
