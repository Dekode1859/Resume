import streamlit as st

def main():
    st.title("Software Developer Portfolio")
    
    # Sidebar navigation
    page = st.sidebar.selectbox("Select a page", ("Project Showcase", "About"))
    
    if page == "Project Showcase":
        show_project_showcase()
    elif page == "About":
        show_about_page()

def show_project_showcase():
    st.header("Project Showcase")
    
    # Add your project showcase content here
    st.write("Project 1")
    st.write("Project 2")
    st.write("Project 3")

def show_about_page():
    st.header("About")
    
    # Add your about page content here
    st.write("Name: John Doe")
    st.write("Experience: X years")
    st.write("Skills: Python, JavaScript, HTML, CSS")

if __name__ == "__main__":
    main()
