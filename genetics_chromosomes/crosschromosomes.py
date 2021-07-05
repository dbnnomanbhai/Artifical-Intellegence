import random
import math

chromosome = ["01101", "11000", "01000", "10011"]

chromosome_length = len(chromosome)
list = []
phn = []
crosschrom = []

def decimal(n):
    phn = 0
    for i in range(len(n)):
        f = n.pop()
        if f == 1:
            phn  = phn + pow(2, i)
    return phn


for i in range(chromosome_length):
    for p in chromosome[i]:
        list.append(int(p))
    phn.append(decimal(list))


fitness1 = pow(phn[0], 2)
fitness2 = pow(phn[1], 2)
fitness3 = pow(phn[2], 2)
fitness4 = pow(phn[3], 2)
total = fitness1 + fitness2+ fitness3 + fitness4


print("Initiate    Chromosome: ", chromosome)
print(" Phenotypes : ", phn[0], phn[1], phn[2], phn[3])
print(" Fitness : ", fitness1, fitness2, fitness3, fitness4)
print("Total Fitness  : ", total)


probability1= round((fitness1/total), 2)
probability2 = round((fitness2/total), 2)
probability3 = round((fitness3/total), 2)
probability4 = round((fitness4/total), 2)
totalprobable = round((total/total), 2)


print(" The   rate of probability  : ", probability1 ,  probability2  , probability3 , probability4  , totalprobable )

bound1 = round(random.uniform(0,probability1),2)
bound2 = round(random.uniform(probability1,probability1+probability2),2)
bound3 = round(random.uniform(probability1+probability2,probability2+probability3),2)
bound4= round(random.uniform((probability2+probability3),(probability3+probability4)),2)
print(bound1, bound2, bound3 , bound4)
print(type(probability1))
if(bound1<= probability1):
    n1 = "01101"
    crosschrom.append(n1)
if(probability1>= bound2<= (probability1+probability2)):
    n2 = "11000"
    crosschrom.append(n2)
    if(probability1>= bound3 <= (probability1+probability2)):
        n2 = "01000"
        crosschrom.append(n2)
if((probability1+probability2) >= bound3 <= (probability2+probability3)):
    n3 = "01000"
    crosschrom.append(n3)
if((probability2+probability3) >= bound4<= (probability3+probability4)):
    n4 = "11000"
    crosschrom.append(n4)
else:
    print("The cross chromosomes   :")

print(crosschrom)
#the code has been  modified by Najmul Uddin