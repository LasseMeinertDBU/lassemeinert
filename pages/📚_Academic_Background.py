import streamlit as st
import utils as ut

pdf_file_name = "docs/Passing_Networks_and_Performance_Lasse_Meinert.pdf"

with open(pdf_file_name, "rb") as pdf_file:
    PDFbyte = pdf_file.read()


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

items = [
    "Danish, English, Python, SQL, Azure",
    "Experienced data scientist & youth elite footballer",
    "Performance analyst for women's national team in 2023 (up to and including WC in AUS/NZ '23)",
]

ut.pretty_bullets(items, font_size=16, text_align="left")
