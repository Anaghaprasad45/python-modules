import sys
from inspect import *


module = sys.argv[1]
p = __import__(module)
print(p.__doc__)
print(dir(module))
for i in getmembers(p, predicate=lambda x: isfunction(x)):
    print(i[0])
