from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# MY APP

This is my app. Yay! 

## FAQ
1. How does it work? 
"""

txt = st.text_area('Copy and Paste Tweet Below:', '''
     Lorem ipsum lorem ipsum lorem ipsum... 
     ''', max_chars=280)
    
st.write('Sentiment:', txt)
