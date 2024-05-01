import streamlit as st

# Function to create a horizontal navigation bar
def navigation_bar():
    st.markdown(
        """
        <style>
            .navbar {
                overflow: hidden;
                background-color: #333;
            }

            .navbar a {
                float: left;
                display: block;
                color: #f2f2f2;
                text-align: center;
                padding: 14px 20px;
                text-decoration: none;
                font-size: 17px;
            }

            .navbar a:hover {
                background-color: #ddd;
                color: black;
            }

            .navbar a.active {
                background-color: #4CAF50;
                color: white;
            }
        </style>
        """
    )
    st.markdown(
        """
        <div class="navbar">
            <a href="#home">Home</a>
            <a href="#about">About</a>
            <a href="#projects">Projects</a>
        </div>
        """
    )

# Title
st.title('My Project Showcase')

# Render navigation bar
navigation_bar()

# Description
st.write('Welcome to my project showcase! Here are some of my latest projects:')

# Home content
if st.sidebar.checkbox('Home', True, key='home'):
    st.header('Home')
    st.write('This is the home page.')

# About content
if st.sidebar.checkbox('About', key='about'):
    st.header('About')
    st.write('This is the about page.')

# Projects content
if st.sidebar.checkbox('Projects', key='projects'):
    st.header('Projects')
    st.write('This is the projects page.')
