import numpy as np
import random

A = np.zeros((30,30))+2        #creating a matrix
count=0
for i in range(1000):
  x=random.randint(0,29)
  y=random.randint(0,29)
  if(A[x][y]==2 and count<100):
    A[x][y]= 0
    count+=1
  elif(A[x][y]==2 and count>=100 and count<250):
    A[x][y]= -1
    count+=1
  elif(A[x][y]==2 and count>=250 and count <400):
    A[x][y]= +1
    count+=1
  elif(count==400):
    break
#print(A)

-----------------------------------------------------------------------------------------

#defining values of energy of interation
def energy(x,y):
  if x==0 and y==-1:
    e = -0.1
  elif x==0 and y==1:
    e = 0.1
  elif x==0 and y==0:
    e = 0.1
  elif x==1 and y==1:
    e = 0.5
  elif x==-1 and y==-1:
    e = 0.5
  elif x==1 and y==-1:
    e = -0.7
  else:
    e=0
  return e

------------------------------------------------------------------------------------------

#Initial energy of the system
old_energy = 0
first_energy = np.zeros((30,30))
for i in range(30):
  for j in range(30):
    if(i==29 and j!=29):
      first_energy[i][j] = energy(A[i][j],A[i][j+1])
    elif(i!=29 and j==29):
      first_energy[i][j] = energy(A[i][j],A[i+1][j])
    elif(i==29 and j==29):
      continue
    else:
      first_energy[i][j] += energy(A[i][j],A[i+1][j])
      first_energy[i][j] += energy(A[i][j],A[i][j+1])
    #print((i,j+1),(i+1,j))
  #print(first_energy)
    old_energy=old_energy + first_energy[i][j]
print(old_energy)

-------------------------------------------------------------------------------------------

import random
import math
KT=0.6
for i in range(1000):
  A1=A.copy()
  x=random.randint(0,29)
  y=random.randint(0,29)
  if A[x][y]==0 or A[x][y]==1 or A[x][y]==-1:
    r=random.random()
    if(r<=0.25):
      x1=x-1
      y1=y
      if(x1<0):
    #adding Periodic Boundary Condition
        x1=x1+30
      if(A[x1][y1]==2):
        A[x1][y1]=A[x][y]
        A[x][y]=2
        x=x1
        y=y1
    if(r>0.25 and r<=0.5):
      x1=x+1
      y1=y
      if(x1>29):
        x1=x1-30
        if(A[x1][y1]==2):
          A[x1][y1]=A[x][y]
          A[x][y]=2
          x=x1
          y=y1
    if(r>0.5 and r<=0.75):
      x1=x
      y1=y-1
      if(y1<0):
        y1=y1+30
      if(A[x1][y1]==2):
        A[x1][y1]=A[x][y]
        A[x][y]=2
        x=x1
        y=y1
    if(r>0.75):
      x1=x
      y1=y+1
      if(y1>29):
        y1=y1-30
      if(A[x1][y1]==2):
        A[x1][y1]=A[x][y]
        A[x][y]=2
        x=x1
        y=y1
#print(A)

------------------------------------------------------------------------------------

#Energy after the random movement of particles
new_energy = 0
sec_energy = np.zeros((30,30))
for i in range(30):
  for j in range(30):
    if(i==29 and j!=29):
      sec_energy[i][j] = energy(A[i][j],A[i][j+1])
    elif(i!=29 and j==29):
      sec_energy[i][j] = energy(A[i][j],A[i+1][j])
    elif(i==29 and j==29):
      continue
    else:
      sec_energy[i][j] += energy(A[i][j],A[i+1][j])
      sec_energy[i][j] += energy(A[i][j],A[i][j+1])
    #print((i,j+1),(i+1,j))
#print(sec_energy)

-------------------------------------------------------------------------------------

#Metropolis criterion of the Monte Carlo algorithm
for i in range(30):
  for j in range(30):
    new_energy = new_energy + sec_energy[i][j]
    if new_energy < old_energy:
        old_energy = new_energy
    elif new_energy > old_energy:
      r2=random.random()
      if math.e**(-(new_energy-old_energy))/KT < r2:
        old_energy = new_energy
      else:
        #Revert to the previous state and energy
        new_energy = old_energy
        A = A1
        continue
print(old_energy,new_energy)

--------------------------------------------------------------------------------------

import numpy as np
import random
import math
A = np.zeros((30,30))+2
count=0
for i in range(100000):
  x=random.randint(0,29)
  y=random.randint(0,29)
  if(A[x][y]==2 and count<100):
    A[x][y]=0
    count+=1
  elif(A[x][y]==2 and count>=100 and count<250):
    A[x][y]=-1
    count+=1
  elif(A[x][y]==2 and count>=250 and count <400):
    A[x][y]=+1
    count+=1
  elif(count==400):
    break

B=np.zeros((30,30,2))
k_a=100
k_d=0.01
R=k_a+k_d

for i in range(10000000):
  A1=A.copy()
  x=random.randint(0,29)
  y=random.randint(0,29)
  if A[x][y]==0 or A[x][y]==1 or A[x][y]==-1 and A[x][y]==3:
    r=random.random()
    if(r<=0.25):
      x1=x-1
      y1=y
      if(x1<0):
        x1=x1+30
    elif(r>0.25 and r<=0.5):
      x1=x+1
      y1=y
      if(x1>29):
        x1=x1-30
    elif(r>0.5 and r<=0.75):
      x1=x
      y1=y-1
      if(y1<0):
        y1=y1+30
    elif(r>0.75):
      x1=x
      y1=y+1
      if(y1>29):
        y1=y1-30

    #Complex Formation
    r1=random.random()
    rr=r1*R
    #Association
    if(A[x1][y1]!=2 and A[x][y]!=0 and A[x1][y1]!=0 and  A[x][y]!=3 and rr<=k_a):
      if(A[x][y]==1 and A[x1][y1]==1):
        B[x1][y1][0]+=2
      if(A[x][y]==-1 and A[x1][y1]==-1):
        B[x1][y1][1]+=2
      if((A[x][y]==1 and A[x1][y1]==-1) or (A[x][y]==-1 and A[x1][y1]==1)):
        B[x1][y1][0]+=1
        B[x1][y1][1]+=1
      if(A[x][y]==1 and A[x1][y1]==3):
        B[x1][y1][0]+=1
      if(A[x][y]==-1 and A[x1][y1]==3):
        B[x1][y1][1]+=1
      A[x][y]=2
      A[x1][y1]=3
    #Dissociation
    elif (A[x][y]==3 and A[x1][y1]==2 and rr>k_a):
      if(np.sum(B[x][y])==2):
        if(B[x][y][0]==2):
          A[x][y]=1
          A[x1][y1]=1
          B[x][y][0]=0
        elif(B[x][y][1]==2):
          A[x][y]=-1
          A[x1][y1]=-1
          B[x][y][1]=0
        elif(B[x][y][0]==1 and B[x][y][1]==1):
          A[x][y]=-1
          A[x1][y1]=1
          B[x][y][0]=0
          B[x][y][1]=0
      elif(np.sum(B[x][y])>2):
        r3=random.random()
        if(r3<=0.5):
          if(B[x][y][0]>1):
            A[x1][y1]=1
            B[x][y][0]=B[x][y][0]-1
          elif(B[x][y][1]>1):
            A[x1][y1]=-1
            B[x][y][1]=B[x][y][1]-1
        else:
          if(B[x][y][1]>1):
            A[x1][y1]=-1
            B[x][y][1]=B[x][y][1]-1
          elif(B[x][y][0]>1):
            A[x1][y1]=1
            B[x][y][0]=B[x][y][0]-1

    #Movement of Particles
    elif(A[x1][y1]==2):
          A[x1][y1]=A[x][y]
          A[x][y]=2
          x=x1
          y=y1

count1=0
count0=0
countn1=0
count3=0
sum=0
for i in range(30):
  for j in range(30):
    if(A[i][j]==1):
      count1 +=1
    if(A[i][j]==-1):
      countn1 +=1
    if(A[i][j]==0):
      count0 +=1
    if(A[i][j]==3):
      #print(A[i][j],B[i][j],np.sum(B[i][j]))
      count3 +=1
      sum+=np.sum(B[i][j])
print(count1,countn1,count0,count3,sum)




































