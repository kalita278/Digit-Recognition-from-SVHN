import tensorflow as tf
import numpy as np
import streamlit as st
import pandas as pd
from io import StringIO
from keras.preprocessing import image
from PIL import Image, ImageOps


loaded_model = tf.keras.models.load_model('Model/model4_svhn.hdf5')


def pred(input_image):
    #data = np.ndarray(shape=(1, 32, 32, 1), dtype=np.float32)
    z =ImageOps.fit(input_image,(32,32))
    z = np.expand_dims(z,axis=3)
    z_arr=np.asarray(z)
    z_arr = z_arr.astype(np.float32)/255.0
    #z_dim=np.expand_dims(z_arr,axis=0)
    #z_dim = z_arr.resize((32,32,1))
    #data[0]=z_arr
    prob = loaded_model.predict(z_arr)
    pred = np.argmax(prob,axis=1)
    return pred
    
        
def main():
    st.title('SVHN Recognition')
    uploaded_file = st.file_uploader("Choose a file:")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image,caption='Uploaded File',use_column_width=True)
        
        predict = ' '
        
        if st.button('Predict'):
            predict = pred(image)
            
        st.success(predict)
        
if __name__ == '__main__':
    main()  