import sys
import zipfile

name = sys.argv[1]
zipname = zipfile.ZipFile(name, 'w')

for i in sys.argv[2:]:
    zipname.write(i)


