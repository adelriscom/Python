import requests

miReq=requests.get("https://www.eltiempo.com/")

print(miReq.status_code)
print(miReq.headers)
print(miReq.text)