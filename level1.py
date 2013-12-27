# solution 1
a =  "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
# a = 'map'
tmp = ''
b = ''
for i in a:
    if i.isalpha():
        if i == 'y':
            tmp = 'a'
        elif i == 'z':
            tmp = 'b'
        else:
            tmp = chr(ord(i) + 2)
    else:
        tmp = i 
    b += tmp
    # print(b)
print(b)
# solution 2
import string
table = a.maketrans(string.ascii_lowercase, \
        string.ascii_lowercase[2:]+string.ascii_lowercase[:2])
a.translate(table)

#solution 3
o=""
for x in a :
    if ord(x)>=ord('a') and ord(x)<=ord('z'):
        o+=chr((ord(x)+2-ord('a'))%26+ord('a'))
    else:
        o+=x
print(o)