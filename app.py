#import library
import streamlit as st
import pandas as pd
import numpy as np
from sklearn import linear_model
from joblib import dump,load
import base64

#loading model file
model = load('./model_lr.joblib') 

def predict(model, input_df):
    predictions_df=pd.DataFrame(model.predict(input_df))
    predictions_df.columns=['Label']    
    predictions = predictions_df['Label'][0]
    return predictions

if __name__ == "__main__":
    add_selectbox = st.sidebar.selectbox(
        "How would you like to predict?",
        ("Online", "Batch"))
    st.sidebar.info('This app is created to predict house prices in boston area')
    st.title("Predicting boston houses prices")
    if add_selectbox == 'Online':
        crime=st.sidebar.number_input('CRIME' , min_value=0.1, max_value=1.0, value=0.1)
        zn =st.sidebar.number_input('ZN',min_value=0.1, max_value=1.0, value=0.1)
        indus = st.sidebar.number_input('INDUS', min_value=0, max_value=50, value=5)
        chas = st.sidebar.number_input('CHAS', min_value=1, max_value=10, value=3)
        nox = st.sidebar.number_input('NOX',  min_value=0, max_value=50, value=0)
        rm = st.sidebar.number_input('RM',  min_value=0, max_value=50, value=0)
        age = st.sidebar.number_input('Age', min_value=0, max_value=50, value=0)
        dis = st.sidebar.number_input('DIS', min_value=0, max_value=50, value=0)
        rad = st.sidebar.number_input('RAD', min_value=0, max_value=50, value=0)
        tax = st.sidebar.number_input('TAX', min_value=0, max_value=50, value=0)
        PTRATIO = st.sidebar.number_input('PTRATIO', min_value=0, max_value=50, value=0)
        B = st.sidebar.number_input('B', min_value=0, max_value=50, value=0)
        LSTAT = st.sidebar.number_input('LSTAT', min_value=0, max_value=50, value=0)
        
        output=""
        
        input_dict= {'CRIM':crime,
        'ZN':zn,
        'INDUS':indus,
        'CHAS':chas,
        'NOX': nox,
        'RM':rm,
        'AGE' : age,
        'DIS': dis,
        'RAD':rad,
        'TAX' : tax,
        'PTRATIO': PTRATIO,
        'B':B,
        'LSTAT':LSTAT}
        
        input_df = pd.DataFrame([input_dict])
        
        if st.button("Predict"):
            output = model.predict(input_df)
            output = str(output)
            st.success('The output is {}'.format(output))

    if add_selectbox == 'Batch':
        file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])
        if file_upload is not None:
            data = pd.read_csv(file_upload)
            predictions = model.predict(data)  
            data['predictions'] =  predictions       
            st.dataframe(data)
            data_csv = data.to_csv(index=False)
            data_csv_b64 = base64.b64encode(data_csv.encode()).decode()  # some strings
            href= f'<a href="data:file/csv;base64,{data_csv_b64}" download="myfilename.csv">Download csv file</a>'
            st.markdown(href, unsafe_allow_html=True)