import streamlit as st
from pages.buyer_tool import tool1

# Initialize the session state on first load
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

# Top nav bar / header
st.markdown(
    """
    <div style='background-color:#3E5064;padding:20px;border-radius:8px;display:flex;align-items:center;justify-content:space-between;'>
        <div style='display:flex;align-items:center;gap:10px;'>
            <a href="/" onclick="window.location.reload();" style='text-decoration:none;'>
                <span style='font-size:24px;color:white;'>🏠</span>
            </a>
            <h1 style='color:white;margin:0;font-size:24px;'>Founders Advisors – Internal Tools</h1>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "<div style='background-color:#fff;border:1px solid #ccc;padding:15px;border-radius:6px;margin-top:15px;text-align:center;'>"
    "This internal toolkit provides deal professionals with intelligent tools to support buyer research and outreach. "
    "Use the buttons below to access each tool."
    "</div>",
    unsafe_allow_html=True
)

# Home Page UI
if st.session_state.current_page == "home":
    col1, col2 = st.columns([1, 4])

    with col1:
        if st.button("Buyer Tool"):
            st.session_state.current_page = "buyer_tool"

    with col2:
        st.markdown("#### Buyer Recommendation")
        st.caption("Input a new M&A target and receive suggested buyers based on past outreach and internal deal history.")

# Buyer Tool UI
elif st.session_state.current_page == "buyer_tool":
    tool1.run()










