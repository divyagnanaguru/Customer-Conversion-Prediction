import streamlit as st
import pandas as pd
import pickle
import time
import warnings
warnings.filterwarnings("ignore")

st.set_page_config(page_title="Customer Conversion Prediction", page_icon="ins.png", layout="centered")

st.title("Customer Conversion Prediction")



def ccp_predictor(job, education_qual, call_type, dur, num_calls, prev_outcome):
    pickle_file = open("Customer_Conversion_Prediction.pkl", "rb")
    model = pickle.load(pickle_file)
    prediction = model.predict([[job,education_qual,call_type,dur,num_calls,prev_outcome]])
    if prediction[0] == 0:
        return "This customer has very less chance to subscribe the Insurance!"
    else:
        return "This customer has a great chance to subscribe the Insurance!"

def main():
    html_temp = """
    <div style="background-color:black;padding:7px">
    <h2 style="color:grey;text-align:center;">Enter the required details</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    age = st.slider("Enter the age :",0,100,step=1)
    job = st.radio("Enter the job :", ('Blue Collar','Entrepreneur','House-maid','Services','Technician','Self-Employed','Admin','Management','Unemployed','Retired','	Student'))
    marital = st.radio("Enter the marital status :",('Married','Divorced','Single'))
    education_qual = st.radio("Enter the education qualification :", ('Primary', 'Secondary(UG)', 'Tertiary(PG'))
    call_type = st.radio("Enter the call type :", ('Cellular', 'Telephone', 'Unknown'))
    day = st.number_input("Enter the day :",1,31,step=1)
    mon = st.number_input("Enter the month :",0,11,step=1)
    dur = st.slider("Enter the duration :",0,643,step=1)
    num_calls = st.number_input("Enter the no.of calls :",0,6,step=1)
    prev_outcome = st.radio("Enter the previous outcome :", ('Unknown','Failure','Other','Success'))
    result=''

    if st.button("Predict"):
        result = ccp_predictor(job,education_qual,call_type,dur,num_calls,prev_outcome)
        with st.spinner("Predicting..."):
            time.sleep(3)
        st.success(result)


if __name__ == '__main__':
    main()
