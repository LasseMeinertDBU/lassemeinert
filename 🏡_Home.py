import streamlit as st
import utils as ut
import matplotlib.pyplot as plt
from importlib import reload
from streamlit_navigation_bar import st_navbar

reload(ut)
# st.sidebar.title("Navigation")


pdf_file_name = "docs/Lasse_Meinert_CV.pdf"

with open(pdf_file_name, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# with open("styles/main.css") as f:
#     st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# st.set_page_config(
#     page_title="Main",
#     page_icon=":wave:",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

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
    "Performance analyst for the women's national team in 2023 (up to and including WC in AUS/NZ '23)",
]

with cols[1] as c:
    ut.courier_text(t, 14, "left", c)

    ut.courier_download_button(
        label="Download Resume", data=PDFbyte, file_name=pdf_file_name, container=c
    )

    ut.pretty_bullets(items=items, font_size=14, container=c)

st.markdown("---")

t = """26 years of age. I speak Danish, English, Python, and SQL fluently.
    I've been with DBU since leaving the IT-University of Copenhagen in June 2022.
    I've played football since the age of 3 and only recently quit
    the top amateur level to have more time for work and recreation. """

t_2 = """ I've lived in Copenhagen for the past 5 years and 
I'm an avid traveller, both privately and whenever national team duty calls."""

ut.courier_text("About Me", font_size=30, text_align="left")
cols = st.columns((1, 2))

with cols[0] as c:
    ut.courier_text(t, font_size=14, text_align=14, container=c)
    ut.vertical_space(1)
    ut.courier_text(t_2, font_size=14, text_align=14, container=c)


categories, values = ut.example_data()

N = len(categories)
theta = ut.radar_factory(N, frame="polygon")

fig, ax = plt.subplots(
    figsize=(9, 9), nrows=1, ncols=1, subplot_kw=dict(projection="radar")
)
fig.subplots_adjust(wspace=0.25, hspace=0.20, top=0.85, bottom=0.05)

case_data = ut.example_data()

# colors = ["b", "r", "g", "m", "y"] * 2
color = "#76f5a0"
# Plot the four cases from the example data on separate Axes
# for category, value in zip(categories, values):
ax.set_rgrids([0.2, 0.4, 0.6, 0.8])
# ax.set_title(
#     category,
#     weight="bold",
#     size="medium",
#     position=(0.5, 1.1),
#     horizontalalignment="center",
#     verticalalignment="center",
# )
# for d, color in zip(case_data, colors):
ax.plot(theta, values, color=color)
ax.fill(
    theta,
    values,
    facecolor=color,
    alpha=0.25,
)  # label="_nolegend_")
ax.set_varlabels(categories)
for label in ax.get_xticklabels():
    label.set_color("white")

fig.set_facecolor("None")

ax.xaxis.grid(False)
ax.spines["polar"].set_color("None")
ax.set_yticklabels([])

ax.patch.set_facecolor("None")

fig.text(
    0.5,
    0.965,
    "Totally accurate profile",
    horizontalalignment="center",
    color="white",
    weight="bold",
    size="large",
)

fig.text(
    0.5,
    0.935,
    "4 seasons of data (2 years)",
    horizontalalignment="center",
    color="white",
    weight="regular",
    size="large",
)

cols[1].pyplot(fig)

st.divider()

# ut.vertical_space(1)
ut.courier_text("Experience", font_size=30)
t = """During my time with DBU I have built, developed, and maintained
    our end-to-end data analysis platform. This includes:"""

ut.courier_text(t)

items = [
    "Relational cloud database (Microsoft SQL server)",
    "Automatic API pulls from data suppliers (Wyscout, OPTA) wrapped in Python-based Docker",
    "Automatic enrichment of SQL tables in Python (xG, xT, possession sequences, ...)",
    "Automatically updating data visualizations in webapp (Streamlit wrapped in Docker) -- this includes standard reporting like a match report, team report, ..., and drill-down tools for our analysts",
]

# Create a list with custom bullets
ut.pretty_bullets(items=items, font_size=14)
st.divider()
ut.courier_text("Contact", font_size=30)
# st.write("Provide contact information here.")
linked = """<a href="https://linkedin.com/in/lassemeinertpedersen" class="st-emotion-cache-1khpbey e1x90zqc0">LinkedIn</a>"""
github = """<a href="https://github.com/lassemeinertDBU" class="st-emotion-cache-1khpbey e1x90zqc0">Github</a>"""
ut.courier_text(linked, font_size=14)
ut.courier_text(github, font_size=14)
