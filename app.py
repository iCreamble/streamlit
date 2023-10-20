import streamlit as st
from PIL import ImageOps
from PIL import Image
st.write('Lembre que eu amo muito você!')
image = Image.open('IMG_3896.JPG')
image = ImageOps.exif_transpose(image)
st.image(image, 'nois')
