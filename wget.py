from urllib.request import urlopen
import sys

url = sys.argv[1]


def basename(url):
    if url == '/':
        return 'index.html'
    else:
        return url.split('/')[-1]


def save(url):
    bs = basename(url)
    print(bs)
    response = urlopen(url)
    content = response.read()
    f = open(bs, 'w')
    f.write(str(content))
    f.close()


save(url)
