import streamlit as st
import pickle

st.title("Personality Test")

with open("personality_test.pkl",'rb') as f:
    model = pickle.load(f)

time = st.number_input("Enter Time Spend Alone")
stage = st.selectbox("Do you have stage fear?",[0,1])
socialevent = st.number_input("Enter Social Event Attendance")
going = st.number_input("Enter Going Outside")
drained = st.selectbox("Do you Feel Drained After Socializing?",[0,1])
friendcirle = st.number_input("Enter Friend Circle Size")
post = st.number_input("Enter Post Frequency")

st.info("Has a Accuracy of 93% on Test Data")

if st.button("Analyse"):
    pred = model.predict([[time,stage,socialevent,going,drained,friendcirle,post]])
    if pred == 0:
        st.info("You are Introvert")
    else:
        st.info("You are Extrovert")


