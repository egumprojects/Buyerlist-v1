import streamlit as st
from backend.embeddings import embed
from backend.vector_search import load_target_data, search_similar_targets


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

   


    # Centered tool description under header
    st.markdown("""
        <div style="background-color:white; border:1px solid #ccc; border-radius:8px; padding:20px; margin: 20px auto; text-align: center; max-width: 1000px;">
            This tool allows you to input a new M&A target and receive recommended buyers from our internal deal history, based on similarity in description, industry, and past engagement.
        </div>
    """, unsafe_allow_html=True)

    # Horizontal Inputs (3 columns)
    with st.form("target_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            target_name = st.text_input("Target Company Name")
        with col2:
            target_desc = st.text_area("Target Description")
        with col3:
            target_industry = st.text_input("Industry")
        
        submitted = st.form_submit_button("Find Recommended Buyers")

    # Processing
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









