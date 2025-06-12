import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="La Liga Dashboard",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTitle {
        color: #1E3A8A;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("La Liga Dashboard")

st.markdown("""
    This project was created out of pure passion for football and data analysis. 
    It's a personal journey to improve my skills in data visualization and analytics.
    
    I promise to keep this dashboard updated after each season ends, sharing fresh insights 
    and statistics as they become available. This is a genuine effort to contribute to the 
    football analytics community while growing my own skills.
""")

# Data Source Section
st.markdown("""
    ### 📊 Data Source
    This dashboard uses comprehensive football statistics from [FBref](https://fbref.com/), providing detailed insights into match results, 
    team performance metrics, player statistics, and advanced analytics including Expected Goals (xG), Progressive Passes, and more.
""")

# Feature sections
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📊 2023 Season")
    st.markdown("Analyze complete statistics from the 2023 season, including team performance, player stats, and match results.")

with col2:
    st.markdown("### ⚡ 2024 Season")
    st.markdown("Stay updated with real-time data from the current season, including live standings and recent match results.")

with col3:
    st.markdown("### 👨‍💻 About")
    st.markdown("Learn more about the creator of this dashboard and the technologies used to build it.")

# Navigation guide
st.markdown("""
    ### Navigation Guide
    
    Use the sidebar to explore:
    - **LaLiga 2023**: Complete 2023 season statistics
    - **LaLiga 2024**: Current season data
    - **About**: More about the author
""")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ for football analytics enthusiasts") 