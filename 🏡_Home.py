import streamlit as st
import utils as ut

pdf_file_name = "docs/Lasse_Meinert_CV.pdf"

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

st.sidebar.title("Navigation")

# st.title("Lasse Meinert ")
ut.courier_text("Lasse Meinert", 40, "center")

ut.vertical_space(1)

# https://mouadettali-streamlit-resume-1--home-xnsqgc.streamlit.app/

cols = st.columns((2))
cols[0].image("img/cropped_profil.png")

t = """Data scientist working for the Danish football association (Dansk Boldsspil-Union). 
    BSc Data Science. UEFA C coaching license, working towards UEFA B license. 
    Performance analyst and opponent scout for the Danish U21 men's. Drone certificate. """

items = [
    "Danish, English, Python, SQL, Azure",
    "Experienced data scientist & youth elite footballer",
    "Performance analyst for women's national team in 2023 (up to and including WC in AUS/NZ '23)",
]

with cols[1] as c:
    ut.courier_text(t, 14, "left", c)

    ut.courier_download_button(
        label="Download Resume", data=PDFbyte, file_name=pdf_file_name, container=c
    )

    ut.pretty_bullets(items=items, font_size=14, container=c)

st.markdown("---")

t = """26 years of age. I speak Danish, English, Python and SQL fluently. 
    I've been with DBU since leaving the IT-University in June 2022. 
    I've played football since the age of 3 and only recently quit 
    the top of the amateur levels to have more time for work and recreation. """

ut.courier_text("About Me", font_size=30, text_align="left")
ut.courier_text(t, font_size=14, text_align=14)

st.header("Projects")
t = """During my time with DBU I have built, developed and maintained 
    our end-to-end data analysis platform. This includes"""

ut.courier_text(t)


items = [
    "Relational cloud database (Microsoft SQL server)",
    "Automatic API pulls from data suppliers (Wyscout, OPTA) wrapped in Python-based Docker",
    "Automatic enrichment of SQL tables in Python (xG, xT, possession sequences)",
    "Automatically updating data visualizations in webapp (Streamlit wrapped in Docker) -- this includes standard reporting like a match report, team report, ...",
]

# Create a list with custom bullets
ut.pretty_bullets(items=items, font_size=14)

ut.courier_text("Contact", font_size=30)
# st.write("Provide contact information here.")
linked = """<a href="https://linkedin.com/in/lassemeinertpedersen" class="st-emotion-cache-1khpbey e1x90zqc0">LinkedIn</a>"""
github = """<a href="https://github.com/lassemeinertDBU" class="st-emotion-cache-1khpbey e1x90zqc0">Github</a>"""
ut.courier_text(linked, font_size=14)
ut.courier_text(github, font_size=14)
