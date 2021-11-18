import os
import sys
import time

path = sys.argv[1]


def details(path):
    data = []
    for i in os.listdir(path):
        a = os.stat(os.path.join(path, i))
        data.append([i, len(i), time.ctime(a.st_mtime)])
    print(data)


details(path)
