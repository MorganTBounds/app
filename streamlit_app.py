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

if option == 'URL (requires credentials)':
     
     public_key = '194DYG3yLlLALXtzL4XHYgLyV'
     public_token = '1421108778842349570-4OM14pkDa47PXsP7TzSHMUfHqYQWjV'
     
     """
     #### Please Enter Twitter API Credentials
     """
     
     is_credentials = False
     
     private_key = st.text_input('Enter Private Key:', '', type='password', disabled=is_credentials)
     private_token = st.text_input('Enter Private Access Toekn:', '', type='password', disabled=is_credentials)
     
     if st.button('Submit'):
          
          # fire up the Twitter API using Tweepy 
          auth = tweepy.OAuthHandler(public_key, private_key)
          auth.set_access_token(public_token, private_token)
          api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
     
          is_credentials = api.verify_credentials()
          
          if is_credentials:
               st.markdown("<font color='green'> Login Successful! </font>")
          else:
               st.markdown("<font color='red'> Login failed... Please re-enter credentials. </font>")


if option == 'Copy & Paste':
     
     txt = st.text_area('Copy and Paste Tweet Below:', '''
          Lorem ipsum lorem ipsum lorem ipsum... 
          ''', max_chars=280)
    
st.write('Sentiment:', 'sentiment here...')
