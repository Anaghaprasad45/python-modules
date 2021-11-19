import re


def make_slug(string):
    a = re.sub(r'[\W_]+', '-', string)
    print(a)


make_slug('hello $ $ world')
