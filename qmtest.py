import matplotlib.pyplot as plt
import numpy as np
import random as rndm

a = [i for  i in range(1, 1001)]


n1 = list()
n2 = list()
n3 = list()
n4 = list()
n5 = list()
n6 = list()


for i in a:
    r=rndm.random()
    r=r*6
    if r<=1:
        n1.append(1)
    elif r<=2:
        n2.append(2)
    elif r<=3:
        n3.append(3)
    elif r<=4:
        n4.append(4)
    elif r<=5:
        n5.append(5)
    elif r<=6:
        n6.append(6)
        
x = np.array(["1", "2", "3", "4", "5", "6"])
y = np.array([len(n1), len(n2), len(n3), len(n4), len(n5), len(n6)])

plt.bar(x,y)
plt.show()

print (len(n1),":", n1)
print (len(n2),":",n2)
print (len(n3),":",n3)
print (len(n4),":",n4)
print (len(n5),":",n5)
print (len(n6),":",n6)