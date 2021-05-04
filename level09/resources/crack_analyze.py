import sys

out = []

for idx, el in enumerate(sys.argv[1].split()):
    print(f"{el} - {int(el, 16):3} : {idx:3} : {int(el, 16)-idx:3} - {chr(int(el, 16) - idx):3}")
    out.append(chr(int(el, 16) - idx))
print("".join(out))
