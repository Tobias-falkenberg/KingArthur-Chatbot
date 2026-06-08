# test_no_proxy.py

import requests

s = requests.Session()
s.trust_env = False

r = s.get("http://localhost:11434/api/tags")

print(r.status_code)
print(r.text[:100])