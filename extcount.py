import os, sys

path = sys.argv[1]

d = {}
ext = []


def extcount(path):
    for i in os.listdir(path):
        a = i.split('.')
        ext.append(a[1])
    for j, e in enumerate(ext):
        d.setdefault(e, []).append(j)
    for key, value in d.items():
        print(key, len(value))


extcount(path)
