import requests
r=requests.get("http://127.0.0.1:8000/media/documents/proxies.txt")
open('google.txt', 'w').write(r.text)
