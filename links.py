import sys
import re
from urllib.request import urlopen


def links(data):
    link = re.findall('://www.([\w\-.]+)', data)
    print(link)


url = sys.argv[1]
data = urlopen(url).read()
links(str(data))

