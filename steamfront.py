import streamlit as st
import pickle
import numpy as np

# Load your pickled machine learning models
with open('xgmodel.pkl', 'rb') as file:
    model1 = pickle.load(file)

with open('proj2model.pkl', 'rb') as file:
    model2 = pickle.load(file)

# Define functions to make predictions using your models
def predict_model1(input_data):
    prediction = model1.predict(input_data)
    return prediction

def predict_model2(input_data):
    prediction = model2.predict(input_data)
    return prediction

# Create the Streamlit web interface
def home():
    st.title('Welcome to My Portfolio')
    st.write('This is the home page of my portfolio.')

# About page content
def about():
    st.title('About Me')
    st.write('I am a data scientist passionate about machine learning and web development.')

# Contact page content
def contact():
    st.title('Contact Me')
    st.write('You can reach me at: example@example.com')

# Projects page content
def projects():
    st.title('Projects')

    # Add input fields for user input
    st.sidebar.title('Input Parameters')

    # Project selection dropdown
    project_selection = st.sidebar.multiselect('Select Project', ['Project 1', 'Project 2'])

    if 'Project 1' in project_selection:
        st.sidebar.subheader('Project 1 Inputs')
        input_params_project1 = []
        for i in range(13):
            input_param = st.sidebar.slider(f'Input Parameter {i+1}', min_value=0.0, max_value=100.0, value=50.0, key=f'param1_{i}')
            input_params_project1.append(input_param)
        input_data_project1 = np.array([input_params_project1])  # Format input data for project 1 prediction

        if st.sidebar.button('Predict Project 1'):
            st.subheader('Project 1 Prediction')
            prediction1 = predict_model1(input_data_project1)
            st.write(f'Project 1 predicted class: {prediction1}')

    if 'Project 2' in project_selection:
        st.sidebar.subheader('Project 2 Inputs')
        input_params_project2 = []
        for i in range(8):
            input_param = st.sidebar.number_input(f'Input Parameter {i+1}', min_value=-300.0, max_value=50000.0, value=0.0, step=1.0, key=f'param2_{i}')
            input_params_project2.append(input_param)
        input_data_project2 = np.array([input_params_project2])  # Format input data for project 2 prediction

        if st.sidebar.button('Predict Project 2'):
            st.subheader('Project 2 Prediction')
            prediction2 = predict_model2(input_data_project2)
            st.write(f'Project 2 predicted class: {prediction2}')

# Create a dictionary to map page names to their respective functions
pages = {
    'Home': home,
    'About': about,
    'Contact Me': contact,
    'Projects': projects
}

# Create a sidebar navigation menu
selected_page = st.sidebar.radio('Navigation', list(pages.keys()))

# Display the selected page content
pages[selected_page]()