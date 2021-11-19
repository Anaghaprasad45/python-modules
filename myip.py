import json
from urllib.request import urlopen

f = urlopen('http://httpbin.org/get').read()

ip = json.loads(f)
print(ip['origin'])
