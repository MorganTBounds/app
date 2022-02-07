import streamlit as st
import pandas as pd
import tweepy


"""
# MY APP

This is my app. Yay! 

## FAQ
1. How does it work? 
"""
if 'is_credential' not in st.session_state:
     st.session_state.is_credential = False
     
if 'private_key' not in st.session_state:
     st.session_state.private_key = ''
     
if 'private_token' not in st.session_state:
     st.session_state.private_token = ''
     
with st.form('credentials'):
     public_key = '194DYG3yLlLALXtzL4XHYgLyV'
     public_token = '1421108778842349570-4OM14pkDa47PXsP7TzSHMUfHqYQWjV'
     
     key_container = st.empty()
     token_container = st.empty()
     
     if st.session_state.private_key == '':
          private_key = key_container.text_input('Enter Private Key:', '', type='password')
          private_token = token_container.text_input('Enter Private Access Token:', '', type='password')

          # Every form must have a submit button.
          if st.form_submit_button("Submit"):
               try:
                    # fire up the Twitter API using Tweepy 
                    auth = tweepy.OAuthHandler(public_key, private_key)
                    auth.set_access_token(public_token, private_token)
                    api = tweepy.API(auth, wait_on_rate_limit=True)
                    api.verify_credentials()

                    key_container.empty()
                    token_container.empty()
                    st.session_state.private_key = private_key
                    st.session_state.private_token= private_token         
                    st.markdown("Credentials successfully verified!")

               except:
                    st.markdown("Bad credentials... Please try again!")  
     else:
          auth = tweepy.OAuthHandler(public_key, private_key)
          auth.set_access_token(public_token, private_token)
          api = tweepy.API(auth, wait_on_rate_limit=True)
          st.markdown("Credentials successfully verified!")
               


url = st.text_input('Enter URL:', '')

is_disabled = True

if st.button("Fetch Tweet"):
     # Standardize URL
     tweet_url = api.get_oembed(url)['url']

     # Extract Tweet ID from URL
     tweet_id = tweet_url.split('/status/')[1]

     # Extract text
     text = api.get_status(tweet_id).text
     
     # Display Text
     st.text_area('Tweet:', text, max_chars=280, disabled=True)
     
     is_disabled=False
     
if st.button('Classify Tweet', disabled=is_disabled):
     st.write('test:', text)

"""

url = https://twitter.com/KimKardashian/status/1489401564284346369?s=20&t=nMf-OpIe73e8Gvnh--9kPA

"""
    
