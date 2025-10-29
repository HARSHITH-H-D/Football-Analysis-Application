import streamlit as st
st.set_page_config(
    page_title="Football Analysis Hub",
    layout="wide",
    initial_sidebar_state="expanded"
)
import euro_shot_map
import web_app

# Set page configuration


# Background GIF & Overlay
st.markdown(
    """
    <style>
    .stApp {
        background: url("https://github.com/HARSHITH-H-D/HARSHITH-H-D.github.io/blob/main/Untitled design (1).gif") no-repeat center center fixed;
        background-size: cover;
    }
    .background-overlay {
        background-color: rgba(0, 0, 0, 0.5);
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
    }
    </style>
    <div class="background-overlay"></div>
    """,
    unsafe_allow_html=True
)

# Main Heading Section
with st.container():
    st.title("⚽ Football Analysis Hub")
    st.subheader("Insights | Tactics | Tracking | Strategy")
    st.write("Welcome to the future of football analytics.")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Player Tracking", "Formations & Tactics", "Match Stats", "Heatmaps", "AI Predictions", "About"])

# Routing Logic
if page == "Home":
    st.markdown("""
        Welcome to the **Football Analysis Hub** — your all-in-one platform for visualizing and understanding football like never before.

        **Features:**
        - Real-time **Player Tracking**
        - Team **Formations and Tactical Analysis**
        - Match-wise **Statistical Insights**
    """)

elif page == "Player Tracking":
    web_app.app()

elif page == "Formations & Tactics":
    web_app.app()

elif page == "Euro 2024 Shot Maps":
    st.write("This page includes all the Shots taken by the players from the particular position in the pitch.")
    euro_shot_map.app()

elif page == "Heatmaps":
    st.write("Heatmaps section coming soon!")  # Placeholder

elif page == "AI Predictions":
    st.write("AI Prediction models coming soon!")  # Placeholder

elif page == "About":
    st.header("About This Project")
    st.markdown("""
        Created by SUI... Team, this project aims to bridge football with technology.
        Using computer vision, machine learning, and data science — we bring the pitch to your screen in a whole new way.
    """)

# Footer
st.markdown("---")
st.caption("Powered by Streamlit | Developed with passion for football.")
