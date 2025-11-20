import os
import math

def shannon_entropy(path):
    with open(path, "rb") as f:
        data = f.read()

    if not data:
        return 0.0

    freq = {}
    for b in data:
        freq[b] = freq.get(b, 0) + 1

    entropy = 0.0
    length = len(data)

    for count in freq.values():
        p = count / length
        entropy -= p * math.log2(p)

    return entropy


def file_tail_hex(path, n=64):
    with open(path, "rb") as f:
        f.seek(0, os.SEEK_END)
        size = f.tell()
        f.seek(max(size - n, 0))
        return f.read(n).hex()


def file_size(path):
    return os.path.getsize(path)