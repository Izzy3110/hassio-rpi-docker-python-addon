import os
import requests

# print(requests.__version__)
print(os.getenv('HASSIO_TOKEN', None))
resp = requests.get('https://ipv4.icanhazip.com/')
if resp.status_code == 200:
    print(resp.text.rstrip("\r\n"))
