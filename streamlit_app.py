import streamlit as st
import tweepy
import pandas as pd
import pickle
import matplotlib.pyplot as plt 
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import GridSearchCV



"""
# MY APP

This is my app. Yay! 
"""

# Add session variables 
if 'is_credential' not in st.session_state:
     st.session_state.is_credential = False
     
if 'private_key' not in st.session_state:
     st.session_state.private_key = ''
     
if 'private_token' not in st.session_state:
     st.session_state.private_token = ''
     
if 'tweet_text' not in st.session_state:
     st.session_state.tweet_text = ''
     
# Load model
clf = pickle.load(open('model.pickle', 'rb'))


# Get public keys 
public_key = '194DYG3yLlLALXtzL4XHYgLyV'
public_token = '1421108778842349570-4OM14pkDa47PXsP7TzSHMUfHqYQWjV'

credential_container = st.expander("Twitter API Credentials", expanded=True)

with credential_container:
     # If valid credentials haven't been given, ask for credentials input ]
     private_key = st.text_input('Enter Private Key:', st.session_state.private_key, type='password')
     private_token = st.text_input('Enter Private Token:', st.session_state.private_token, type='password')

     # Check credentials
     if st.button("Submit"):
          # If credential are verified, cache in session state and disable credential UI to prevent valid credentials from being overwritten 
          try:
               auth = tweepy.OAuthHandler(public_key, private_key)
               auth.set_access_token(public_token, private_token)
               api = tweepy.API(auth, wait_on_rate_limit=True)
               api.verify_credentials()
               
               st.session_state.private_key = private_key
               st.session_state.private_token = private_token

               st.session_state.is_credential = True

          # If credentials don't work, ask to resubmit
          except:
               st.markdown("Bad credentials... Please try again!")
               st.session_state.is_credential = False

# If valid credentials have already been given, proceed
if st.session_state.is_credential:
     # Give confirmation in credential container
     credential_container.markdown("Credentials successfully verified!")
     
     # Fire up the Twitter API with given credentials 
     auth = tweepy.OAuthHandler(public_key, st.session_state.private_key)
     auth.set_access_token(public_token, st.session_state.private_token)
     api = tweepy.API(auth, wait_on_rate_limit=True)
     
     # Input for Tweet URL 
     url = st.text_input('Enter URL:', '')

     # Use Twitter API to extract text of tweet from URL 
     if st.button("Fetch Tweet"):
          
          try:
               # Standardize URL
               tweet_url = api.get_oembed(url)['url']

               # Extract Tweet ID from URL
               tweet_id = tweet_url.split('/status/')[1]

               # Extract text
               tweet_text = api.get_status(tweet_id).text

               # Cache in session state
               st.session_state.tweet_text = tweet_text
          except:
               st.markdown("Invalid URL... Please try again!")
          
     # Display tweet and/or manually enter tweet
     text = st.text_area('Tweet:', st.session_state.tweet_text, max_chars=280)
     
     # Cache tweet text input in session state
     st.session_state.tweet_text = text

     if st.button('Classify Tweet'):
          pred = clf.predict_proba([st.session_state.tweet_text])[0]
          plt.ylim(0,1)
          plt.xticks(ticks=[0, 1], labels=["Not Hate", "Hate"])
          plt.text(0, pred[0], pred[0], ha='center')
          plt.text(1, pred[1], pred[1], ha='center')
          fig = plt.bar(x=[0, 1], height=pred, color=['#75C29C', '#EE6666'])
          st.pyplot(fig)
    
