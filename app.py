import streamlit as st
import pickle
import pandas as pd

# Load the model
try:
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("❌ model.pkl not found. Please make sure it's in the same directory as app.py.")
    st.stop()

# Define the prediction function
def predict_price(input_data):
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)
    return prediction[0]

# Set page config
st.set_page_config(page_title="Smartphone Price Predictor", layout="centered")

# Display banner image and title
st.image("smartphones_image.jpg", use_container_width=True)
st.markdown("## 📱 Smartphone Price Prediction")
st.markdown("Estimate the price of a smartphone based on its features.")

# Sidebar for inputs
st.sidebar.header("🔧 Input Features")

five_g = st.sidebar.selectbox('5G Support', options=[0, 1], index=0)
ram = st.sidebar.slider('RAM (GB)', min_value=1, max_value=12, value=4)
rom = st.sidebar.slider('ROM (GB)', min_value=16, max_value=512, value=64, step=16)
front_camera = st.sidebar.slider('Front Camera (MP)', min_value=0, max_value=64, value=8)
back_camera_sum = st.sidebar.slider('Back Camera Total (MP)', min_value=0, max_value=200, value=13)

brand_name = st.sidebar.selectbox('Brand Name', options=[
    'Apple', 'Google', 'Infinix', 'Motorola', 'OPPO', 'OnePlus', 'Others',
    'POCO', 'REDMI', 'Samsung', 'realme', 'vivo'
])

# Processor options based on brand
if brand_name == 'Apple':
    processor_options = ['Bionic']
elif brand_name in ['Samsung', 'Google', 'Motorola', 'OPPO', 'OnePlus', 'Infinix', 'POCO', 'REDMI', 'realme', 'vivo']:
    processor_options = ['Mediatek', 'Others', 'Snapdragon']
else:
    processor_options = ['Others']

processor_name = st.sidebar.selectbox('Processor Name', options=processor_options)

# Input dictionary
input_data = {
    '5G': five_g,
    'RAM': ram,
    'ROM': rom,
    'Front_camera': front_camera,
    'Back_camera_sum': back_camera_sum,
    'Brand_name_Apple': int(brand_name == 'Apple'),
    'Brand_name_Google': int(brand_name == 'Google'),
    'Brand_name_Infinix': int(brand_name == 'Infinix'),
    'Brand_name_Motorola': int(brand_name == 'Motorola'),
    'Brand_name_OPPO': int(brand_name == 'OPPO'),
    'Brand_name_OnePlus': int(brand_name == 'OnePlus'),
    'Brand_name_Others': int(brand_name == 'Others'),
    'Brand_name_POCO': int(brand_name == 'POCO'),
    'Brand_name_REDMI': int(brand_name == 'REDMI'),
    'Brand_name_Samsung': int(brand_name == 'Samsung'),
    'Brand_name_realme': int(brand_name == 'realme'),
    'Brand_name_vivo': int(brand_name == 'vivo'),
    'Processor_name_Bionic': int(processor_name == 'Bionic'),
    'Processor_name_Mediatek': int(processor_name == 'Mediatek'),
    'Processor_name_Others': int(processor_name == 'Others'),
    'Processor_name_Snapdragon': int(processor_name == 'Snapdragon')
}

# Prediction button
if st.button('🔍 Predict Price'):
    predicted_price = predict_price(input_data)
    st.success(f"💰 Estimated Price: ₹{predicted_price:,.2f}")
