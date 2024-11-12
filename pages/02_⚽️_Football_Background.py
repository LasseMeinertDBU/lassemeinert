import streamlit as st
import utils as ut
from importlib import reload

reload(ut)

ut.courier_text("Football Background", 40, "center")
ut.courier_text("Working", 30, "center")
ut.vertical_space(1)
ut.courier_text(
    "Danish Men's U21 National Team | Opposition Scout | EURO2025 qualifications",
    20,
    "left",
)
ut.courier_text(
    """Supplied the U21 Men's analyst and coaching staff with analysis of opposing 
    teams (prior to facing Wales away and Iceland home, both Ws). Helped out the main analyst when 
    travelling to watch opposition had us overlap.""",
    12,
    "left",
)

ut.vertical_space(1)

ut.courier_text(
    "Danish Women's National Team | Performance Analyst (consultant)", 20, "left"
)

ut.courier_text("Feb 2023 – August 2023 ", 12, "left")

a, _, b = st.columns((1, 0.05, 1.5))

ut.courier_text(
    """Participated in two national team camps in February and April, 
    respectively, prior to our five-week preparations for the World Cup 
    in Australia and the subsequent tournament. 
    Responsible for capturing tactical drone and stationary camera 
    footage during training, as well as managing post-training 
    synchronization and tagging in Sportscode. Additionally, responsible 
    for setting up video converters, live tagging, and making game footage 
    available at halftime during games, while maintaining live communication
    with an assistant coach on the bench.""",
    12,
    "left",
    container=a,
)


b.image("img/DBU_analyst.jpg")
ut.courier_text(
    """That hardcase went everywhere across Australia with me during our
    WC run. """,
    font_size=11,
    text_align="right",
    container=b,
)
video_path = "img/drone.mov"
a.video(video_path, start_time=0)
ut.courier_text(
    """*I took my drone license before starting my stint with the women's team.
    It was a big priority for the coaching staff to get tactical drone footage
    from training sessions.""",
    font_size=11,
    text_align="right",
    container=a,
)

st.divider()
ut.courier_text("Education", 30, "center")
ut.vertical_space(1)

ut.courier_text(
    "UEFA C license 2024 | C1 Feb | C2 Apr | C3 Sep",
    20,
    "left",
)  # container=a)
a, _, b = st.columns((1, 0.05, 1.5))
ut.courier_text(
    """Started and finished my C license in 2024. Took and passed the exam on October 2nd, 2024.
    """,
    font_size=12,
    text_align="left",
    container=a,
)
ut.vertical_space(1, container=a)

ut.courier_text(
    """I will be starting B1 in January 2025 and I am planning to 
    finish my UEFA B license ASAP.""",
    font_size=12,
    text_align="left",
    container=a,
)
ut.vertical_space(1, container=b)
b.image("img/c_eksamen.png")


st.divider()
ut.vertical_space(1)
ut.courier_text("Playing", 30, "center")
a, _, b = st.columns((1, 0.05, 0.5))
b.image("img/HIF.JPG")

ut.courier_text("Herlev IF | Player", 20, "left", a)
ut.courier_text(
    "Aug 2018 – June 2022, Spring 2023, Spring 2024 | Herlev, DK", 12, "left", a
)


ut.courier_text(
    """Earned 100+ caps in the top amateur league and 31 caps in the 3rd 
    division (semi-pro) while studying full time at ITU. Captained the team 
    from 2019 onwards.""",
    12,
    "left",
    a,
)
ut.vertical_space(1, a)
ut.courier_text("FC Roskilde | Youth Player", 20, "left", a)
ut.courier_text("2014 - 2017 | Roskilde, DK", 12, "left", a)
ut.courier_text(
    """Played one season in the U17s 1st division and two seasons in 
   the U19s 1st division.""",
    12,
    "left",
    a,
)

st.divider()
