# -*- coding: utf-8 -*-

def chem(inp:str)->str:
    temp = 5*[""];
    i,j = 0,0;
    num = "";
    mark = False;
    for i in range(len(inp)):
        #deal with the numbers
        if inp[i].isdigit():
            num+=inp[i];
        else:
            if mark and 0!=len(num):#the numbers after an English alphabet should be a subscript
                if len(num)>1:temp[j]+="_{"+num+"}";#add "{}" to long numbers
                else:temp[j]+="_"+num;
            else:
                temp[j] += num;
            num = "";

            mark = inp[i].isalpha() or (inp[i] in ")]");#mark the English alphabet
            #deal with the "="
            if "="==inp[i]:
                j += 1;
                if j>3:break;
                continue;
            temp[j]+=inp[i];
    #deal with the last part
    if mark and 0!=len(num):
        if len(num)>1:temp[j]+="_{"+num+"}";
        else:temp[j]+="_"+num;
    else:
        temp[j] += num;
    #output
    if 0==j:return temp[0];
    elif 1==j:return temp[0]+"="+temp[1];
    elif 2==j:return temp[0]+"\\frac{\\underline{"+temp[1]+"}}{\\ }"+temp[2];
    elif 3==j:return temp[0]+"\\frac{\\underline{"+temp[1]+"}}{"+temp[2]+"}"+temp[3];
    else:return "Error! There seems more then 3\"=\" !";


while True:
    inp = input("input:");
    print("output:"+chem(inp));
    print();
