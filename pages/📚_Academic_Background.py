import streamlit as st
import utils as ut

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
ut.courier_text("University", 30, "left")
ut.courier_text(
    """I finished my bachelor of science in data science at the IT-University
in Copenhagen in June, 2021. My bachelor thesis is titled "Networks and Passing Performance"
and I was awarded the highest passing grade at my oral defense.
You can download the paper below.""",
    14,
    "left",
)

# Example usage
ut.courier_download_button(
    label="📄 Networks and Passing Performance",
    data=PDFbyte,
    file_name="networks_and_passing_performance.pdf",
)

ut.courier_text(
    """And you can download my ITU transcript (120 BSc credits and 37 MSc credits, currently) here: """,
    14,
    "left",
)

ut.courier_download_button(
    label="📄 ITU transcript",
    data=ITU_pdf,
    file_name="ITU_transcript.pdf",
)

# items = [
#     "Danish, English, Python, SQL, Azure",
#     "Experienced data scientist & youth elite footballer",
#     "Performance analyst for women's national team in 2023 (up to and including WC in AUS/NZ '23)",
# ]

# ut.pretty_bullets(items, font_size=16, text_align="left")
st.divider()
ut.courier_text("High school", 30, "left")
ut.courier_text(
    """I finished high school top of my class in 2016 with A-levels in Danish*, History*, Mathematics** and Social science**.
My final <i>study line project</i> (<i>Studieretningsprojekt</i> in Danish) was a 
comparative  historical and mathematical analysis of two variations of poker: 
Five card draw and Texas Hold 'em. I was awarded the highest passing grade for the paper.
You can download the paper below.""",
    14,
    "left",
)

ut.courier_text(
    """(beware that it is in Danish but these days I'm 
sure any LLM will translate it for you if you ask it nicely...)""",
    14,
    "left",
)

# ut.vertical_space(1)

ut.courier_text(
    """*mandatory, **elective""",
    11,
    "right",
)

ut.courier_download_button(
    label="📄 Matematikken i og Historien om Poker",
    data=SRP_pdf,
    file_name="Matematikken_i_og_historien_om_poker.pdf",
)

ut.courier_text(
    """And you can download my high school diploma here: """,
    14,
    "left",
)

ut.courier_download_button(
    label="📄 High school diploma",
    data=afgangsbevis_pdf,
    file_name="stenhus.pdf",
)
