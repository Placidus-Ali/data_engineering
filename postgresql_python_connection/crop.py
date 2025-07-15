# Import Libraries
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import json
print('Libraries Imported Successfully')

# Load model
interpreter = tf.lite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()
print('Model Loaded Successfully')

# Load class labels and treatment dictionary
with open("class_mapping.json", "r") as f:
    class_mapping = json.load(f)

with open("treatment_dict.json", "r") as f:
    treatment_dict = json.load(f)
print('Class Labels and Treatment Dictionary Loaded Successfully')

# Get input and output tensor details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
print('Input and Output Sensor Set Successfully')

# Image preprocessing
def preprocess_image(image):
    image = image.resize((224, 224))  # Resize to expected input size
    image = np.array(image).astype(np.float32) / 255.0  # Normalize to 0-1
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image
print('Image Processed Successfully')

# Predict function
def predict(image):
    input_data = preprocess_image(image)
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    predicted_index = np.argmax(output_data)
    predicted_class = class_mapping[str(predicted_index)]
    treatment = treatment_dict.get(predicted_class, "No treatment info available.")
    return predicted_class, treatment
print('Predict Function Set Successfully')

# Streamlit UI
st.title("Crop Disease Detector")
st.write("Upload a leaf image to detect disease and get treatment recommendation")
print('Streamlit Title Set Successfully')

uploaded_file = st.file_uploader("Upload Leaf Image", type=["jpg", "jpeg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Leaf Image", use_column_width=True)

    predicted_class, treatment = predict(image)

    st.success(f"Predicted Disease: **{predicted_class}**")
    st.info(f"Recommended Treatment: {treatment}")
print('Deployment Done Successfully')



# PyInstaller to convert the entire app into a single .exe file.

# ✅ Step-by-Step Guide to Create the Offline App
# 🧱 Step 1: Folder Structure
#bash
#crop_disease_app/
#│
#├── app.py
#├── model.tflite
#├── class_mapping.json
#├── treatment_dict.json
#└── requirements.txt     

# 🔧 Step 2: Install Required Tools
# Do this only once on your own laptop (with internet).
# bash
# pip install pyinstaller streamlit tensorflow pillow

# 🧩 Step 3: Create a Simple Launcher Script (Optional)
# Create run.py as an entry point to avoid CLI:

# python
# import os
# os.system("streamlit run app.py")

# 🛠️ Step 4: Build the .exe File
# In your terminal, run:

# bash
# pyinstaller --noconfirm --onefile --windowed --icon=icon.ico run.py
# --onefile → All files bundled into a single .exe

# --windowed → Prevent command window from showing

# --icon=icon.ico → Optional icon

# After building, go to:

# arduino
# dist/run.exe
# ✅ This is the file you’ll send to others. Rename it to something like Crop_Disease_Detector.exe.

# 📁 Step 5: Package the App Folder
# Create a folder like this:

# pgsql
# CropDiseaseApp_Package/
# │
# ├── Crop_Disease_Detector.exe
# ├── model.tflite
# ├── class_mapping.json
# ├── treatment_dict.json
# └── README.txt (Optional)

# 🔗 Step 6: Share via USB or Bluetooth
# Send the whole CropDiseaseApp_Package folder to users.

# They double-click the .exe to start the app.

# The app opens in a browser without needing internet.

# All files are loaded locally, and it just works.

# 🎁 Optional: Customize for Better UX
# Auto-fullscreen browser launch

# Add your logo and colors to the app

# Auto-close after use (kiosk style)

# ❗ Notes
# This works best on Windows (especially .exe packaging).

# For Mac/Linux, the user must have Python + Streamlit installed — unless you build native versions.

# The .exe might trigger antivirus on some machines the first time — just inform users it’s safe.
