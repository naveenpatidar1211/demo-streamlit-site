import streamlit as st
from datetime import datetime

# Page config
st.set_page_config(page_title="Blog", page_icon="📝")

# Header
st.markdown("# 📝 Blog Posts")
st.markdown("### *Latest Insights and Tips*")
st.markdown("---")

# Sample blog post list (you can expand this with a DataFrame or database)
blog_posts = [
    {
        "title": "Getting Started with Streamlit: A Beginner's Guide",
        "excerpt": "Learn the basics of building your first app in under 30 minutes. From installation to deployment, we've got you covered!",
        "date": "2025-11-15",
        "read_more": "Dive deeper into widgets and layouts."
    },
    {
        "title": "Top 5 Streamlit Extensions for Data Viz Pros",
        "excerpt": "Enhance your dashboards with these must-have libraries. Includes code snippets and real-world examples.",
        "date": "2025-11-10",
        "read_more": "Explore Altair, Plotly, and more."
    },
    {
        "title": "Why Multi-Page Apps Are the Future of Prototyping",
        "excerpt": "Say goodbye to single-file chaos. This post breaks down the structure and best practices for scalable Streamlit projects.",
        "date": "2025-11-05",
        "read_more": "See our demo structure in action."
    }
]

# Display the list
for post in blog_posts:
    with st.expander(f"**{post['title']}**  _{post['date']}_", expanded=False):
        st.write(post["excerpt"])
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("**Full Post:**")
            st.write(post["read_more"])
        with col2:
            if st.button("Read More", key=post["title"]):
                st.success("Redirecting to full article... (placeholder)")

# Pagination or total count
st.markdown("---")
st.markdown(f"*Showing {len(blog_posts)} posts. Stay tuned for more!*")