import streamlit as st

# Page configuration
st.set_page_config(
    page_title="About Me",
    page_icon="👤",
    layout="wide"
)

# Styling
st.markdown("""
<style>
    .title {
        font-size: 28px;
        font-weight: 700;
        margin-bottom: 20px;
    }

    .about-box {
        background-color: rgba(250, 250, 250, 0.05);
        padding: 24px;
        border-radius: 12px;
        margin-bottom: 30px;
        border: 1px solid rgba(255,255,255,0.08);
    }

    .about-text {
        font-size: 16px;
        line-height: 1.7;
        color: inherit;
    }

    .contact-box {
        font-size: 16px;
        line-height: 1.7;
        color: inherit;
        background-color: rgba(250, 250, 250, 0.05);
        padding: 20px;
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.08);
    }

    .contact-label {
        font-weight: 600;
        width: 150px;
        display: inline-block;
    }

    .contact-link {
        color: #3399ff;
        text-decoration: none;
    }

    .contact-link:hover {
        text-decoration: underline;
    }

    .inline-links {
        margin-top: 10px;
    }

    .inline-links a {
        margin-right: 25px;
        color: #3399ff;
        text-decoration: none;
        font-weight: 500;
    }

    .inline-links a:hover {
        text-decoration: underline;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">👤 About Me</div>', unsafe_allow_html=True)

# About Box
st.markdown("""
<div class="about-box">
    <div class="about-text">
        Hi! I'm <strong>Jovid Jumaev</strong>, a rising senior at Furman University majoring in Computer Science.  
        I'm from Khorog, Tajikistan 🇹🇯 and I’ve been a loyal FC Barcelona fan for over 14 years 🔴🔵.
        <br><br>
        This dashboard combines my love for football with my passion for data. I love building interactive tools that offer insights into the game beyond what you see on the pitch.
    </div>
</div>
""", unsafe_allow_html=True)

# Contact Section
st.markdown('<div class="title">📬 Get in Touch</div>', unsafe_allow_html=True)

st.markdown("""
<div class="contact-box">
    <div><span class="contact-label">Personal Portfolio:</span>
        <a class="contact-link" href="https://jovidjumaev.com" target="_blank">jovidjumaev.com</a>
    </div>
    <div><span class="contact-label">Email:</span>
        <a class="contact-link" href="mailto:jovid.jumaev01@gmail.com">jovid.jumaev01@gmail.com</a>
    </div>
    <div class="inline-links">
        <a href="https://linkedin.com/in/jovid-jumaev-967751291/" target="_blank">LinkedIn</a>
        <a href="https://github.com/jovidjumaev" target="_blank">GitHub</a>
    </div>
</div>
""", unsafe_allow_html=True)
