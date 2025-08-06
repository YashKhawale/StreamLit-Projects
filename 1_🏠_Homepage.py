import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded",)

st.title("Welcome to Yash Khawale's Streamlit Web App")

col1, col2, col3 = st.columns(3, vertical_alignment="center", gap="large")
with col1:
    st.metric(label="Total Active Projects in Web App", value="4", delta=4, border=True)
with col2:
    st.image("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-lighttext.png", width=300)
with col3:
    st.image("https://www.python.org/static/community_logos/python-logo.png", width=300)
st.markdown("""
#### This web app is designed to showcase various projects and applications built using Streamlit.
#### You can explore different projects by selecting them from the sidebar.
#### You can also find the source code for this app on [GitHub](https://github.com/YashKhawale/StreamLit-Projects).
""")

st.sidebar.success("Select a Project above.")