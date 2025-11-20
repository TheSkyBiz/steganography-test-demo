from PIL import Image
import numpy as np

DELIMITER = "###END###"

def extract_message(stego_path):
    img = Image.open(stego_path).convert("RGB")
    arr = np.array(img)

    flat = arr.flatten()
    bits = [int(byte & 1) for byte in flat]

    extracted_bytes = bytearray()

    for i in range(0, len(bits), 8):
        chunk = bits[i:i+8]
        if len(chunk) < 8:
            break

        byte = 0
        for bit in chunk:
            byte = (byte << 1) | bit

        extracted_bytes.append(byte)

        text = extracted_bytes.decode("utf-8", errors="ignore")
        if DELIMITER in text:
            return text.split(DELIMITER)[0]

    return extracted_bytes.decode("utf-8", errors="ignore")