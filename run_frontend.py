import json
import requests

import streamlit as st
import joblib
import pickle

st.header('Credit Machine Learning Model ☄️​​💴​')
st.write("")

model_selected = st.selectbox('Select the machine learning model you prefer 🌳 ​vs 🚀​',
                             ['RandomForest', 'XGBClassifier'])

st.write(f'Select the feature inputo to make a prediction with {model_selected}')

col1, col2 = st.columns(2)

with col1:

    credit_limit = st.number_input("Enter your credit limit:",step=1)
    gender = st.number_input('Male or Female (0,1): ', min_value=0, max_value=1, step=1)
    education = st.number_input('Education level (1-5): ',min_value=0, max_value=5, step=1)
    age = st.number_input('Age: ', step=1)
    n_delay_payment = st.number_input('Num of delay payment: ',step=1)

with col2:
    bill_at_1 = st.number_input('Bill at 1: ',step=1)
    bill_at_2 = st.number_input('Bill at 2: ',step=1)
    bill_at_3 = st.number_input('Bill at 3: ',step=1)
    bill_at_4 = st.number_input('Bill at 4: ',step=1)
    bill_at_5 = st.number_input('Bill at 5: ',step=1)
    bill_at_6 = st.number_input('Bill at 6: ',step=1)


threshold = st.slider('Select your threshold classification: ', min_value=0, max_value=100,value=50)
st.write("Your threshold is", threshold ,'%', ' for classification')

inputs = {
        'credit_limit':credit_limit,
        'gender':gender,
        'education':education,
        'age':age,
        'n_delay_payment':n_delay_payment,
        'bill_at_1': bill_at_1,
        'bill_at_2': bill_at_2,
        'bill_at_3': bill_at_3,
        'bill_at_4': bill_at_4,
        'bill_at_5': bill_at_5,
        'bill_at_6': bill_at_6,
        'model_name':model_selected
        }

if st.button("Make predictions ☄️"):
    res = requests.post(url="http://127.0.0.1:8000/predict_model", data=json.dumps(inputs))
    st.subheader(f"Response from ML API☄️: {res.json()['Prediction']}")



model = joblib.load('models/RForestModel.pkl')


st.subheader('Download the model below ⬇️​')
st.download_button(
    f"Download Model {model_selected} ✅​",
    data=pickle.dumps(model),
    file_name="rm_model.pkl"
)
