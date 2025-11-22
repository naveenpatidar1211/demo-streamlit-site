import streamlit as st

# Page config
st.set_page_config(page_title="About", page_icon="👤")

# Header
st.markdown("# 👤 About Us")
st.markdown("### *Discover Who We Are*")
st.markdown("---")

# Bio text content
st.markdown("""
#### Our Story
We are a team of developers dedicated to making data visualization accessible. Founded in 2023, our mission is to empower users with tools like Streamlit.

#### Meet the Founder
**Jane Doe**  
*Full-Stack Developer & Streamlit Enthusiast*  
With over 10 years in software engineering, Jane discovered Streamlit during a hackathon. "Streamlit turns Python scripts into shareable web apps in minutes—it's magic!" When not coding, she's hiking in the Rockies or mentoring at local tech meetups.

#### What Drives Us?
- **Innovation**: Pushing boundaries with open-source tools.
- **Community**: Contributing to forums and GitHub repos.
- **Fun**: Because building apps should be enjoyable!

Thanks for visiting. We’d love to hear your feedback!
""")

# Add an image placeholder (you can replace with a real URL)
st.image("https://via.placeholder.com/400x200?text=Team+Photo", caption="Our amazing team (placeholder)", use_column_width=True)

st.markdown("---")
st.markdown("*Connect with us: [LinkedIn](https://linkedin.com) | [GitHub](https://github.com)*")