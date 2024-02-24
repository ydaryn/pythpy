import re

#ex1
txt = input()
x = re.findall("ab*", txt)
print(x)

#ex2
txt=input()
x=re.match("ab{2,3}", txt) 
if x:
    print("yes")
else:
    print ("no")
    
ex3
txt = input()
xx = re.findall(r'[a-z]+_[a-z]+', txt)
for x in xx:
    print(x)

ex4
txt = input()
xx = re.findall(r'[A-Z][a-z]+', txt)
for x in xx:
    print(x)

#ex5
txt = input()
xx = re.findall(r'\ba\w*b\b', txt)
for x in xx:
    print(x)

ex6
txt = input()
xx = re.sub(r'[ ,.]', ':', txt)
print(xx)

#ex7
def sn_to_cam(sn_str):
    common_str=sn_str.split('_')
    cam_str=common_str[0]+''.join(word.capitalize() for word in common_str[1:])
    return cam_str
s=input()
print(sn_to_cam(s))
 
#ex8
s = input()
parts = re.split(r'([A-Z])', s)
print(parts)

#ex9
import re
def insert_spaces(txt):
    res = re.sub(r'\b([A-Z][a-z]*)\s+(?=[A-Z])', r'\1  ', txt)
    return res
sent = input()
mod_sent = insert_spaces(sent)
print(mod_sent)

#ex10
def cam_to_sn(cam_str):
    sn_str=' '
    for i, char in enumerate(cam_str):
        if char.isupper() and i==0:
            sn_str+=char.lower()
        elif char.isupper():
            sn_str+='_'+char.lower()
        else:
            sn_str+= char
    return sn_str
camel=input()
snake=cam_to_sn(camel)
print(snake)     

