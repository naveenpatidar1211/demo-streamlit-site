import streamlit as st

# Page config for this specific page
st.set_page_config(page_title="Home", page_icon="🏠")

# Header banner
st.markdown("# 🏠 Homepage")
st.markdown("### *Your Gateway to Awesome Content*")
st.markdown("---")

# Banner text content
st.markdown("""
Welcome to our demo site! This is a simple multi-page application built with Streamlit, showcasing how easy it is to create interactive web apps with Python.

**Why Streamlit?**
- **Rapid Development**: Write apps in pure Python.
- **Interactive Widgets**: Add buttons, sliders, and charts effortlessly.
- **Deployment Ready**: Host on Streamlit Cloud or anywhere.

Explore the pages in the sidebar to learn more. Let's get started!
""")

# Add a fun element: a progress bar as a placeholder
st.markdown("### Quick Start Progress")
progress = st.progress(0)
for i in range(100):
    progress.progress(i + 1)
st.success("Ready to dive in? Check out the About or Blog page!")

st.markdown("---")
st.markdown("*Footer: Built with ❤️ using Streamlit*")