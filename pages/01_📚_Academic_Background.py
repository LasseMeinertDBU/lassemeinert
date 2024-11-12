import streamlit as st
import utils as ut

# with open("styles/main.css") as f:
#     st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

pdf_file_name = "docs/Passing_Networks_and_Performance_Lasse_Meinert.pdf"

with open(pdf_file_name, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

srp_pdf_file = "docs/SRP.pdf"

with open(srp_pdf_file, "rb") as pdf_2:
    SRP_pdf = pdf_2.read()

afgangsbevis_pdf_file = "docs/stenhus.pdf"

with open(afgangsbevis_pdf_file, "rb") as pdf_3:
    afgangsbevis_pdf = pdf_3.read()

ITU_file = "docs/ITU_transcript.pdf"

with open(ITU_file, "rb") as pdf_3:
    ITU_pdf = pdf_3.read()


ut.courier_text("Academic Background", 40, "center")
ut.courier_text("University", 30, "center")

a, _, b = st.columns((1, 0.05, 1))

ut.courier_text(
    """I finished my bachelor of science in data science at the IT-University
in Copenhagen in June, 2021. My bachelor thesis is titled "Networks and Passing Performance"
and I was awarded the highest grade at my oral defense.""",
    14,
    "left",
    container=a,
)

ut.courier_download_button(
    label="📄 Networks and Passing Performance",
    data=PDFbyte,
    file_name="networks_and_passing_performance.pdf",
    container=a,
)


b.image("img/pass_network.png")
ut.courier_text(
    "*Passing network from my BSc thesis. Brøndby IF played with 3 CBs for most of the season. Attacking direction is left to right.",
    font_size=11,
    text_align="right",
    container=b,
)

# Example usage


ut.vertical_space(1, container=a)
ut.courier_text(
    """You can download my ITU transcript (120 BSc credits and 37 MSc credits, currently) here: """,
    14,
    "left",
    container=a,
)

ut.courier_download_button(
    label="📄 ITU transcript", data=ITU_pdf, file_name="ITU_transcript.pdf", container=a
)

# items = [
#     "Danish, English, Python, SQL, Azure",
#     "Experienced data scientist & youth elite footballer",
#     "Performance analyst for women's national team in 2023 (up to and including WC in AUS/NZ '23)",
# ]

# ut.pretty_bullets(items, font_size=16, text_align="left")
st.divider()
ut.courier_text("High school", 30, "center")
a, _, b = st.columns((1, 0.05, 1))
ut.courier_text(
    """I finished high school top of my class in 2016 with A-levels in Danish*, History*, Mathematics** and Social science**.
My final <i>study line project</i> (<i>Studieretningsprojekt</i> in Danish) was a 
comparative  historical and mathematical analysis of two variations of poker: 
Five card draw and Texas Hold 'em. I was awarded the highest grade for the paper.""",
    14,
    "left",
    container=a,
)

ut.courier_text(
    """""",
    14,
    "left",
    container=b,
)

ut.courier_download_button(
    label="📄 Matematikken i og Historien om Poker",
    data=SRP_pdf,
    file_name="Matematikken_i_og_historien_om_poker.pdf",
    container=b,
)

ut.courier_text(
    """(beware that it is in Danish but these days I'm 
sure any LLM will translate it for you if you ask it nicely...)""",
    14,
    "left",
    container=b,
)

ut.courier_text("""*mandatory, **elective""", 11, "right", container=a)


ut.courier_text(
    """And you can download my high school diploma here: """, 14, "left", container=b
)

ut.courier_download_button(
    label="📄 High school diploma",
    data=afgangsbevis_pdf,
    file_name="stenhus.pdf",
    container=b,
)
