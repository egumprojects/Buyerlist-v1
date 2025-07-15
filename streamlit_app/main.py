import streamlit as st
import os
import sys

# Make sure Python can find your 'pages' folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages import buyer_tool, contact_tool

# Page config
st.set_page_config(page_title="Founders Advisors - Internal Tools", layout="centered")

# Custom CSS
st.markdown("""
<style>
    .title-box {
        background-color: #1E3A8A;  /* 🔵 Change this hex color to match your brand */
        color: white;
        text-align: center;
        padding: 30px 10px;
        border-radius: 8px;
        font-size: 32px;
        font-weight: bold;
        margin-bottom: 40px;
    }
    .tool-box {
        background-color: #f8f9fa;
        border: 1px solid #e1e1e1;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 25px;
    }
    .tool-button {
        background-color: #e2e8f0;
        color: #000;
        padding: 12px 25px;
        border: none;
        border-radius: 8px;
        font-size: 16px;
        font-weight: 500;
        margin-top: 10px;
    }
    .tool-button:hover {
        background-color: #cbd5e1;
    }
</style>
""", unsafe_allow_html=True)

# Main Title
st.markdown('<div class="title-box">Founders Advisors - Internal Tools</div>', unsafe_allow_html=True)

# Sidebar Menu (for redundancy, but not used on this page)
st.sidebar.title("Navigation")

# Tool 1 – Buyer Recommendation
st.markdown('<div class="tool-box">', unsafe_allow_html=True)
st.subheader("🧠 Buyer Recommendation Tool")
st.write("Input a new M&A target and get buyer suggestions based on your internal deal history.")
if st.button("Go to Buyer Tool"):
    buyer_tool.run()
st.markdown('</div>', unsafe_allow_html=True)

# Tool 2 – Contact Info Lookup
st.markdown('<div class="tool-box">', unsafe_allow_html=True)
st.subheader("📬 Contact Info Lookup Tool")
st.write("Find contact info like emails using name, company, and role.")
if st.button("Go to Contact Tool"):
    contact_tool.run()
st.markdown('</div>', unsafe_allow_html=True)
