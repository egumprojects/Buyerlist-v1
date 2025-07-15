import streamlit as st
import os
import sys

# Make sure Python can find your 'pages' folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages import buyer_tool, contact_tool

# Streamlit page config
st.set_page_config(page_title="Founders Advisors - Internal Tools", layout="wide")

# Custom CSS styling
st.markdown("""
<style>
    body {
        background-color: white;
    }
    .title-box {
        background-color: #3E5064;  
        color: white;
        text-align: center;
        padding: 30px 10px;
        border-radius: 8px;
        font-size: 32px;
        font-weight: bold;
        margin-bottom: 50px;
    }
    .tool-row {
        display: flex;
        align-items: center;
        gap: 20px;
        margin-bottom: 30px;
    }
    .tool-button {
        background-color: #e2e8f0;
        color: black;
        padding: 15px 25px;
        border: none;
        border-radius: 10px;
        font-size: 16px;
        font-weight: 500;
        cursor: pointer;
        min-width: 200px;
        text-align: center;
    }
    .tool-button:hover {
        background-color: #cbd5e1;
    }
</style>
""", unsafe_allow_html=True)

# Title section
st.markdown('<div class="title-box">Founders Advisors - Internal Tools</div>', unsafe_allow_html=True)

# Tool 1 – Buyer Recommendation Tool
st.markdown('<div class="tool-row">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 4])
with col1:
    if st.button("Buyer Tool", key="buyer_button"):
        buyer_tool.run()
with col2:
    st.markdown("### Buyer Recommendation")
    st.write("Input a new M&A target and receive suggested buyers based on internal deal history.")
st.markdown('</div>', unsafe_allow_html=True)

# Tool 2 – Contact Info Lookup Tool
st.markdown('<div class="tool-row">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 4])
with col1:
    if st.button("Contact Tool", key="contact_button"):
        contact_tool.run()
with col2:
    st.markdown("### Contact Info Lookup")
    st.write("Find contact information (like emails) using the person’s name, title, and company.")
st.markdown('</div>', unsafe_allow_html=True)


