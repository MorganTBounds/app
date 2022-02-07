import streamlit as st
import pandas as pd
import tweepy


"""
# MY APP

This is my app. Yay! 

## FAQ
1. How does it work? 
"""

with st.form("credentials"):
     public_key = '194DYG3yLlLALXtzL4XHYgLyV'
     public_token = '1421108778842349570-4OM14pkDa47PXsP7TzSHMUfHqYQWjV'
     private_key = st.text_input('Enter Private Key:', '', type='password')
     private_token = st.text_input('Enter Private Access Token:', '', type='password')

     # fire up the Twitter API using Tweepy 
     auth = tweepy.OAuthHandler(public_key, private_key)
     auth.set_access_token(public_token, private_token)
     api = tweepy.API(auth, wait_on_rate_limit=True)

     # Every form must have a submit button.
     if st.form_submit_button("Submit"):
          try:
               api.verify_credentials()
               st.markdown("Credentials successfully verified!")

          except:
               st.markdown("Bad credentials... Please try again!")  
               
url_container = st.container()

text = st.text_area('Tweet:', '', max_chars=280)
               
url = url_container.text_input('Enter URL:', '')

if url_container.button("Fetch Tweet"):
     # Standardize URL
     tweet_url = api.get_oembed(url)['url']

     # Extract Tweet ID from URL
     tweet_id = tweet_url.split('/status/')[1]

     # Extract text
     fetch_text = api.get_status(tweet_id).text
     
     # Display text
     text.value = fetch_text
     

          

"""

url = https://twitter.com/KimKardashian/status/1489401564284346369?s=20&t=nMf-OpIe73e8Gvnh--9kPA

"""
    
