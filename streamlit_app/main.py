import streamlit as st

# Route control via session_state
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "home"

# Navigation actions
def go_home():
    st.session_state["current_page"] = "home"
    st.experimental_rerun()

def go_buyer_tool():
    st.session_state["current_page"] = "buyer_tool"
    st.experimental_rerun()

def go_contact_tool():
    st.session_state["current_page"] = "contact_tool"
    st.experimental_rerun()

# Top Header (Shared)
def render_header(title_text):
    st.markdown(f"""
        <div style="background-color:#3E5064; padding: 20px 30px; border-radius: 8px; display: flex; align-items: center; justify-content: space-between;">
            <button onclick="window.location.reload();" style="background-color: white; color: #3E5064; padding: 10px 15px; border: none; border-radius: 8px; font-size: 20px; font-weight: bold; cursor: pointer;">
                🏠
            </button>
            <h1 style="color: white; margin: 0 auto; font-size: 26px;">{title_text}</h1>
            <div></div>
        </div>
    """, unsafe_allow_html=True)

# Home Page UI
def show_homepage_ui():
    render_header("Founders Advisors – Internal Tools")

    st.markdown("""
        <div style="background-color:white; border:1px solid #ccc; border-radius:8px; padding:20px; margin-top:20px; text-align:center;">
            This internal toolkit provides deal professionals with intelligent tools to support buyer research and outreach. Use the buttons below to navigate between modules.
        </div>
    """, unsafe_allow_html=True)

    # Buyer Tool Block
    st.markdown('<div style="display: flex; align-items: center; margin-top: 30px;">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("Buyer Tool"):
            go_buyer_tool()
    with col2:
        st.subheader("🧠 Buyer Recommendation")
        st.caption("Input a new M&A target and receive suggested buyers based on past outreach and internal deal history.")
    st.markdown('</div>', unsafe_allow_html=True)

    # Contact Tool Block
    st.markdown('<div style="display: flex; align-items: center; margin-top: 20px;">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("Contact Tool"):
            go_contact_tool()
    with col2:
        st.subheader("📬 Contact Info Lookup")
        st.caption("Find decision-maker contact details using name, title, and company.")
    st.markdown('</div>', unsafe_allow_html=True)

# Page Routing
if st.session_state["current_page"] == "buyer_tool":
    from pages.buyer_tool import tool1
    tool1.run()

elif st.session_state["current_page"] == "contact_tool":
    from pages.contact_tool import tool2
    tool2.run()

else:
    show_homepage_ui()










