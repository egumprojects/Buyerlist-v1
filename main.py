import streamlit as st
import pandas as pd
from backend.vector_search import find_similar_buyers

st.title("Buyer Recommendation Tool")

st.sidebar.title("New Target Input")
description = st.sidebar.text_area("Target Description")
industry = st.sidebar.text_input("Industry")

if st.sidebar.button("Find Buyers"):
    buyers = find_similar_buyers(description, industry)
    st.subheader("Recommended Buyers")
    st.dataframe(buyers)
