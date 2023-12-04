import streamlit as st

def main():
    st.title("Software Developer Portfolio")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # make a clickable button named home that reroutes to the home page
        if st.button("Home"):
            st.write("Welcome to my portfolio!")
            st.write("My name is Michael and I am a software developer.")
            st.write("I am currently a senior at the University of Texas at Dallas majoring in Computer Science.")
            st.write("I am currently looking for a full-time position as a software developer.")
            st.write("I am proficient in Python, Java, C, and C++.")
            st.write("I have experience in web development using HTML, CSS, and JavaScript.")
            st.write("I have experience in SQL and NoSQL databases.")
            st.write("I have experience in cloud computing using AWS.")
            st.write("I have experience in machine learning using Python and TensorFlow.")
            st.write("I have experience in data analysis using Python and Pandas.")
            st.write("I have experience in mobile development using Android Studio.")
            st.write("I have experience in game development using Unity.")
            st.write("I have experience in version control using Git.")
            st.write("I have experience in agile development using Scrum.")
            st.write("I have experience in software testing.")
            
    with col2:
        # make a clickable button named projects that reroutes to the projects page
        if st.button("Projects"):
            st.write("Here are some of my projects!")
            st.write("My projects are also available on my GitHub profile.")
            st.write("  ")
            st.write("  ")  
            st.write("  ")
            
            # make a clickable button named project1 that reroutes to the project1 page
            if st.button("Project 1"):
                st.write("Project 1")
                st.write("  ")
                st.write("  ")
                st.write("  ")
                
            # make a clickable button named project2 that reroutes to the project2 page
            if st.button("Project 2"):
                st.write("Project 2")
                st.write("  ")
                st.write("  ")
                st.write("  ")
                
            # make a clickable button named project3 that reroutes to the project3 page
            if st.button("Project 3"):
                st.write("Project 3")
                st.write("  ")
                st.write("  ")
                st.write("  ")
                
    

if __name__ == "__main__":
    main()
