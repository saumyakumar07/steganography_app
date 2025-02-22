from flask import Flask, render_template, request, send_file
from PIL import Image
import os

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to hide message in image
def hide_message(image_path, message, output_path):
    image = Image.open(image_path)
    encoded = image.copy()
    
    message += "###"  # Delimiter to mark end of message
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    
    pixels = list(encoded.getdata())
    new_pixels = []
    msg_index = 0
    
    for pixel in pixels:
        new_pixel = list(pixel)
        for i in range(3):  # Modify RGB channels
            if msg_index < len(binary_message):
                new_pixel[i] = new_pixel[i] & ~1 | int(binary_message[msg_index])
                msg_index += 1
        new_pixels.append(tuple(new_pixel))
    
    encoded.putdata(new_pixels)
    encoded.save(output_path)
    return output_path

# Function to extract hidden message
def extract_message(image_path):
    image = Image.open(image_path)
    pixels = list(image.getdata())
    
    binary_message = ""
    for pixel in pixels:
        for i in range(3):  # Extract from RGB channels
            binary_message += str(pixel[i] & 1)
    
    message = ""
    for i in range(0, len(binary_message), 8):
        char = chr(int(binary_message[i:i+8], 2))
        if message[-3:] == "###":
            break
        message += char
    
    return message[:-3]  # Remove delimiter

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hide', methods=['POST'])
def hide():
    image = request.files['image']
    message = request.form['message']
    if image and message:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], "encoded_" + image.filename)
        image.save(image_path)
        encoded_image = hide_message(image_path, message, output_path)
        return send_file(encoded_image, as_attachment=True)
    return "Error: Upload an image and enter a message"

@app.route('/extract', methods=['POST'])
def extract():
    image = request.files['image']
    if image:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        image.save(image_path)
        hidden_message = extract_message(image_path)
        return f"Extracted Message: {hidden_message}"
    return "Error: Upload an image"

if __name__ == '__main__':
    app.run(debug=True)
