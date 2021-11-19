import tablib
import sys

csv_file = sys.argv[1]
excel_file = sys.argv[2]

with open(csv_file, 'r') as f:
    cs = f.read()
    data = tablib.Dataset()
    data.append(cs)
print(data)

with open(excel_file, 'wb') as f:
    f.write(data.export('xls'))
