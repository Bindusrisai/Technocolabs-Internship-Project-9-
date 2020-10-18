import tensorflow as tf
model = tf.keras.models.load_model('my_model.hdf5')


import streamlit as st
st.write("""
          American  Sign language Recognition using Keras
         """
         )
st.write("This is a simple image classification web app to predict american sign letters!!")
file = st.file_uploader("Please upload an image file", type=["jpg", "png"])


import cv2
from PIL import Image, ImageOps
import numpy as np
def import_and_predict(image_data, model):
    
        size = (150,150)    
        image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        image = np.asarray(image)
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        img_resize = (cv2.resize(img, dsize=(75, 75),    interpolation=cv2.INTER_CUBIC))/255.
        
        img_reshape = img_resize[np.newaxis,...]
    
        prediction = model.predict(img_reshape)
        
        return prediction
if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    prediction = import_and_predict(image, model)
    
    if np.argmax(prediction) == 1:
        
        st.write("A")
    elif np.argmax(prediction) == 2:
        
        st.write("B")
    elif np.argmax(prediction) == 3:
        
        st.write("C")
    elif np.argmax(prediction) == 4:
        
        st.write("D")
    elif np.argmax(prediction) == 5:
        
        st.write("E")
    elif np.argmax(prediction) == 6:
        
        st.write("F")
        
    else:
        st.write("G")
    
    st.text("Probability (0: A, 1: B, 2: C")
    st.write(prediction)
