# LSB Image Steganography Demo

This project demonstrates a simple and safe **Least Significant Bit (LSB)** steganography technique using Python.  
It hides a text message inside an image and then extracts it back, along with basic steganalysis.

## 📁 Project Structure
steganography_demo/
│
├── main.py
├── lsb_embed.py
├── lsb_extract.py
├── utils.py
│
├── assets/
│ ├── input_image.png # Add your own image here
│ ├── output_stego.png # Generated after embedding
│ └── extracted_message.txt # Generated after extraction

## 🚀 How to Run
1. Add an image inside `assets/` named `input_image.png`
2. Run:

python main.py

markdown
Copy code

3. Output files generated:
- `assets/output_stego.png`
- `assets/extracted_message.txt`

## 🧠 Features
- Hide text inside an image using LSB (RGB channels)
- Extract hidden text from the stego image
- File size comparison (original vs stego)
- Shannon entropy comparison (basic steganalysis)
- Hex-tail comparison to visualize byte changes

## ⚠️ Notes
- Avoid JPEG for embedding — always use PNG to prevent data loss.
- LSB steganography is simple and easily detectable (purpose is educational).

## 📜 License
This project is for academic and ethical cybersecurity learning.