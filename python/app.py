import requests
import time

time.sleep(5)
r = requests.get("http://nginx")
print(r.status_code)
print(r.text)