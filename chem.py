# -*- coding: utf-8 -*-
import os


def chem(inp: str) -> str:
    temp = 5*[""]
    i, j = 0, 0
    num = ""
    mark = False
    for i in range(len(inp)):
        # deal with the numbers
        if inp[i].isdigit():
            num += inp[i]
        else:
            # the numbers after an English alphabet should be a subscript
            if mark and 0 != len(num):
                # add "{}" to long numbers
                if len(num) > 1:
                    temp[j] += "_{" + num + "}"
                else:
                    temp[j] += "_" + num
            else:
                temp[j] += num
            num = ""

            # mark the English alphabet
            mark = inp[i].isalpha() or (inp[i] in ")]")
            # deal with the "="
            if "=" == inp[i]:
                j += 1
                if j > 3:
                    break
                continue
            temp[j] += inp[i]
    # deal with the last part
    if mark and 0 != len(num):
        if len(num) > 1:
            temp[j] += "_{" + num + "}"
        else:
            temp[j] += "_"+num
    else:
        temp[j] += num
    # output
    if 0 == j:
        return temp[0]
    elif 1 == j:
        return temp[0] + "=" + temp[1]
    elif 2 == j:
        return temp[0] + "\\frac{\\underline{" + temp[1] + "}}{\\ }" + temp[2]
    elif 3 == j:
        return temp[0] + "\\frac{\\underline{" + temp[1] + "}}{" + temp[2] + "}"\
                       + temp[3]
    else:
        return "Error! There seems more then 3\"=\" !"


while True:
    inp = input("input:")
    outp = chem(inp)
    print("output:" + outp)
    os.system(r"powershell echo \"" + outp + r"\"|clip")  # paste to clipboard
    print("已复制到剪贴板")
    print()
