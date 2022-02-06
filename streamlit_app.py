import streamlit as st
import pandas as pd
import tweepy


"""
# MY APP

This is my app. Yay! 

## FAQ
1. How does it work? 
"""

option = st.selectbox(
     'Please select a method for loading Tweets:',
     (
          'URL (requires credentials)', 
          'Copy & Paste', 
          'Sample Tweets'
     )
)

is_credentials = False

if option == 'URL (requires credentials)':
     
     public_key = '194DYG3yLlLALXtzL4XHYgLyV'
     public_token = '1421108778842349570-4OM14pkDa47PXsP7TzSHMUfHqYQWjV'
     
     """
     #### Please Enter Twitter API Credentials
     """
     
     private_key = st.text_input('Enter Private Key:', '', type='password')
     private_token = st.text_input('Enter Private Access Toekn:', '', type='password')
     
     # fire up the Twitter API using Tweepy 
     auth = tweepy.OAuthHandler(public_key, private_key)
     auth.set_access_token(public_token, private_token)
     api = tweepy.API(auth, wait_on_rate_limit=True)
     
     if st.button('Submit'):
          
          try:
               is_credentials = api.verify_credentials()
               st.markdown("Credentials successfully verified!")
          except:
               st.markdown("Bad credentials... Please try again!")  
               
     if is_credentials:
          tweet_url = st.text_input('Enter URL:', '')


if option == 'Copy & Paste':
     
     txt = st.text_area('Copy and Paste Tweet Below:', '''
          Lorem ipsum lorem ipsum lorem ipsum... 
          ''', max_chars=280)
    
st.write('Sentiment:', 'sentiment here...')
