import streamlit as st
import pandas as pd
import tweepy


"""
# MY APP

This is my app. Yay! 

## FAQ
1. How does it work? 
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


# Get public keys 
public_key = '194DYG3yLlLALXtzL4XHYgLyV'
public_token = '1421108778842349570-4OM14pkDa47PXsP7TzSHMUfHqYQWjV'

# If valid credentials haven't been given, ask for credentials input 
if not st.session_state.is_credential:
     # Input for typing in credentials 
     private_key = st.text_input('Enter Private Key:', st.session_state.private_key, type='password', disabled=st.session_state.is_credential)
     private_token = st.text_input('Enter Private Access Token:', st.session_state.private_key, type='password', disabled=st.session_state.is_credential)
     
     # Check credentials
     if st.button("Submit", disabled=st.session_state.is_credential):
          # If credential are verified, cache in session state and disable credential UI to prevent valid credentials from being overwritten 
          try:
               auth = tweepy.OAuthHandler(public_key, private_key)
               auth.set_access_token(public_token, private_token)
               api = tweepy.API(auth, wait_on_rate_limit=True)
               api.verify_credentials()

               st.session_state.is_credential = True
               st.session_state.private_key = private_key
               st.session_state.private_token = private_token
               
               # refresh app so that credentials UI is disabled
               st.experimental_rerun()
               
          # If credentials don't work, ask to resubmit
          except:
               st.markdown("Bad credentials... Please try again!")  

# If valid credentials have already been given, proceed
if st.session_state.is_credential:
     # Fire up the Twitter API with given credentials 
     auth = tweepy.OAuthHandler(public_key, st.session_state.private_key)
     auth.set_access_token(public_token, st.session_state.private_token)
     api = tweepy.API(auth, wait_on_rate_limit=True)
     st.markdown("Credentials successfully verified!")
     
     # Input for Tweet URL 
     url = st.text_input('Enter URL:', '')

     # Use Twitter API to extract text of tweet from URL 
     if st.button("Fetch Tweet"):
          # Standardize URL
          tweet_url = api.get_oembed(url)['url']

          # Extract Tweet ID from URL
          tweet_id = tweet_url.split('/status/')[1]

          # Extract text
          tweet_text = api.get_status(tweet_id).text
          
          # Cache in session state
          st.session_state.tweet_text = tweet_text
          

     # Display tweet and/or manually enter tweet
     text = st.text_area('Tweet:', st.session_state.tweet_text, max_chars=280)
     
     # Cache tweet text input in session state
     st.session_state.tweet_text = text

     if st.button('Classify Tweet'):
          st.write('test:', st.session_state.init_text)
     
       



"""

url = https://twitter.com/KimKardashian/status/1489401564284346369?s=20&t=nMf-OpIe73e8Gvnh--9kPA

"""
    
