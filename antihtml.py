from urllib.request import urlopen
import re
import sys

url = sys.argv[1]

data = urlopen(url).read()


def strip(data):
    a = re.compile(r'<[^>]+>')
    p = a.sub('', str(data))
    print(p)


strip(data)