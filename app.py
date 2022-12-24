import qrcode
import streamlit as st
from io import BytesIO


#Sembunyikan hamburger menu di pojok kanan atas dan footer
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


st.title("QR Code Generator")
data = st.text_input("Masukkan Teks Yang Akan Digenerate")
generate_button = st.button("Generate")


if generate_button:
# Generate QR code object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )


    qr.add_data(data)
    qr.make(fit=True)

    # Create image from QR code object
    img = qr.make_image(fill_color="black", back_color="white")

    img_binary = BytesIO()
    img.save(img_binary, format="PNG")
    img_binary.seek(0)
    st.image(img_binary)

    byte_im = img_binary.getvalue()

    st.download_button(
      label="Download Image",
      data=byte_im,
      file_name=data+".png",
      mime="image/jpeg",
      )
