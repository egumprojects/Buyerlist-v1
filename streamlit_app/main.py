import sys
import os
import streamlit as st
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages import buyer_tool, contact_tool



st.set_page_config(page_title="M&A Toolkit", layout="wide")
st.title("🔎 M&A Research Toolkit")

# Sidebar menu
st.sidebar.title("Menu")
selected_tool = st.sidebar.selectbox("Choose a tool", [
    "Buyer Recommendation",
    "Contact Info Lookup"
])

# Route to selected tool
if selected_tool == "Buyer Recommendation":
    buyer_tool.run()

elif selected_tool == "Contact Info Lookup":
    contact_tool.run()
