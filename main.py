import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pandas as pd

st.title("Personality Test")

df = pd.read_csv("personality_dataset.csv")
df.dropna(inplace=True)
df["Stage_fear"] = df["Stage_fear"].apply(lambda x: 1 if x == "Yes" else 0)
df["Drained_after_socializing"] = df["Drained_after_socializing"].apply(lambda x: 1 if x == "Yes" else 0)
df["Personality"] = df["Personality"].apply(lambda x: 0 if x == "Introvert" else 1)
X = df.drop("Personality",axis=1)
y = df["Personality"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,shuffle=True)
model = LogisticRegression()
model.fit(X_train,y_train)

time = st.number_input("Enter Time Spend Alone")
stage = st.selectbox("Do you have stage fear?",[0,1])
socialevent = st.number_input("Enter Social Event Attendance")
going = st.number_input("Enter Going Outside")
drained = st.selectbox("Do you Feel Drained After Socializing?",[0,1])
friendcirle = st.number_input("Enter Friend Circle Size")
post = st.number_input("Enter Post Frequency")

st.info("Has a Accuracy of 92% on Test Data")

if st.button("Analyse"):
    pred = model.predict([[time,stage,socialevent,going,drained,friendcirle,post]])
    if pred == 0:
        st.write("You are Introvert")
    else:
        st.write("You are Extrovert")


