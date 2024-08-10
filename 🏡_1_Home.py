import streamlit as st

pdf_file_name = "Lasse_Meinert_CV.pdf"

with open(pdf_file_name, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# with open("styles/main.css") as f:
#     st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

st.set_page_config(
    page_title="Main",
    page_icon=":wave:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Lasse Meinert ")

# https://mouadettali-streamlit-resume-1--home-xnsqgc.streamlit.app/

cols = st.columns((2))
cols[0].image("img/cropped_profil.png")
cols[1].write(
    """Data scientist working for the Danish football association (Dansk Boldsspil-Union). 
    BSc Data Science. UEFA C coaching license, working towards UEFA B license. 
    Performance analyst and opponent scout for the Danish U21 men's. Drone certificate. """
)

st.markdown(
    """
    <style>
    div.stDownloadButton > button {
        border: 2px solid #404040; /* Initial border color */
        transition: border-color 0.3s;
        color: white; /* Initial text color */
    }
    div.stDownloadButton > button:hover {
        border-color: #ff4b4b; /* Change this to your desired hover border color */
        color: white; /* Text color on hover, same as initial */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <style>
    ul.pretty-bullets {
        list-style-type: none; /* Remove default bullets */
        padding-left: 0; /* Remove default padding */
    }
    ul.pretty-bullets li {
        position: relative;
        padding-left: 1.5em; /* Space for custom bullet */
        margin-bottom: 0.5em; /* Space between bullets */
        line-height: 1.2em; /* Ensure consistent line height */
    }
    ul.pretty-bullets li:before {
        content: '•'; /* Custom bullet character */
        color: #76f5a0; /* Bullet color */
        font-size: 1em; /* Bullet size */
        position: absolute;
        left: 0;
        top: 50%;
        transform: translateY(-55%); /* Center the bullet vertically */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

cols[1].download_button(
    label="📄 Download Resume",
    data=PDFbyte,
    file_name=pdf_file_name,
    mime="application/octet-stream",
    # type="secondary",
)

cols[1].markdown(
    """
    <ul class="pretty-bullets">
        <li>Danish, English, Python, SQL, Azure</li>
        <li>Experienced data scientist & youth elite footballer</li>
        <li>Performance analyst for women's national team in 2023 (up to and including WC in AUS/NZ '23)</li>
    </ul>
 """,
    unsafe_allow_html=True,
)

# st.sidebar.title("")
# st.sidebar.write(
#     "Everyone needs a sidebar. As long as you keep your main bar happy... ;-)"
# )

st.header("About Me")
st.write(
    """26 years of age. I speak Danish, English, Python and SQL fluently. 
    I've been with DBU since leaving the IT-University in June 2022. 
    I've played football since the age of 3 and only recently quit 
    the top of the amateur levels to have more time for work and recreation. """
)

st.header("Projects")
st.write(
    """During my time with DBU I have built, developed and maintained 
    our end-to-end data analysis platform. This includes"""
)


# Create a list with custom bullets
st.markdown(
    """
    <ul class="pretty-bullets">
        <li>Relational cloud database (Microsoft SQL server)</li>
        <li>Automatic API pulls from data suppliers (Wyscout, OPTA) wrapped in Python-based Docker</li>
        <li>Automatic enrichment of SQL tables in Python (xG, xT, possession sequences)</li>
        <li>Automatically updating data visualizations in webapp (Streamlit wrapped in Docker) -- this includes standard reporting like a match report, team report, ...</li>
    </ul>
    """,
    unsafe_allow_html=True,
)

st.header("Contact")
# st.write("Provide contact information here.")
linked = """<a href="https://linkedin.com/in/lassemeinertpedersen" class="st-emotion-cache-1khpbey e1x90zqc0">LinkedIn</a>"""
github = """<a href="https://github.com/lassemeinertDBU" class="st-emotion-cache-1khpbey e1x90zqc0">Github</a>"""
st.markdown(linked, unsafe_allow_html=True)
st.markdown(github, unsafe_allow_html=True)
