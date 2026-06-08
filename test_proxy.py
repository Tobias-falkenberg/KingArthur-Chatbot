# test_proxy.py

import os

print("HTTP_PROXY =", os.environ.get("HTTP_PROXY"))
print("HTTPS_PROXY =", os.environ.get("HTTPS_PROXY"))
print("http_proxy =", os.environ.get("http_proxy"))
print("https_proxy =", os.environ.get("https_proxy"))
print("ALL_PROXY =", os.environ.get("ALL_PROXY"))
print("NO_PROXY =", os.environ.get("NO_PROXY"))