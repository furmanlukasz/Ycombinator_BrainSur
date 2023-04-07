import base64
import requests
import streamlit as st

# set page to wide mode and dark theme
st.set_page_config(layout="wide", page_title="BrainSur", page_icon=":brain:")

def add_bg_from_url(image_url):
    # Download the image from the URL
    response = requests.get(image_url)
    image_data = response.content

    # Encode the image data using base64
    encoded_string = base64.b64encode(image_data)

    # Set the background image using the encoded string
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
        unsafe_allow_html=True
    )

add_bg_from_url('https://i.ibb.co/w4M8rTh/macos-big-sur.jpg')
st.title("BrainSur :brain:")

# 3 buttons in a row
col1, col2, col3 = st.columns(3)

st.write("---")
st.write("---")
if col1.button("Gallery"):
    img1, img2, img3, img4 = st.columns(4)
    img1.image('https://i.ibb.co/z52MN1r/336521860-767667991223026-3716096178740033935-n.jpg')
    img2.image('https://i.ibb.co/59tmg47/336591774-935879294120196-1810085195217107535-n.jpg')
    img3.image('https://i.ibb.co/qRwBWK2/336595154-599597758427683-5319373594229108266-n.jpg')
    img4.image('https://i.ibb.co/0qjfybc/336617838-1928161714213923-3015425846256950520-n.jpg')

    img5, img6, img7, img8 = st.columns(4)
    img5.image('https://i.ibb.co/RgcCHFH/336619576-167900139406201-2150038040840111361-n.jpg')
    img6.image('https://i.ibb.co/wcyWrWm/336623287-158443167108591-5221780258192442617-n.jpg')
    img7.image('https://i.ibb.co/d43KhBT/336637396-6307110886039515-6517113633736493418-n.jpg')
    img8.image('https://i.ibb.co/3sNNWz3/336650437-222764600412548-4863298622138483421-n.jpg')

    img9, img10, img11, img12 = st.columns(4)
    img9.image('https://i.ibb.co/wWdLZDM/IMG-1397.jpg')
    img10.image('https://i.ibb.co/sHVLvJq/IMG-1399.jpg')
    img11.image('https://i.ibb.co/tcxzMtG/IMG-1401.jpg')
    img12.image('https://i.ibb.co/YDFd9ch/IMG-1403.jpg')

    img13, img14, img15, img16 = st.columns(4)
    img13.image('https://i.ibb.co/VvKg7BT/photo-2023-03-23-21-24-10.jpg')
    img14.image('https://i.ibb.co/ZYc9PXq/photo-2023-03-23-21-24-14.jpg')
    img15.image('https://i.ibb.co/j3twH41/photo-2023-03-23-21-24-17.jpg')
    img16.image('https://i.ibb.co/W2F8G16/photo-2023-03-23-21-24-19.jpg')


if col2.button("Movies"):

    st.video('https://youtu.be/RyNUUMeZgV0')
    st.video('https://youtu.be/c6yFWVkHYZk')
    st.video('https://youtu.be/GnWIMP4iLDU')

if col3.button("About"):
    st.video('https://youtu.be/z34Q0KDRwdk')

