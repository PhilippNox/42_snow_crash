import sys

# xxd -p token | sed 's/../&_/g'
input = "66_34_6b_6d_6d_36_70_7c_3d_82_7f_70_82_6e_83_82_44_42_83_44_75_7b_7f_8c_89_0a_"

out = []
for idx, el in enumerate(input.split("_")[:-2]):
    print(f"{el} - {int(el, 16):3} : {idx:3} : {int(el, 16)-idx:3} - {chr(int(el, 16) - idx):3}")
    out.append(chr(int(el, 16) - idx))
print("".join(out))
