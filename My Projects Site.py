import streamlit as st
import pickle
import numpy as np

from PIL import Image

def display_image(image_path):
    image = Image.open('acc.PNG')
    st.image(image, caption='Accuracy Plot', use_column_width=True)

with open('lgbmodel.pkl', 'rb') as file:
    model1 = pickle.load(file)

with open('gbm.pkl', 'rb') as file:
    model11 = pickle.load(file)

with open('rc.pkl', 'rb') as file:
    model111 = pickle.load(file)

#Additional files/proj2model.pkl
with open('Additional files/proj2model.pkl', 'rb') as file:
    model2 = pickle.load(file)

# Define functions to make predictions using your models
def predict_model1(input_data):
    prediction = model1.predict(input_data)
    return prediction

def predict_model2(input_data):
    prediction = model2.predict(input_data)
    return prediction

# Home page content
def home():
    st.title('Welcome to My Project Showcase site')
    st.write('This is the home page of my project website.')

def overview():
    st.title('Overview of Projects')
    proj = st.selectbox('Select Project', [' ','Steam Games', 'Meteorite', 'Global Electricity'])
    if proj == 'Steam Games':
        header_image = "steam_thumbnail.jpg"  # Change this to the path of your image
        st.image(header_image, use_column_width=True)
        st.title("About Steam Games")
        st.write(
            "Steam is a digital distribution platform developed by Valve Corporation, primarily for purchasing and playing video games. "
            "It offers a vast library of games across various genres, including action, adventure, role-playing, simulation, strategy, sports, and more. "
            "Key features include:"
        )
        st.write(
            "- **Community Features**: Steam incorporates various community features, such as user reviews, forums, community hubs, and user-generated content, fostering interaction among players."
        )
        st.write(
            "- **Workshop Support**: Many games on Steam support the Steam Workshop, allowing players to create and share mods, maps, and other custom content, enhancing the gameplay experience."
        )
        st.write(
            "- **Achievements and Trading Cards**: Steam games often include achievements and trading cards, providing additional goals for players to accomplish and collectibles to trade or craft into badges."
        )
        st.write(
            "- **Sales and Discounts**: Steam hosts regular sales events, offering significant discounts on a wide selection of games. These events, such as the Steam Summer Sale and Steam Winter Sale, are eagerly anticipated by gamers."
        )
        st.write(
            "- **Multiplayer and Online Play**: Many Steam games offer multiplayer and online play, allowing players to compete or cooperate with others from around the world, enhancing the social aspect of gaming."
        )
        st.write(
            "- **Updates and Patches**: Game developers often release updates and patches through Steam, providing bug fixes, performance improvements, and new content to enhance the gaming experience."
        )
        st.markdown("[Visit Steam](https://store.steampowered.com/)")
    elif proj == 'Meteorite':
        st.title("Meteors and NASA")
        description = """
        Meteors, also commonly known as shooting stars, are small celestial objects that enter Earth's atmosphere and burn up due to friction, creating a streak of light in the sky. These objects are typically debris left behind by comets or asteroids. 

        NASA, the National Aeronautics and Space Administration, has been actively studying meteors and their impact on Earth's atmosphere for many years. NASA's efforts include tracking meteor showers, which occur when Earth passes through the debris trail of a comet, resulting in an increased number of visible meteors in the night sky.

        NASA also monitors larger meteors, known as fireballs or bolides, which can produce significant atmospheric effects or even impact the Earth's surface. Through observation, analysis, and modeling, NASA aims to better understand the characteristics and behavior of meteors, as well as their potential impact on our planet.
        """
        st.write(description)
        st.markdown("[Learn more about NASA's Meteor Studies](https://science.nasa.gov/solar-system/meteors-meteorites/facts/)")
    elif proj == 'Global Electricity':
        st.markdown("[Click here for more data on global electricity production](https://www.eia.gov/todayinenergy/detail.php?id=61928)")
    else:
        st.text('Please select a project to view description!')

# Projects page content
def projects():
    st.title('Projects')

    # Project selection dropdown
    selected_project = st.selectbox('Select Project', [' ','Steam games sales data prediction', 'Meteorite fall prediction', 'Global Electricity Production'])

    if selected_project == 'Steam games sales data prediction':

        redirect_url = 'https://colab.research.google.com/drive/1jlwEO0Z8N-xnutXI63Hp44OAQ9qS1gjA?usp=sharing'
        if st.button('Show Code'):
            st.markdown(f'<a href="{redirect_url}" target="_blank">Go to External Site</a>', unsafe_allow_html=True)
        
        st.header('Steam Games Sales Prediction App',divider='rainbow')
        st.subheader('Enter input data to predict')

        s1 = st.slider('Name',min_value=0,max_value=11561, value=11075)
        s2 = st.slider('Platform',min_value=0,max_value=30, value=26)
        s3 = st.slider('Genre',min_value=0,max_value=11, value=10)
        s4 = st.slider('Publisher',min_value=0,max_value=580, value=361)
        s5 = st.number_input('NA Sales', min_value=0.0, max_value=0.600000, value=0.410)
        s6 = st.number_input('EU Sales', min_value=0.0, max_value=0.300000, value=0.280)
        s7 = st.number_input('JP Sales', min_value=0.0, max_value=0.700000, value=0.0370)
        s8 = st.number_input('Other Sales', min_value=0.0, max_value=0.750000, value=0.084)
        s9 = st.number_input('Critic Score', min_value=67.00, max_value=72.00000, value=71.55)
        s10 = st.number_input('Critic Count', min_value=15.0, max_value=33.00000, value=32.90)
        s11 = st.number_input('User Score', min_value=40.0, max_value=95.00000, value=77.00, step=1.0)
        s12 = st.number_input('User Count', min_value=4.0, max_value=361.00000, value=322.00, step=1.0)
        s13 = st.slider('Developer',min_value=0.00,max_value=1695.00, step=1.0, value=1020.00)
        s14 = st.slider('Rating',min_value=0.00,max_value=7.00, step=1.0, value= 1.00)
       


        # if st.button('Predict'):
        #     st.subheader('Global Sales')
        #     result = model1.predict([[s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14]])
        #     st.write(f'Expected sales : {result[0]*80.12:.2f} M Units')

        selected_model = st.selectbox('Select Model', ['LGBM Regressor','Gradient Boosting Regressor', 'Random Forest Regressor'])
    
        # Perform prediction based on selected model
        if st.button('Predict'):
            if selected_model == 'Gradient Boosting Regressor':
                st.subheader('Global Sales')
                result = model11.predict([[s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14]])
                st.write(f'Expected sales : {result[0]*80.12:.2f} M Units')
  
            elif selected_model == 'LGBM Regressor':
                st.subheader('Global Sales')
                result = model1.predict([[s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14]])
                st.write(f'Expected sales : {result[0]*80.12:.2f} M Units')
            
            elif selected_model == 'Random Forest Regressor':
                st.subheader('Global Sales')
                result = model111.predict([[s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14]])
                st.write(f'Expected sales : {result[0]*80.12:.2f} M Units')



        if st.button('View Accuracy'):
            display_image('accuracy_plot.png')

    elif selected_project == 'Meteorite fall prediction':
        redirect_url = 'https://colab.research.google.com/drive/11MY4e2Q7Dn6mP191UWNpXENF6iFxn_XG?usp=sharing'
        if st.button('Show Code'):
            st.markdown(f'<a href="{redirect_url}" target="_blank">Go to External Site</a>', unsafe_allow_html=True)
        
        st.header('Meteorite Fall Prediction App',divider='rainbow')
        st.subheader('Enter input data to predict')
        max_values = {
                    'name': 45715.00000,
                    'id': 57458.00000,
                    'nametype': 1.00000,
                    'recclass': 465.00000,
                    'mass': 504.20000,
                    'year': 2027.00000,
                    'reclat': 81.16667,
                    'reclong': 354.47333
                    }

        min_values = {
                    'name': 0.00000,
                    'id': 1.00000,
                    'nametype': 1.00000,
                    'recclass': 0.00000,
                    'mass': 0.00000,
                    'year': 1963.00000,
                    'reclat': -87.36667,
                    'reclong': -165.43333
                    }

        t1 = st.number_input('Name', min_value=min_values['name'], max_value=max_values['name'], step=1.0, value=0.0)
        t2 = st.number_input('ID', min_value=1.00, max_value=57458.00, step=1.0, value=1.0)
        # t3 = st.number_input('Name Type', min_value=min_values['nametype'], max_value=max_values['nametype'], step=1.0)
        t3 = 1.0
        t4 = st.number_input('Rec Class', min_value=min_values['recclass'], max_value=max_values['recclass'], step=1.0, value=327.0)
        t5 = st.number_input('Mass', min_value=min_values['mass'], max_value=max_values['mass'], step=1.0, value=21.0)
        t6 = st.number_input('Year', min_value=min_values['year'], max_value=max_values['year'], step=1.0, value=1963.0)
        t7 = st.number_input('Rec Lat', min_value=min_values['reclat'], max_value=max_values['reclat'], step=1.0, value=50.77500	)
        t8 = st.number_input('Rec Long', min_value=min_values['reclong'], max_value=max_values['reclong'], step=1.0, value=6.08333)

        if st.button('Predict'):
            res = model2.predict([[t1, t2, t3, t4, t5, t6, t7, t8]])
            st.write(f'Status: {res[0]}')
    elif selected_project == 'Global Electricity Production':
        st.header('Global Electricity Production Prediction App',divider='rainbow')
        redirect_url = 'https://colab.research.google.com/drive/1ng00vs8AErfkEzqPZlt_KYh-GVrltq_g?usp=sharing'
        if st.button('Show Code'):
            st.markdown(f'<a href="{redirect_url}" target="_blank">Go to External Site</a>', unsafe_allow_html=True)
    else:
        st.text("Please select a project to predict from the dropdown menu!")

            


# Create a dictionary to map page names to their respective functions
pages = {
    'Home': home,
    'Overview': overview,
    'Projects': projects
}

# Create a sidebar navigation menu
selected_page = st.sidebar.selectbox('Navigation', list(pages.keys()))

# Display the selected page content
pages[selected_page]()
