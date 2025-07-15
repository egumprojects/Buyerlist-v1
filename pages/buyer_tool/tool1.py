import streamlit as st
import pandas as pd
import faiss
from backend.embeddings import embed
from backend.vector_search import load_target_data, search_similar_targets

def run():
    st.markdown("<h1 style='color:#3E5064;'>🧠 Buyer Recommendation Tool</h1>", unsafe_allow_html=True)

    st.markdown('<div style="background-color:white; border:1px solid #ccc; border-radius:8px; padding:20px; margin-bottom:30px;">'
                'Use this tool to input a new M&A target and receive recommended buyers based on similarity to past internal deals. '
                'Recommendations are based on engagement history, industry, and textual similarity.</div>', unsafe_allow_html=True)

    with st.form("target_form"):
        target_name = st.text_input("Target Company Name")
        target_desc = st.text_area("Target Description")
        target_industry = st.text_input("Industry")
        submitted = st.form_submit_button("Find Recommended Buyers")

    if submitted and target_desc:
        query_text = f"{target_name}. {target_desc}. Industry: {target_industry}"
        query_vec = embed([query_text])

        targets_df, embeddings, deal_to_buyers, buyer_meta = load_target_data()
        top_targets = search_similar_targets(query_vec, targets_df, embeddings)

        buyer_scores = {}
        for deal_id in top_targets["deal_id"]:
            for buyer in deal_to_buyers.get(deal_id, []):
                buyer_scores[buyer] = buyer_scores.get(buyer, 0) + 1

        if buyer_scores:
            sorted_buyers = sorted(buyer_scores.items(), key=lambda x: -x[1])
            st.subheader("🔍 Top Recommended Buyers")
            for buyer, score in sorted_buyers[:10]:
                description = buyer_meta.get(buyer, "No profile available")
                st.markdown(f"""
                    <div style="border:1px solid #ddd; border-radius:8px; padding:15px; margin-bottom:15px; background-color:#f9f9f9;">
                        <strong>{buyer}</strong><br>
                        <em>Engagement Score: {score}</em><br>
                        <span style="font-size:14px; color:#444;">{description}</span>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("No matching buyers found.")






