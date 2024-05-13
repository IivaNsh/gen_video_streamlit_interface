import streamlit as st
from datetime import datetime
import utils

from converter import convert_video

st.set_page_config(layout="wide")

time_start = 0



# choose file section

video_file = st.file_uploader(label="Choose a video", type=["mp4"], key="video_file")
pgn_file = st.file_uploader(label="Choose a PGN", type=["pgn"], key="pgn_file")



# choose action section

def btn1_callback():
    #check for file presence
    pass


btn1 = st.button("Make interesting video", on_click=btn1_callback)

btn2 = st.button("Get if game is intersing")

btn3 = st.button("Get interesting moments") 



if btn1:

    # check for file presence
    if True:
        
        # video = video_file.read()
        # st.video(video)

        st.session_state.time_str = ""

        st.text_input("Chose time when fist move occured (HH : MM : SS)", key="time_str") # здесь при нажатии enter пропадает все (((((
        if st.session_state.time_str != "":
            time = utils.get_sec(st.session_state.time_str)
            st.write("time stemp = ", time)

            #video_file_converted = convert_video(video, pgn_file)
            # show video file
            #st.video(video_file_converted)
        

            now = datetime.now()
            date_time = now.strftime("%m-%d-%Y-%H-%M-%S")
            file_name = date_time    
        
            #   download video file
            #st.download_button(label="Download", data=video_file_converted, file_name=file_name)
    else:
        st.error("choose video & pgn")


if btn2:

    # check for file presence
    if (pgn_file != None):
        
        # TODO: check if game is interesting

        st.text("NO")
    
    else:
        st.error("choose pgn file")



if btn3:
    
    # check for file presence
    if (pgn_file != None):
        # TODO: choose format for interesting moments
        
        # TODO: get interesting moments

        # TODO: return and show interesting moments
        st.text("some intersgin moments as an array(?) or may be interative table")

    else:
        st.error("choose pgn file")