import sys

file = sys.argv[1] if len(sys.argv) > 1 else "/dev/stdin"

with open(file, 'r') as f:
    lines = f.read()
    print(lines)

#for line in sys.stdin.readline():
#    print("".join([chr(ord(el) - idx) for idx, el in enumerate("abcd")]))
