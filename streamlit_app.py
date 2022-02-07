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
     
if 'init_text' not in st.session_state:
     st.sesssion_state.init_text = ''


# Get public keys 
public_key = '194DYG3yLlLALXtzL4XHYgLyV'
public_token = '1421108778842349570-4OM14pkDa47PXsP7TzSHMUfHqYQWjV'

credential_container = st.empty()

if not st.session_state.is_credential:
     with credential_container.container():
          private_key = st.text_input('Enter Private Key:', '', type='password')
          private_token = st.text_input('Enter Private Access Token:', '', type='password')

          if st.button("Submit"):
               try:
                    # fire up the Twitter API using Tweepy 
                    auth = tweepy.OAuthHandler(public_key, private_key)
                    auth.set_access_token(public_token, private_token)
                    api = tweepy.API(auth, wait_on_rate_limit=True)
                    api.verify_credentials()

                    st.session_state.is_credential = True
                    st.session_state.private_key = private_key
                    st.session_state.private_token = private_token

                    credential_container.empty()

               except:
                    st.markdown("Bad credentials... Please try again!")  

if st.session_state.is_credential:
     auth = tweepy.OAuthHandler(public_key, st.session_state.private_key)
     auth.set_access_token(public_token, st.session_state.private_token)
     api = tweepy.API(auth, wait_on_rate_limit=True)
     st.markdown("Credentials successfully verified!")

     url = st.text_input('Enter URL:', '')
     
     def save_text(value):
          st.session_state.init_text = value

     if st.button("Fetch Tweet"):
          # Standardize URL
          tweet_url = api.get_oembed(url)['url']

          # Extract Tweet ID from URL
          tweet_id = tweet_url.split('/status/')[1]

          # Extract text
          tweet_text = api.get_status(tweet_id).text
          
          save_text(tweet_text)
          

     # Display Text
     text = st.text_area('Tweet:', st.session_state.init_text, max_chars=280, on_change=save_text, args=value)

     if st.button('Classify Tweet'):
          st.write('test:', st.session_state.init_text)
     
       



"""

url = https://twitter.com/KimKardashian/status/1489401564284346369?s=20&t=nMf-OpIe73e8Gvnh--9kPA

"""
    
