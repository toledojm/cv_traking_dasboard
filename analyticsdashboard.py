import cv2
import streamlit as st
import pandas as pd
import torch
import time
from detect_and_track import *


    

st.title("Analytics")
inference_msg = st.empty()
st.sidebar.title("Configurations")
input_source = st.sidebar.radio("Select input source",('Local video','None'))
### Video module


if input_source == "Local video":
    video = st.sidebar.file_uploader("Select input video", 
                    type=["mp4", "avi","mov"], accept_multiple_files=False)
    if video != None:
        imgpath = os.path.join(video.name)
        outputpath = os.path.join('/runs/detect/'+os.path.basename(imgpath))
        with open(imgpath, mode='wb') as f:
            f.write(video.read())

    if st.sidebar.button("StartDetection"):
        stframe = st.empty()
        
        col1, col2=st.columns(2)

        with col1:
        
            st.markdown("**Detección en el Frame Acual**")
            kpi1_text = st.markdown("0")
        
        with col2:
            st.markdown("**Total Acumulado**")
            kpi2_text = st.markdown("0")
        
        detect(
            source=imgpath, 
            stframe=stframe, 
            kpi1_text=kpi1_text,
            kpi2_text=kpi2_text
            )

        

   