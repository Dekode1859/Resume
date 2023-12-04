import streamlit as st

def main():
    st.title("Software Developer Portfolio")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("Home")
        
    with col2:
        st.write("Project Showcase")
        
    with col3:
        st.write("About")
    
    
    

def show_home_page():
    st.header("Home")
    
    # Add your home page content here
    st.write("Welcome to my portfolio!")
    st.write("I'm a software developer.")
    st.write("I like to build cool stuff with Python and JavaScript.")

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
