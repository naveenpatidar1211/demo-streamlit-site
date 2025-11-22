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
Founded in 2023, we are a dedicated team of developers focused on democratizing data visualization. We believe that the ability to understand and present data should not be limited to technical experts. Inspired by tools such as Streamlit, our work revolves around creating platforms that are simple, scalable, and powerful.
Over time, we have expanded our capabilities, embracing new technologies, improving user experience, and continuously refining our approach. Our goal is to empower individuals, teams, and organizations to make smarter decisions by turning complex data into clear, interactive visuals.
As we grow, our commitment remains the same—delivering solutions that bridge the gap between data and understanding.

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