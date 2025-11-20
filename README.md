# LSB Image Steganography Demo

This project demonstrates a simple and safe implementation of **Least Significant Bit (LSB)** image steganography using Python.  
The program embeds a text message inside an image and extracts it back, along with performing basic steganalysis.

---

## Project Structure
```
steganography_demo/
│
├── main.py               # Runs the full demo
├── lsb_embed.py          # LSB embedding logic
├── lsb_extract.py        # LSB extraction logic
├── utils.py              # Entropy, hex tail, and file utilities
│
└── assets/
    ├── input_image.png        # Provide your own image here
    ├── output_stego.png       # Generated after embedding
    └── extracted_message.txt  # Extracted secret message
```

---

## How to Run

### 1. Add an input image  
Place an image named **`input_image.png`** inside the `assets/` folder.  
Use **PNG** format for best results.

### 2. Run the script
```
python main.py
```

### 3. Output files generated
- `assets/output_stego.png` — image with hidden message  
- `assets/extracted_message.txt` — message extracted from the stego image  

---

## Features
- Embed a text message into an image using LSB (RGB channels)  
- Extract the hidden message from the modified image  
- Compare original vs stego image sizes  
- Compute Shannon entropy (basic steganalysis indicator)  
- Compare hex tail values to observe data modifications  

---

## Notes
- **Do not use JPEG** for embedding, as JPEG compression destroys pixel-level data.  
  Always use **PNG** or another lossless format.
- LSB steganography is **not secure** and is used here for educational purposes only.
- This project is safe and does not use any harmful or destructive techniques.

---

## License
This project is intended solely for academic and ethical cybersecurity learning.
