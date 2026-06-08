# test_httpx.py

import httpx

with httpx.Client(trust_env=False) as client:
    r = client.get("http://localhost:11434/api/tags")

print(r.status_code)