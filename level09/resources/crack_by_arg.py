import sys

print("".join([chr(int(el, 16) - idx) for idx, el in enumerate(sys.argv[1])]))
