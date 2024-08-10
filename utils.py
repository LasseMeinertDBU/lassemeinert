import streamlit as st


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
