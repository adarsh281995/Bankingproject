 
from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np
model = load_model('bank_deposit')






def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    return predictions

def run():
    from PIL import Image
    image = Image.open('honduras-banking.jpg')
    image_office = Image.open('banking.jpg')
    st.image(image,use_column_width=True)
    add_selectbox = st.sidebar.selectbox(
    "How would you like to predict?",
    ("Online", "Batch"))
    st.sidebar.info('This app is created to predict if a customer will deposit in the bank or not')
    st.sidebar.success('https://www.pycaret.org')
    st.sidebar.image(image_office)
    st.title("Predicting customer will deposit or not")
    if add_selectbox == 'Online':
        age=st.number_input('age' , min_value=18, max_value=95, value=18)
        balance =st.number_input('balance',min_value=-8019, max_value=102127, value=-8019)
        day = st.number_input('day', min_value=1, max_value=31, value=1)
        duration = st.number_input('duration', min_value=0, max_value=4918, value=0)
        campaign = st.number_input('campaign',  min_value=1, max_value=63, value=1)
        pdays = st.number_input('pdays',  min_value=-1, max_value=871, value=-1)
        previous=st.number_input('previous',  min_value=0, max_value=275, value=0)

        job = st.selectbox('job', ['blue-collar','management','technician',"admin.","services","retired","self-employed","entrepreneur","unemployed","housemaid","student","unknown"])
        marital= st.selectbox('marital', ['single', 'married','divorced'])
        education = st.selectbox('education', ['unknown', 'primary','secondary','tertiary'])
        default = st.selectbox('default', ['yes', 'no'])
        housing = st.selectbox('housing', ['yes', 'no'])
        loan = st.selectbox('loan', ['yes', 'no'])
        contact = st.selectbox('contact', ['cellular', 'telephone','uknown'])
        month = st.selectbox('month', ['jan', 'feb','mar','apr','may','june','jul','aug','sep','oct','nov','dec'])
        poutcome = st.selectbox('poutcome', ['uknown', 'failure','other','success'])
        deposit = st.selectbox('deposit', ['yes', 'no'])
        

        output=""
        input_dict={'age':age,'balance':balance,'day': day,'duration': duration,'campaign': campaign,'pdays': pdays,'previous' : previous,'job':job,'marital':marital,'education':education,'default':dafault,'housing':housing,'loan':loan,'contact':contact,'month':month,'poutcome':poutcome,'deposit':deposit}
        input_df = pd.DataFrame([input_dict])
        if st.button("Predict"):
            output = predict(model=model, input_df=input_df)
            output = str(output)
            if output == 'yes':
              output="the customer will deposit"
            else:
              output="the customer will not deposit"  
        st.success('output -- {}'.format(output))
    if add_selectbox == 'Batch':
        file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])
        if file_upload is not None:
            data = pd.read_csv(file_upload)            
            predictions = predict_model(estimator=model,data=data)
            st.write(predictions)
def main():
    run()

if __name__ == "__main__":
  main()
