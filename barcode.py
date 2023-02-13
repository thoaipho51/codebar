import time
import numpy as np
from pyzbar.pyzbar import decode
import streamlit as st
from PIL import Image
import io

# camera = True
list_code = []
list_product = []



def write_f(list_product):
    # Mở một tệp txt để ghi dữ liệu
    with open("products.txt", "a", encoding='utf-8') as file:
        for product in list_product:
            # Ghi từng dòng vào tệp txt
            file.write(f"{product['code']} - {product['name']} - {product['price']}\n")

def write_f(product):
    # Mở một tệp txt để ghi dữ liệu
    with open("products.txt", "a", encoding='utf-8') as file:
        # Ghi từng dòng vào tệp txt
        file.write(f"{product['code']} - {product['name']} - {product['price']}\n")


# # Vòng white
# while camera:

with open("products.txt", "r", encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        barcode = line.split(' - ')[0]
        if barcode not in list_code:
            list_code.append(barcode)

# print(list_code) # Danh sách mã barcode
# frame = video.read()

img = st.camera_input("Take a picture")
if img is not None:
    
    # decode hình ảnh sang chuỗi nhị phân để xử lý
    bytes_data = img.getvalue()
    img = Image.open(io.BytesIO(bytes_data))

    for code in decode(img):
        if code.data.decode('utf-8') not in list_code:
            name = st.text_input("Nhập tên sản phẩm")
            price = st.text_input("Nhập giá sản phẩm")
            if st.button("Nhập Dữ Liệu"):
                product = {
                    'code': code.data.decode('utf-8'),
                    'name': name,
                    'price': price
                }
                st.write(f'Nhập code : {code.data.decode("utf-8")} Thành Công ! - {name}')
                write_f(product)

        else:
            st.write(f'Mã Code : {code.data.decode("utf-8")}')
            with open("products.txt", "r", encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines:
                    barcode = line.split(' - ')[0]
                    name = line.split(' - ')[1]
                    price = line.split(' - ')[2]
                    if barcode == code.data.decode('utf-8'):
                        st.write(f"Tên: {name} Giá: {price}")
        