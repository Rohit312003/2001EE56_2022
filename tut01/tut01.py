from operator import concat
import pandas as pd
import itertools
import csv
import numpy as np




df=pd.read_csv('octant_input.csv')
meanU=df['U'].mean()
meanV=df['V'].mean()
meanW=df['W'].mean()

df['U avg']=meanU
df['V avg']=meanV
df['W avg']=meanW

df['U-Uavg']=df['U']-meanU
df['V-Vavg']=df['V']-meanV
df['W-Wavg']=df['W']-meanW
octant=[]
for (l, m, q) in zip(df['U-Uavg'],df['V-Vavg'],df['W-Wavg']):
         
     

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


# creating list nmae matri

k=int (input("enter mod "))

popoo=[]
popoo.append("enter mod ")
popoo.append(str(k))



z=int(leng/k)+1


R = int(z)
C = int(9)
  
# Initialize matrix
matrix = []
number=['1','-1','2','-2','3','-3','4','-4']
  
# For user input
zz=int(0)
for i in range(R):          # A for loop for row entries
    a =[]
     
    for j in range(C): 
     if j==0:
         if i==R-1:
            u=str(i*k)+"-"+str(leng) 
            a.append(u) 
         else:         
              u=str(i*k)+"-"+str(k*(i+1)-1) 
              a.append(u) 
     else:    # A for loop for column entries
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








# with open("file1.csv","w+") as file1:
#     csvWriter = csv.writer(file1,delimiter=',')
    
#     csvWriter.writerows(matri)
#     csvWriter.writerows(popoo)
#     csvWriter.writerows(matrix)


# df.to_csv('file1.csv', mode='a', header=False)

# def octact_identification(mod=5000):
# ###Code


# from platform import python_version
# ver = python_version()

# if ver == "3.8.10":
#     print("Correct Version Installed")
# else:
#     print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

# mod=5000
# octact_identification(mod)