import streamlit as st
import os
import sys

# Allow import of modules from the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages import buyer_tool, contact_tool

st.set_page_config(page_title="Founders Advisors - Internal Tools", layout="wide")

# Custom CSS for professional layout
st.markdown("""
<style>
    body {
        background-color: white;
    }
    .title-bar {
        background-color: #3E5064;  /* Updated brand color */
        color: white;
        text-align: center;
        padding: 30px 20px;
        border-radius: 8px;
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .description-box {
        background-color: white;
        border: 1px solid #ccc;
        border-radius: 8px;
        padding: 20px;
        font-size: 16px;
        margin-bottom: 40px;
        text-align: center;
        color: #333;
    }
    .tool-row {
        display: flex;
        align-items: center;
        gap: 20px;
        margin-bottom: 30px;
        padding: 10px 0;
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

# Title header
st.markdown('<div class="title-bar">Founders Advisors – Internal Tools</div>', unsafe_allow_html=True)

# Static description box
st.markdown("""
<div class="description-box">
This internal toolkit provides deal professionals with intelligent tools to support buyer research and outreach. Use the options below to navigate between modules.
</div>
""", unsafe_allow_html=True)

# Tool 1 – Buyer Recommendation Tool
st.markdown('<div class="tool-row">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 4])
with col1:
    if st.button("Buyer Tool", key="buyer_button"):
        buyer_tool.run()
with col2:
    st.markdown("### Buyer Recommendation")
    st.write("Input a new M&A target and receive suggested buyers based on past outreach and internal deal history.")
st.markdown('</div>', unsafe_allow_html=True)

# Tool 2 – Contact Info Lookup Tool
st.markdown('<div class="tool-row">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 4])
with col1:
    if st.button("Contact Tool", key="contact_button"):
        contact_tool.run()
with col2:
    st.markdown("###  Contact Info Lookup")
    st.write("Find decision-maker contact details using their name, title, and company across web and internal sources.")
st.markdown('</div>', unsafe_allow_html=True)


