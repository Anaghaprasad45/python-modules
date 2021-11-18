import re


def isValid(n):
    Pattern = re.compile("^[6-9]\d{9}$")
    return Pattern.match(n)


n = "9207750878"
if isValid(n):
    print("Valid Number")
else:
    print("Invalid Number")
