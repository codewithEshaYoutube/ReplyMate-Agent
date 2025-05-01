import streamlit as st

# Page config
st.set_page_config(page_title="ReplyMate AI - WhatsApp ChatBot", layout="wide")

# Sidebar-style header (just styled info, not actual navigation)
with st.sidebar:
    st.markdown("""
    <div style="text-align: center;">
        <img src="https://img.icons8.com/ios-filled/100/26e07f/whatsapp--v1.png" width="60"/>
        <h3 style="font-family: Arial; color: #25D366;">ReplyMate AI</h3>
        <p style="font-size: 14px;">WhatsApp Smart ChatBot for Secure Replies & Fraud Detection</p>
        <hr>
    </div>
    """, unsafe_allow_html=True)

# Main Title
st.markdown("""
<h2 style='font-family:Orbitron, sans-serif; color:#004080;'>🤖 Chat Interface</h2>
<p style='font-size:16px;'>Ask anything related to WhatsApp fraud detection, secure replies, or support.</p>
""", unsafe_allow_html=True)

# Embed Chatbot (smaller height for better fit)
st.components.v1.html("""
    <iframe 
        src="https://www.chatbase.co/chatbot-iframe/tlV_gt9CoGajJQXAsMg3i" 
        width="100%" 
        style="height: 600px; border: none; border-radius: 12px;" 
        frameborder="0">
    </iframe>
""", height=620)

