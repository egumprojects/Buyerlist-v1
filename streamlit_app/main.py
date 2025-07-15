import streamlit as st
import os
import sys

# Add parent directory to path so we can import tool modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.buyer_tool import tool1
from pages.contact_tool import tool2

# Streamlit page setup
st.set_page_config(page_title="Founders Advisors - Internal Tools", layout="wide")

# Custom styles and full title bar with Home button
st.markdown("""
<style>
    body {
        background-color: white;
    }
    .title-bar {
        background-color: #3E5064;
        color: white;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 20px 30px;
        border-radius: 8px;
        margin-bottom: 20px;
    }
    .title-left {
        display: flex;
        align-items: center;
        gap: 20px;
    }
    .home-link {
        background-color: white;
        color: #3E5064;
        font-size: 22px;
        padding: 10px 16px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
    }
    .home-link:hover {
        background-color: #f0f0f0;
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

<div class="title-bar">
    <div class="title-left">
        <a class="home-link" href="/" target="_self">🏠</a>
        <div style="font-size: 28px; font-weight: bold;">Founders Advisors – Internal Tools</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Static description box
st.markdown("""
<div class="description-box">
This internal toolkit provides deal professionals with intelligent tools to support buyer research and outreach. Use the options below to navigate between modules.
</div>
""", unsafe_allow_html=True)

# Buyer Recommendation Tool section
st.markdown('<div class="tool-row">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 4])
with col1:
    if st.button("Buyer Tool", key="buyer_button"):
        tool1.run()
with col2:
    st.markdown("###  Buyer Recommendation")
    st.write("Input a new M&A target and receive suggested buyers based on past outreach and internal deal history.")
st.markdown('</div>', unsafe_allow_html=True)

# Contact Lookup Tool section
st.markdown('<div class="tool-row">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 4])
with col1:
    if st.button("Contact Tool", key="contact_button"):
        tool2.run()
with col2:
    st.markdown("###  Contact Info Lookup")
    st.write("Find decision-maker contact details using the person’s name, title, and company across web and internal sources.")
st.markdown('</div>', unsafe_allow_html=True)






