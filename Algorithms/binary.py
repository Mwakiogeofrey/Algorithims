import requests

# URL of the TFLite model (replace with RAW GitHub URL)
url = "https://raw.githubusercontent.com/Gourav9165/crop_disease_detection_model/main/detection/model.tflite"
file_path = "model.tflite"  # Save it locally

# Download the file
response = requests.get(url)

if response.status_code == 200:
    with open(file_path, "wb") as file:
        file.write(response.content)
    print(f"✅ Downloaded successfully: {file_path}")
else:
    print(f"❌ Failed to download. Status code: {response.status_code}")

import tensorflow as tf

# Load the TFLite model
interpreter = tf.lite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()

# Print model input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

print("📌 Model Input Details:", input_details)
print("📌 Model Output Details:", output_details)
