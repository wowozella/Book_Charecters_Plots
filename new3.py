import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
#باز کردن فايل اصلي تکست
fp=open('Projects.txt','r')
text=fp.read().lower()
fp.close()
words=text
# نمايش طول ليست کلمات اصلي
print('len(text) : ',len(text))
print('len(words) : ',len(words))
voices=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
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
        found[letter]+=1
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
new_arr=np.array([])
new_arr=list(found.values())
print(new_arr)
print(voices)
x_=list(range(26))
print(x_)

# labels for bars   
tick_label = voices
# plotting a bar chart   
plt.bar(x_, new_arr, tick_label = tick_label,width = 0.8)   
# naming the x-axis   
plt.xlabel('Letters')   
# naming the y-axis   
plt.ylabel('repitation')   
# plot title   
plt.title('bar chart for letters!')

# function to show the plot   
plt.show()
