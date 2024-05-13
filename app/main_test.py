import streamlit as st
from datetime import datetime
import utils

from converter import convert_video

st.set_page_config(layout="wide")

col1, col2, col3 = st.columns(3)

def btn1_callback():
    st.session_state.myvalue = "Hello world!"

def btn2_callback():
    st.session_state.myvalue = "world Hellow"

def text_input_callback():
    print("wow")





with col1:
    st.text_input("myvalue", "Hello!", key="myvalue", on_change=text_input_callback)

with col2:
    st.button("btn1", on_click=btn1_callback)

with col3:
    st.button("btn2", on_click=btn2_callback)

if "myvalue" in st.session_state:
    st.write(st.session_state.myvalue)