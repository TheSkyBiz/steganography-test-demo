# lsb_embed.py

from PIL import Image
import numpy as np

DELIMITER = "###END###"

def _to_bit_list(data_bytes):
    bits = []
    for b in data_bytes:
        bits.extend([(b >> i) & 1 for i in reversed(range(8))])
    return bits

def embed_message(input_path, output_path, message):
    message_full = message + DELIMITER
    message_bytes = message_full.encode("utf-8")
    message_bits = _to_bit_list(message_bytes)

    img = Image.open(input_path).convert("RGB")
    arr = np.array(img)

    h, w, _ = arr.shape
    capacity_bits = h * w * 3

    if len(message_bits) > capacity_bits:
        raise ValueError("Message is too large for this image.")

    flat = arr.flatten()

    for i, bit in enumerate(message_bits):
        # FIX: clear LSB with 0xFE & reapply bit safely inside uint8 range
        flat[i] = ((flat[i] & 0xFE) | bit) & 0xFF

    new_arr = flat.reshape(arr.shape)
    out_img = Image.fromarray(new_arr.astype('uint8'), 'RGB')
    out_img.save(output_path)

    return output_path