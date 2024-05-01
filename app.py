import streamlit as st
import joblib

model=joblib.load('sentiment-model.pkl')

sentiment_labels={'1':'positive', '0':'negative'}  

st.title("Sentiment Analysis") 

user_input=st.text_area("Enter your text here:")
if st.button("predict"):
    predicted_sentiment=model.predict([user_input])[0]
    print('predicted Label:'+str(predicted_sentiment))
    predicted_sentiment_label=sentiment_labels[str(predicted_sentiment)]

    st.info(f"predicted Sentiment: {predicted_sentiment_label}")