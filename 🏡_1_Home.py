import streamlit as st

st.set_page_config(
    page_title="My Personal Website",
    page_icon=":wave:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Welcome to My Personal Website")

cols = st.columns((2))
cols[0].image("img/cropped_profil.png")
cols[1].write("Hello, world! This is my personal website built with Streamlit.")

st.sidebar.title("Navigation")
st.sidebar.write("This is the sidebar.")

st.header("About Me")
st.write("This section can include information about you.")

st.header("Projects")
st.write("Showcase your projects here.")

st.header("Contact")
st.write("Provide contact information here.")
