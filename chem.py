# -*- coding: utf-8 -*-

def chem(inp:str):
    temp = 4*[""];
    i,j = 0,0;
    num = "";
    mark = False;
    for i in range(len(inp)):
        if inp[i].isdigit():
            num+=inp[i];
        else:
            if mark and 0!=len(num):
                if len(num)>1:temp[j]+="_{"+num+"}";
                else:temp[j]+="_"+num;
            else:
                temp[j] += num;
            num = "";
            mark = inp[i].isalpha() or (inp[i] in ")]");
            if "="==inp[i]:
                j += 1;
                continue;
            temp[j]+=inp[i];
    if mark and 0!=len(num):
        if len(num)>1:temp[j]+="_{"+num+"}";
        else:temp[j]+="_"+num;
    else:
        temp[j] += num;
    if 0==j:return temp[0];
    if 1==j:return temp[0]+"="+temp[1];
    if 2==j:return temp[0]+"\\frac{\\underline{"+temp[1]+"}}{\\ }"+temp[2];
    if 3==j:return temp[0]+"\\frac{\\underline{"+temp[1]+"}}{"+temp[2]+"}"+temp[3];

    #for i in temp:print(i)

a=chem("CH3COOH+C2H5OH=\\Delta=H2O+CH3COOC2H5");
print(a);
