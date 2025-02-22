# Steganography Tool

## 📌 About the Project
This project is a **Steganography Tool** that allows users to hide secret messages inside images and extract them later.
It utilizes **LSB (Least Significant Bit) encoding** to embed text into images without visibly altering them.

## 🚀 Features
- **Encode a secret message** into an image.
- **Decode and retrieve** the hidden message from an encoded image.
- **User-friendly Interface** using Bootstrap.
- **Secure & Efficient** text hiding.
- **Responsive Design** for better user experience.

## 🛠️ Technologies Used
- **Python** (Flask for backend)
- **PIL (Pillow)** for image processing
- **HTML, CSS, Bootstrap** for frontend

## 📂 Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/steganography-tool.git
cd steganography-tool
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application
```bash
python app.py
```
The application will start running on `http://127.0.0.1:5000/`.

## 📷 How It Works
1. **Encoding:**
   - Upload an image.
   - Enter a secret message.
   - Click **Encode Message** to embed the text into the image.
   - Download the encoded image.

2. **Decoding:**
   - Upload the encoded image.
   - Click **Decode Message** to extract the hidden text.

## 🎯 Future Enhancements
- Add encryption for additional security.
- Support for more file formats.
- Improve UI with animations and better responsiveness.

## 🤝 Contribution
Feel free to fork this repository and submit pull requests! If you find any issues, report them in the **Issues** section.

## 📄 License
This project is licensed under the **MIT License**.


---
💡 *If you like this project, don't forget to ⭐ the repository!*
