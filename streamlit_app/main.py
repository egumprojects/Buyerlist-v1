import streamlit as st
import os
import sys

# Allow import of modules from the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages import buyer_tool, contact_tool

st.set_page_config(page_title="Founders Advisors - Internal Tools", layout="wide")

# Custom CSS
st.markdown("""
<style>
    body {
        background-color: white;
    }
    .title-bar {
        background-color: #1E3A8A;  /* 🔵 Change this hex to your brand blue */
        color: white;
        padding: 30px 40px 30px 20px;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 30px;
    }
    .title-text {
        font-size: 32px;
        font-weight: bold;
        margin-left: 10px;
    }
    .home-button {
        background-color: white;
        color: #1E3A8A;
        padding: 10px 15px;
        border-radius: 8px;
        border: none;
        font-size: 20px;
        font-weight: bold;
        cursor: pointer;
    }
    .home-button:hover {
        background-color: #f0f0f0;
    }
    .description-box {
        background-color: white;
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 40px;
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

# Title with home button
st.markdown("""
<div class="title-bar">
    <button class="home-button">🏠</button>
    <div class="title-text">Founders Advisors - Internal Tools</div>
</div>
""", unsafe_allow_html=True)

# Website description input box
with st.container():
    st.markdown('<div class="description-box">', unsafe_allow_html=True)
    st.subheader("💡 Description")
    st.text_area("Enter a short description or instructions for this internal toolkit:", "Use the tools below to assist with M&A research and outreach.")
    st.markdown('</div>', unsafe_allow_html=True)

# Tool 1 – Buyer Recommendation Tool
st.markdown('<div class="tool-row">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 4])
with col1:
    if st.button("Buyer Tool", key="buyer_button"):
        buyer_tool.run()
with col2:
    st.markdown("###  Buyer Recommendation")
    st.write("Input a new M&A target and receive suggested buyers based on internal deal history.")
st.markdown('</div>', unsafe_allow_html=True)

# Tool 2 – Contact Info Lookup Tool
st.markdown('<div class="tool-row">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 4])
with col1:
    if st.button("Contact Tool", key="contact_button"):
        contact_tool.run()
with col2:
    st.markdown("###  Contact Info Lookup")
    st.write("Find contact information (like emails) using the person’s name, title, and company.")
st.markdown('</div>', unsafe_allow_html=True)

