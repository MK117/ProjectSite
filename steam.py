import pickle
import streamlit as st
import warnings
from sklearn.preprocessing import LabelEncoder
# from sklearn.exceptions import InconsistentVersionWarning
# warnings.simplefilter("error", InconsistentVersionWarning)

# try:
#    est = pickle.loads("model_from_prevision_version.pickle")
# except InconsistentVersionWarning as w:
#    print(w.original_sklearn_version)
warnings.filterwarnings('ignore')
st.header('Steam Games Sales Prediction App',divider='rainbow')

# with open('label_encoder.pkl', 'rb') as f:
#     lb = pickle.load(f)

# option = st.selectbox(
#     'Select the Game Platform',
#     ('Wii', 'NES', 'GB', 'DS', 'X360', 'PS3', 'PS2', 'SNES', 'GBA',
#        'PS4', '3DS', 'N64', 'PS', 'XB', 'PC', '2600', 'PSP', 'XOne',
#        'WiiU', 'GC', 'GEN', 'DC', 'PSV', 'SAT', 'SCD', 'WS', 'NG', 'TG16',
#        '3DO', 'GG', 'PCFX'))

# s1 = lb.transform([option])
# st.write(s1)
s1 = st.slider('Platform',min_value=1,max_value=30)
s2 = st.slider('Genre',min_value=1,max_value=11)
s3 = st.slider('Publisher',min_value=1,max_value=580)
s4 = st.slider('NA Sales',min_value=0.00,max_value=10.00,step=0.1)
s5 = st.slider('EU Sales',min_value=0.00,max_value=10.00,step=0.1)
s6 = st.slider('JP Sales',min_value=0.00,max_value=10.00,step=0.1)
s7 = st.slider('Other Sales',min_value=0.00,max_value=10.00,step=0.1)
s8 = st.slider('Critic_Score',min_value=0.00,max_value=10.00,step=0.1)
s9 = st.slider('Critic_Count',min_value=0.00,max_value=10.00,step=0.1)
s10 = st.slider('User_Score',min_value=0,max_value=10)
s11 = st.slider('User_Count',min_value=0.00,max_value=10.00,step=0.1)
s12 = st.slider('Developer',min_value=0,max_value=10)
s13 = st.slider('Rating',min_value=0,max_value=10)
# rcmodel = pickle.load(open('project1_saved_model.pkl','rb'))
rcmodel = pickle.load(open('randomforestmodel1.pkl','rb'))



# lst = np.array([[s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13]])
import numpy as np


if st.button('Predict'):
    result = rcmodel.predict([[s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13]])
    st.text(result[0])

import sklearn

# print("scikit-learn version:", sklearn.__version__)