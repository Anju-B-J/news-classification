import streamlit as st
import joblib

# Load the trained model
model = joblib.load("news-classification-model.pkl")
#define sentiment labels
news_labels ={'0': 'Technical', '1':'Business', '2':'Sport','3':'Entertainment','4':'politics'}
# Create streamlit app
st.title("News Classification")
# input tyext area
user_input = st.text_area("Enter news here:")
#prediction button
if st.button("predict"):
    #perform sentiment prediction
    #print(user_input)
    predicted_label = model.predict([user_input])[0]
    #print("predicted Label:" + str(predicted_sentiment))
    predicted_news_label = news_labels[str(predicted_label)]

    #display predicted sentiment
    st.info(f"predicted News label: {predicted_news_label}")