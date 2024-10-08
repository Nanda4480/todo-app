import streamlit as st
from PIL import Image

with st.expander("Start camera"):
    #Start the camera
    camera_image = st.camera_input("camera")

if camera_image:

    #Create a pillow image instance
    img = Image.open(camera_image)

    #Convert the pillow image to grayscale
    gray_img = img.convert("L")

    #display the grayscale image on webpage
    st.image(gray_img, caption="Gray Image")

