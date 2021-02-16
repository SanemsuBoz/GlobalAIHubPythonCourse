import random

matrix=[] 
pList=[]
mList=[]

#Prime numbers for 0 between 100
for num in range(0, 100):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           pList.append(num)  
 
#Choices random 9 numbers from prime numbers list                   
for i in range(10):
    mList.append(random.choice(pList))


matrix=[[mList[0],mList[1],mList[2]],
        [mList[3],mList[4],mList[5]],
        [mList[6],mList[7],mList[8]]]

#Print 3x3 matrix
for i in range(3):
    for j in range(3):
        print(matrix[i][j], end=" ")   
    print()