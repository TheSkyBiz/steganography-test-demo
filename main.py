from lsb_embed import embed_message
from lsb_extract import extract_message
from utils import shannon_entropy, file_tail_hex, file_size

INPUT_IMAGE = "assets/input_image.png"
STEGO_IMAGE = "assets/output_stego.png"
OUTPUT_MESSAGE_FILE = "assets/extracted_message.txt"

def main():
    secret = "This is a stegnastic demo by Aakash and team."

    print("Embedding secret message...")
    embed_message(INPUT_IMAGE, STEGO_IMAGE, secret)
    print(f"Stego image saved -> {STEGO_IMAGE}")

    print("\nExtracting message...")
    extracted = extract_message(STEGO_IMAGE)
    print("Extracted message:", extracted)

    with open(OUTPUT_MESSAGE_FILE, "w") as f:
        f.write(extracted)

    print(f"\nSaved extracted text -> {OUTPUT_MESSAGE_FILE}")

    print("\n--- Steganalysis ---")
    print("Original Size:", file_size(INPUT_IMAGE))
    print("Stego Size   :", file_size(STEGO_IMAGE))
    print("Original Entropy:", shannon_entropy(INPUT_IMAGE))
    print("Stego Entropy   :", shannon_entropy(STEGO_IMAGE))
    print("\nTail of Original:", file_tail_hex(INPUT_IMAGE))
    print("Tail of Stego   :", file_tail_hex(STEGO_IMAGE))

if __name__ == "__main__":
    main()
