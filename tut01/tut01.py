# importing required libraries
from operator import concat
import pandas as pd
import itertools
import csv
import numpy as np
import os



# reading the input csv file
df=pd.read_csv('octant_input.csv')
# calculating the mean value of U,V,W respectively by sing pandas inbulit functions
meanU=df['U'].mean()
meanV=df['V'].mean()
meanW=df['W'].mean()
#  making new colunms for U avg, V avg, W avg.
df['U avg']=meanU
df['V avg']=meanV
df['W avg']=meanW
#  calculating error in U,V and W.
df['U-Uavg']=df['U']-meanU
df['V-Vavg']=df['V']-meanV
df['W-Wavg']=df['W']-meanW
# creating a list for octant values
octant=[]


#  calculating the Octant value .
for (l, m, q) in zip(df['U-Uavg'],df['V-Vavg'],df['W-Wavg']):
         
     
#   appanding the octannt values to the list
         if l>0 and m>0 and q<0:
             octant.append('-1')
         elif l>0 and m>0 and q>0:
              octant.append('1')
         elif l<0 and m>0 and q<0:
              octant.append('-2')
         elif l<0 and m>0 and q>0:
              octant.append('2')
         elif l<0 and m<0 and q<0:
              octant.append('-3')
         elif l<0 and m<0 and q>0:
           octant.append('3')
         elif l>=0 and m<=0 and q<0:
            octant.append('-4')
         elif l>0 and m<0 and q>0:
             octant.append('4')
   
  
df['octant'] = octant
 


 
leng=df['octant'].count()
print(leng) 
# Initialize matrix
matri = []

  
# For user input
a=[]
      # A for loop for column entries
a.append('Octant ID')
a.append('  1')
a.append(' -1')
a.append('  2')
a.append('  -2')
a.append('  3')
a.append('   -3')
a.append('  4')
a.append('  -4')
matri.append(a)
a=[]
a.append('Overall')

a.append(df['octant'].value_counts()['1'])
a.append(df['octant'].value_counts()['-1'])
a.append(df['octant'].value_counts()['2'])
a.append(df['octant'].value_counts()['-2'])
a.append(df['octant'].value_counts()['3'])
a.append(df['octant'].value_counts()['-3'])
a.append(df['octant'].value_counts()['4'])
a.append(df['octant'].value_counts()['-4'])
matri.append(a)  
# For printing the matrix
for i in range(2):
    for j in range(9):
        print(matri[i][j], end = " ")
    print()


# creating list of list name matri

# k=int (input("enter mod "))
# giving the value of MOD  
k=5000
# printing the mod value
print("mod"+str(k))


popoo=[]
popoo.append("mod ")
popoo.append(str(k))
matri.append(popoo)


z=int(leng/k)+1

# no rows in output
R = int(z)

# no column is constant equal to 9
C = int(9)
  
# Initialize matrix
matrix = []
number=['1','-1','2','-2','3','-3','4','-4']
  

zz=int(0)
for i in range(R):          # A for loop for row entries
    # creating a list
    a =[]
     
    for j in range(C): 
     if j==0:
        # condition for last row of output to cheak the  length of input so it stop when input length reached
         if i==R-1:
            u=str(i*k)+"-"+str(leng) 
            a.append(u) 
         else:         
              u=str(i*k)+"-"+str(k*(i+1)-1) 
              a.append(u) 
     else:    # A for loop for column entries
        # for counting the values of diffrent octant i am making a new variable count
      count=0
      for xx in range(i*k,k*(i+1)):
               if xx==leng:
                    break

               if df['octant'][xx]==number[j-1]:
                    count+=1
                    
      a.append(count)
     
    matrix.append(a)
    
      

# For printing the matrix
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end = "    ")
    print()







# temprorly saving matrices in file1.csv
with open("file1.csv","w") as file1:
    csvWriter = csv.writer(file1,delimiter=',')
    
    csvWriter.writerows(matri)
    
    csvWriter.writerows(matrix)


# reading the same file which you recently seved
dt=pd.read_csv('file1.csv')

# addding new column to the Output file
df['Octant ID']=dt['Octant ID']
df['  1']=dt['  1']
df[' -1']=dt[' -1']
df['  2']=dt['  2']
df['  -2']=dt['  -2']
df['  3']=dt['  3']
df['   -3']=dt['   -3']
df['  4']=dt['  4']
df['  -4']=dt['  -4']

# removing the opend file1.csv file
os.remove("file1.csv")
#saving my output in csv
df.to_csv('octant_output.csv', mode='w', header=True)
