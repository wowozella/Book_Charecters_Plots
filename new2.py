
import matplotlib.pyplot as plt
import numpy as np


#باز کردن فايل اصلي تکست
fp=open('Projects.txt','r')
text=fp.read().lower()
fp.close()

words=text

# نمايش طول ليست کلمات اصلي
print('len(text) : ',len(text))

print('len(words) : ',len(words))



### words=input('input: ')
voices=['a','b','c','d','f','g','h','j','e','i','o','u','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

found=dict()
found['a']=0
found['b']=0
found['c']=0
found['d']=0
found['e']=0
found['f']=0
found['g']=0
found['h']=0
found['i']=0
found['j']=0
found['k']=0
found['l']=0
found['m']=0
found['n']=0
found['o']=0
found['p']=0
found['q']=0
found['r']=0
found['s']=0
found['t']=0
found['u']=0
found['v']=0
found['w']=0
found['x']=0
found['y']=0
found['z']=0
for letter in words:
    if letter in voices:
        found[letter]+=1   #اين قسمت کار شمارش کاراکترها رو انجام ميده
    else:
        pass
else:
    print('finished!')
    print('=========')
i=0
for key ,value in found.items():
    if i<9 :
        if value <10:
            print(i+1 ,'----', key,'was found   ',value,'     time(s).')
        elif value <100:
            print(i+1 ,'----', key,'was found   ',value,'    time(s).')
        elif value <1000:
            print(i+1 ,'----', key,'was found   ',value,'   time(s).')
        elif value<10000:
            print(i+1 ,'----', key,'was found   ',value,'  time(s).')
    else:
        if value<10:
            print(i+1 ,'---', key,'was found   ',value,'     time(s).')
        elif value<100:
            print(i+1 ,'---', key,'was found   ',value,'    time(s).')
        elif value<1000:
            print(i+1 ,'---', key,'was found   ',value,'   time(s).')
        elif value<10000:
            print(i+1 ,'---', key,'was found   ',value,'  time(s).')
    i+=1

    
j=0

list1=[]
list2=found.values()
    
list1.append(found.values())
print (list1)


arr=np.array(list(list1))
print (arr[0:1])
