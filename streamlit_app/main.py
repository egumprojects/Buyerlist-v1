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

#  Page UI Navigation
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "home"

if st.session_state["current_page"] == "home":
    from pages import home
    home.run()

elif st.session_state["current_page"] == "buyer_tool":
    from pages.buyer_tool import tool1
    tool1.run()

elif st.session_state["current_page"] == "contact_tool":
    from pages.contact_tool import tool2
    tool2.run()











