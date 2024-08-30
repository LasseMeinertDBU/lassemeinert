import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections import register_projection
from matplotlib.projections.polar import PolarAxes
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D


def courier_text(
    text: str, font_size: int = 14, text_align: str = "left", container=None
):
    markdown_func = st.markdown if container is None else container.markdown
    markdown_func(
        f"""
        <p style="
            font-family: Courier, monospace;
            font-size: {font_size}px;
            text-align: {text_align};
            margin: 0;
        ">
        {text}
        </p>
        """,
        unsafe_allow_html=True,
    )


def pretty_bullets(
    items,
    font_size: int = 14,
    text_align: str = "left",
    bullet_color: str = "#76f5a0",
    container=None,
):
    list_items = "".join(
        f"""
        <li style="
            font-family: Courier, monospace;
            font-size: {font_size}px;
            text-align: {text_align};
            position: relative;
            padding-left: 1.5em;
            margin-bottom: 0.5em;
            line-height: 1.2em;
        ">
        {item}
        </li>
        """
        for item in items
    )

    markdown_func = st.markdown if container is None else container.markdown
    markdown_func(
        f"""
        <style>
        ul.pretty-bullets {{
            list-style-type: none; /* Remove default bullets */
            padding-left: 0; /* Remove default padding */
            font-family: Courier, monospace; /* Set font-family to Courier */
        }}
        ul.pretty-bullets li {{
            position: relative;
            padding-left: 1.5em; /* Space for custom bullet */
            margin-bottom: 0.5em; /* Space between bullets */
            line-height: 1.2em; /* Ensure consistent line height */
            font-family: Courier, monospace; /* Ensure each list item uses Courier */
        }}
        ul.pretty-bullets li:before {{
            content: '•'; /* Custom bullet character */
            color: {bullet_color}; /* Bullet color */
            font-size: 1em; /* Bullet size */
            position: absolute;
            left: 0;
            top: 50%;
            transform: translateY(-55%); /* Center the bullet vertically */
            font-family: Courier, monospace; /* Ensure bullet uses Courier */
        }}
        </style>
        <ul class="pretty-bullets">
            {list_items}
        </ul>
        """,
        unsafe_allow_html=True,
    )


def courier_download_button(label: str, data, file_name: str, container=None):
    markdown_func = st.markdown if container is None else container.markdown
    download_button_func = (
        st.download_button if container is None else container.download_button
    )

    markdown_func(
        """
        <style>
        /* Style for the download button */
        div.stDownloadButton > button {
            border: 2px solid #404040; /* Initial border color */
            transition: border-color 0.3s;
            color: white; /* Initial text color */
            font-family: Courier, monospace; /* Set font-family to Courier */
            display: block; /* Make button a block element */
            margin: 0 auto; /* Center the button */
            background-color: #0e1117; /* Set background color to match Streamlit's dark theme */
        }
        div.stDownloadButton > button:hover {
            border-color: #ff4b4b; /* Change this to your desired hover border color */
            color: white; /* Text color on hover, same as initial */
            font-family: Courier, monospace; /* Maintain font-family on hover */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    download_button_func(
        label=label,
        data=data,
        file_name=file_name,
        mime="application/octet-stream",
    )


def vertical_space(lines: int, container=None):
    # Generate the specified number of empty lines using <br> tags
    empty_lines = "<br>" * lines

    # Determine whether to use st.markdown or container.markdown
    markdown_func = st.markdown if container is None else container.markdown

    # Output the empty lines to the appropriate container
    markdown_func(empty_lines, unsafe_allow_html=True)


def radar_factory(num_vars, frame="circle"):
    """
    Create a radar chart with `num_vars` Axes.

    This function creates a RadarAxes projection and registers it.

    Parameters
    ----------
    num_vars : int
        Number of variables for radar chart.
    frame : {'circle', 'polygon'}
        Shape of frame surrounding Axes.

    """
    # calculate evenly-spaced axis angles
    theta = np.linspace(0, 2 * np.pi, num_vars, endpoint=False)

    class RadarTransform(PolarAxes.PolarTransform):

        def transform_path_non_affine(self, path):
            # Paths with non-unit interpolation steps correspond to gridlines,
            # in which case we force interpolation (to defeat PolarTransform's
            # autoconversion to circular arcs).
            if path._interpolation_steps > 1:
                path = path.interpolated(num_vars)
            return Path(self.transform(path.vertices), path.codes)

    class RadarAxes(PolarAxes):

        name = "radar"
        PolarTransform = RadarTransform

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # rotate plot such that the first axis is at the top
            self.set_theta_zero_location("N")

        def fill(self, *args, closed=True, **kwargs):
            """Override fill so that line is closed by default"""
            return super().fill(closed=closed, *args, **kwargs)

        def plot(self, *args, **kwargs):
            """Override plot so that line is closed by default"""
            lines = super().plot(*args, **kwargs)
            for line in lines:
                self._close_line(line)

        def _close_line(self, line):
            x, y = line.get_data()
            # FIXME: markers at x[0], y[0] get doubled-up
            if x[0] != x[-1]:
                x = np.append(x, x[0])
                y = np.append(y, y[0])
                line.set_data(x, y)

        def set_varlabels(self, labels):
            self.set_thetagrids(np.degrees(theta), labels)

        def _gen_axes_patch(self):
            # The Axes patch must be centered at (0.5, 0.5) and of radius 0.5
            # in axes coordinates.
            if frame == "circle":
                return Circle((0.5, 0.5), 0.5)
            elif frame == "polygon":
                return RegularPolygon((0.5, 0.5), num_vars, radius=0.5, edgecolor="k")
            else:
                raise ValueError("Unknown value for 'frame': %s" % frame)

        def _gen_axes_spines(self):
            if frame == "circle":
                return super()._gen_axes_spines()
            elif frame == "polygon":
                # spine_type must be 'left'/'right'/'top'/'bottom'/'circle'.
                spine = Spine(
                    axes=self,
                    spine_type="circle",
                    path=Path.unit_regular_polygon(num_vars),
                )
                # unit_regular_polygon gives a polygon of radius 1 centered at
                # (0, 0) but we want a polygon of radius 0.5 centered at (0.5,
                # 0.5) in axes coordinates.
                spine.set_transform(
                    Affine2D().scale(0.5).translate(0.5, 0.5) + self.transAxes
                )
                return {"polar": spine}
            else:
                raise ValueError("Unknown value for 'frame': %s" % frame)

    register_projection(RadarAxes)
    return theta


def example_data():

    things = [
        ("Self-Assessment", 5),
        ("Data\nEngineering", 75),
        ("Data\nModeling", 65),
        ("Data\nVisualization", 89),
        ("Cloud\nComputing", 77),
        ("Programming\nSkills", 80),
        ("Football\nAnalytics", 93),
        ("Football\nKnowledge", 74),
        ("Project\nManagement", 63),
        ("Collaboration\n& Communication", 87),
    ]

    categories = [tpl[0] for tpl in things]
    values = [tpl[1] for tpl in things]

    return categories, values
