from io import BytesIO
import streamlit as st
from PIL import Image
from rembg import remove

st.set_page_config(layout="wide", page_title="Image Background Remover")
st.write("## Remove background from your image")

st.sidebar.write("## Upload and download :gear:")
col1, col2 = st.columns(2)

def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

def fix_image(upload):
    image = Image.open(upload)
    col1.write("Original Image :camera:")
    col1.image(image)
    
    fixed = remove(image)
    downloadable_image = convert_image(fixed)
    col2.write("Fixed Image :wrench:")
    col2.image(downloadable_image)
    st.sidebar.markdown("\n")
    st.sidebar.download_button(
        "Download fixed image", downloadable_image, "fixed.png", "image/png"
    )

my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg","jfif"])

if my_upload is not None:
    fix_image(upload=my_upload)
else:
    col1.write("Original Image :camera:")
    image = Image.open("pic.jpg")
    col1.image(image)
    
    col2.write("Fixed Image :wrench:")
    image1 = Image.open("pic_f.png")
    col2.image(image1)
