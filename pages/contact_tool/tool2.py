import streamlit as st

def run():
    st.header(" Contact Info Lookup")

    name = st.text_input("Name")
    company = st.text_input("Company")
    position = st.text_input("Position")

    if st.button("Find Contact Info"):
        st.write("🔍 Looking up contact info...")
        st.info("This would trigger the n8n webhook or search agent.")
