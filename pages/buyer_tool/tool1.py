import pandas as pd
import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from backend.vector_search import recommend_buyers

def run(go_home_callback):
    # Header
    st.markdown("""
        <div style="background-color:#3E5064; padding: 20px 30px; border-radius: 8px; display: flex; align-items: center; justify-content: space-between;">
            <button onclick="window.location.href='/'" style="font-size: 20px; background: none; border: none; color: white; cursor: pointer;">🏠</button>
            <h1 style="color: white; margin: 0 auto;">Buyer List Tool</h1>
            <div></div>
        </div>
    """, unsafe_allow_html=True)

    # Manual Home Button fallback
    if st.button("Back to Home"):
        go_home_callback()

    # Tool description box
    st.markdown("""
        <div style="background-color:white; border:1px solid #ccc; border-radius:8px; padding:20px; margin: 20px auto; text-align: center; max-width: 1000px;">
            This tool allows you to input a new M&A target and receive recommended buyers from our internal deal history, based on similarity in description, industry, and past engagement.
        </div>
    """, unsafe_allow_html=True)

    # Form input section
    with st.form("target_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            target_name = st.text_input("Target Company Name")
        with col2:
            target_desc = st.text_area("Target Description")
        with col3:
            target_industry = st.text_input("Industry")
        
        submitted = st.form_submit_button("Find Recommended Buyers")

    # Processing outside the form
    if submitted and target_desc:
        query_text = f"{target_name}. {target_desc}. Industry: {target_industry}"
        top_buyers = recommend_buyers(query_text)

        if top_buyers:
            st.subheader("📋 Recommended Buyer List")
            df = pd.DataFrame(top_buyers)[["buyer_name", "score", "description"]]
            df.columns = ["Buyer Name", "Engagement Score", "Description"]
            st.dataframe(df, use_container_width=True)

            csv = df.to_csv(index=False)
            st.download_button("📥 Download as CSV", csv, "recommended_buyers.csv", "text/csv")
        else:
            st.warning("No recommended buyers found.")










