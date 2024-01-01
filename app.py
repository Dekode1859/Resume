# import streamlit as st

# # Define the sections of your website
# sections = {
#     "About Me": "This is the About Me section.",
#     "Latest News": "This is the Latest News section.",
#     "Experience": "This is the Experience section.",
#     "Posts": "This is the Posts section.",
#     "Contact Me": "This is the Contact Me section.",
# }

# # Define the layout of your website
# st.set_page_config(
#     page_title="My Website",
#     page_icon=":smiley:",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

# # Define the colors of your website
# primary_color = "#1E90FF"
# secondary_color = "#FFFFFF"
# tertiary_color = "#000000"

# # Define the styles of your website
# st.markdown(
#     f"""
#     <style>
#         .reportview-container {{
#             background-color: {secondary_color};
#             color: {tertiary_color};
#         }}
#         .sidebar .sidebar-content {{
#             background-color: {primary_color};
#             color: {tertiary_color};
#         }}
#         .streamlit-button {{
#             background-color: {primary_color};
#             color: {tertiary_color};
#         }}
#         .css-1aumxhk {{
#             color: {primary_color};
#         }}
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # Define the content of your website
# st.title("My Website")

# for section_name, section_content in sections.items():
#     st.header(section_name)
#     st.write(section_content)

# # Define the contact form of your website
# st.header("Contact Me")

# name = st.text_input("Name")
# email = st.text_input("Email")
# message = st.text_area("Message")
# submit = st.button("Submit")

# if submit:
#     st.write(f"Thank you for your message, {name}!")
import streamlit as st

# Define the layout of your website
st.set_page_config(
    page_title="My Website",
    page_icon=":smiley:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Define the colors of your website
primary_color = "#1E90FF"
secondary_color = "#FFFFFF"
tertiary_color = "#000000"

# Define the styles of your website
st.markdown(
    f"""
    <style>
        .reportview-container {{
            background-color: {secondary_color};
            color: {tertiary_color};
        }}
        .sidebar .sidebar-content {{
            background-color: {primary_color};
            color: {tertiary_color};
        }}
        .streamlit-button {{
            background-color: {primary_color};
            color: {tertiary_color};
        }}
        .css-1aumxhk {{
            color: {primary_color};
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Define the content of your website
st.title("My Website")

# Define the Experience section
st.header("Experience")

# Define the animated line
st.markdown(
    """
    <style>
        .line-container {{
            position: relative;
            width: 100%;
            height: 100px;
        }}
        .line {{
            position: absolute;
            top: 0;
            left: 50%;
            width: 2px;
            height: 100%;
            background-color: #1E90FF;
            animation: animate 2s linear infinite;
        }}
        @keyframes animate {{
            0% {{
                transform: translate(-50%, -50%) scaleY(0);
            }}
            50% {{
                transform: translate(-50%, -50%) scaleY(1);
            }}
            100% {{
                transform: translate(-50%, -50%) scaleY(0);
            }}
        }}
    </style>
    <div class="line-container">
        <div class="line"></div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Define the work experience details
work_experience = [
    {
        "title": "Software Engineer",
        "company": "Microsoft",
        "date": "Jan 2020 - Present",
        "description": "Developed and maintained software for Microsoft products.",
    },
    {
        "title": "Software Engineer Intern",
        "company": "Google",
        "date": "May 2019 - Aug 2019",
        "description": "Developed and tested software for Google products.",
    },
    {
        "title": "Software Engineer Intern",
        "company": "Amazon",
        "date": "May 2018 - Aug 2018",
        "description": "Developed and tested software for Amazon products.",
    },
]

for i, experience in enumerate(work_experience):
    st.write(f"**{experience['title']}**")
    st.write(f"{experience['company']} ({experience['date']})")
    st.write(f"{experience['description']}")

# Define the contact form of your website
st.header("Contact Me")

name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Message")
submit = st.button("Submit")

if submit:
    st.write(f"Thank you for your message, {name}!")
