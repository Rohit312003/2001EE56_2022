
from operator import concat
import pandas as pd
import openpyxl 
import csv
import numpy as np
import os
from openpyxl import load_workbook  
# ------------------------------------------------taking input file---------------------------------------------------------------
wb = load_workbook('input_octant_transition_identify.xlsx')  
sheet_obj = wb.active
                                                                  #reading the input file and storing its value in the df 
df = pd.read_excel('input_octant_transition_identify.xlsx')

print("Column headings:")
print(df)
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
# ----------------------------------------------below code for desiding the octant----------------------------------------------------------
                                                                  # creating a list for octant values
octant=[]                                                         #  calculating the Octant value .
for (l, m, q) in zip(df['U-Uavg'],df['V-Vavg'],df['W-Wavg']):     #   appanding the octannt values to the list
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
# ---------------------------------------------------octant count in certain ranges-------------------------------------------------
                                                                    # Initialize matrix
matri = []

                                                                    #making list
                                                                     
a=[]
                                                                    # making a row using list
a.append('Octant ID')
a.append('  1')
a.append(' -1')
a.append('  2')
a.append('  -2')
a.append('  3')
a.append('   -3')
a.append('  4')
a.append('  -4')
                                                                    # appending list value in matrix its lok like a adding a rowwin exel
matri.append(a)                                                     #making list 
a=[]
a.append('Overall')
                                                                    # appending the value of counts of  octant values
a.append(df['octant'].value_counts()['1'])
a.append(df['octant'].value_counts()['-1'])
a.append(df['octant'].value_counts()['2'])
a.append(df['octant'].value_counts()['-2'])
a.append(df['octant'].value_counts()['3'])
a.append(df['octant'].value_counts()['-3'])
a.append(df['octant'].value_counts()['4'])
a.append(df['octant'].value_counts()['-4'])
                                                                # appending list value in matrix its lok like a adding a rowwin exel  
matri.append(a)  
                                                                # For printing the matrix
for i in range(2):
    for j in range(9):
        print(matri[i][j], end = " ")
    print()


                                                                # creating list of list name matri

# k=int (input("enter mod "))
# -----------------------------------------------below we giving the MOD value for making slots-------------------------------------------------
                                                                # giving the value of MOD  
k=5000
zo=k
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
    # ------------------------------------------------below code of overall transtions in octant value----------------------------------------------
# defing a new matrix for transtion calculations
newtransmat=[] 
# For user input
popoo=[]
popoo4=[]
popoo4.append(" ")
newtransmat.append(popoo4)
popoo4=[]
popoo4.append(" ")
newtransmat.append(popoo4)
popoo.append("Overall Transition Count")
newtransmat.append(popoo)
a=[]

      # adding a new row as required in the output
a.append('Count')
a.append('  1')
a.append(' -1')
a.append('  2')
a.append('  -2')
a.append('  3')
a.append('   -3')
a.append('  4')
a.append('  -4')
newtransmat.append(a)
# below code run for j=1,2,3,4
# below code is for over all
for j in range(1,5):
    q=[]
    # below value are transtion count for j
    a=b=c=d=e=f=g=h=0
    # below value are transtion count for -j
    aa=bb=cc=dd=ee=ff=gg=hh=0
    # below cord for countin the all the transtions in the total length of octant
    for k in range(0,leng-1):
        # below cord for tanstion of j to 1 herw j may be 1,2,3,4
        if(df['octant'][k]==str(j) and df['octant'][k+1]=='1'):
            a=a+1
        # below cord for tanstion of j to -1 herw j may be 1,2,3,4 similerly all the below codes
        if(df['octant'][k]==str(j) and df['octant'][k+1]=='-1'):
            b=b+1
        if(df['octant'][k]==str(j) and df['octant'][k+1]=='2'):
            c=c+1
        if(df['octant'][k]==str(j) and df['octant'][k+1]=='-2'):
            d=d+1
        if(df['octant'][k]==str(j) and df['octant'][k+1]=='3'):
            e=e+1
        if(df['octant'][k]==str(j) and df['octant'][k+1]=='-3'):
            f=f+1
        if(df['octant'][k]==str(j) and df['octant'][k+1]=='4'):
            g=g+1
        if(df['octant'][k]==str(j) and df['octant'][k+1]=='-4'):
            h=h+1
        if(df['octant'][k]==str(-j) and df['octant'][k+1]=='1'):
            aa=aa+1
        if(df['octant'][k]==str(-j) and df['octant'][k+1]=='-1'):
            bb=bb+1
        if(df['octant'][k]==str(-j) and df['octant'][k+1]=='2'):
            cc=cc+1
        if(df['octant'][k]==str(-j) and df['octant'][k+1]=='-2'):
            dd=dd+1
        if(df['octant'][k]==str(-j) and df['octant'][k+1]=='3'):
            ee=ee+1
        if(df['octant'][k]==str(-j) and df['octant'][k+1]=='-3'):
            ff=ff+1
        if(df['octant'][k]==str(-j) and df['octant'][k+1]=='4'):
            gg=gg+1
        if(df['octant'][k]==str(-j) and df['octant'][k+1]=='-4'):
            hh=hh+1   
   
    q.append(str(j))
    # appending the transtion count for j to 1
    q.append(str(a))
    q.append(str(b))
    q.append(str(c))
    q.append(str(d))
    q.append(str(e))
    q.append(str(f))
    q.append(str(g))
    q.append(str(h))
    # adding the transtion counts in new matrix as a row for j to 1,-1,2,-2 and so on
    newtransmat.append(q)
    y=[]
    y.append(str(-j))
    y.append(str(aa))
    y.append(str(bb))
    y.append(str(cc))
    y.append(str(dd))
    y.append(str(ee))
    y.append(str(ff))
    y.append(str(gg))
    y.append(str(hh))
    # adding the transtion counts in new matrix as a row for -j to 1,-1,2,-2 and so on
    newtransmat.append(y)

    # ------------below code if we want above calution in some range like mod =5000 means no transtition in slot of 0-4999,5000-9999 and so on--------------
for i in range(R):          # A for loop for row entries
    # creating a list
    a =[]
        # condition for last row of output to cheak the  length of input so it stop when input length reached
    if(i==R-1):
            popoo=[]
            popoo.append("Transition Count")
            newtransmat.append(popoo)
            u=str(i*zo)+"-"+str(leng-1) 
            a.append(u)
            
            
            newtransmat.append(a)  
    else:    
            # appending the range in which we calculating the transtions count  
            u=str(i*zo)+"-"+str(zo*(i+1)-1) 
            popoo=[]
            popoo.append("Transition Count")
            newtransmat.append(popoo)
            a.append(u)
            newtransmat.append(a)

    a=[]
    a.append('Count')
    a.append('  1')
    a.append(' -1')
    a.append('  2')
    a.append('  -2')
    a.append('  3')
    a.append('   -3')
    a.append('  4')
    a.append('  -4')
    newtransmat.append(a)
    print(newtransmat)   
    for j in range(1,5):
                    q=[]
                    a=b=c=d=e=f=g=h=0
                    aa=bb=cc=dd=ee=ff=gg=hh=0
                    for k in range(i*zo,zo*(i+1)):
                        # checking wether the k is not greater then no of row present in data frame
                        if k>leng-2:
                            break
                        # below code is same as described in above 
                        if(df['octant'][k]==str(j) and df['octant'][k+1]=='1'):
                            a=a+1
                        if(df['octant'][k]==str(j) and df['octant'][k+1]=='-1'):
                            b=b+1
                        if(df['octant'][k]==str(j) and df['octant'][k+1]=='2'):
                            c=c+1
                        if(df['octant'][k]==str(j) and df['octant'][k+1]=='-2'):
                            d=d+1
                        if(df['octant'][k]==str(j) and df['octant'][k+1]=='3'):
                            e=e+1
                        if(df['octant'][k]==str(j) and df['octant'][k+1]=='-3'):
                            f=f+1
                        if(df['octant'][k]==str(j) and df['octant'][k+1]=='4'):
                            g=g+1
                        if(df['octant'][k]==str(j) and df['octant'][k+1]=='-4'):
                            h=h+1
                        if(df['octant'][k]==str(-j) and df['octant'][k+1]=='1'):
                            aa=aa+1
                        if(df['octant'][k]==str(-j) and df['octant'][k+1]=='-1'):
                            bb=bb+1
                        if(df['octant'][k]==str(-j) and df['octant'][k+1]=='2'):
                            cc=cc+1
                        if(df['octant'][k]==str(-j) and df['octant'][k+1]=='-2'):
                            dd=dd+1
                        if(df['octant'][k]==str(-j) and df['octant'][k+1]=='3'):
                            ee=ee+1
                        if(df['octant'][k]==str(-j) and df['octant'][k+1]=='-3'):
                            ff=ff+1
                        if(df['octant'][k]==str(-j) and df['octant'][k+1]=='4'):
                            gg=gg+1
                        if(df['octant'][k]==str(-j) and df['octant'][k+1]=='-4'):
                            hh=hh+1    
                    q.append(str(j))
                    q.append(str(a))
                    q.append(str(b))
                    q.append(str(c))
                    q.append(str(d))
                    q.append(str(e))
                    q.append(str(f))
                    q.append(str(g))
                    q.append(str(h))
                    newtransmat.append(q)
                    y=[]
                    y.append(str(-j))
                    y.append(str(aa))
                    y.append(str(bb))
                    y.append(str(cc))
                    y.append(str(dd))
                    y.append(str(ee))
                    y.append(str(ff))
                    y.append(str(gg))
                    y.append(str(hh))
                    newtransmat.append(y)                                  
  
# temprorly saving matrices in file1.csv
with open("file2.csv","w") as file1:
    csvWriter = csv.writer(file1,delimiter=',')
    csvWriter.writerows(matri)
    csvWriter.writerows(matrix)
    csvWriter.writerows(newtransmat)
# reading the same file which you recently seved
dt=pd.read_csv('file2.csv')
# addding new column to the Output file

# below code is for making gap between octant column and transtion matrix column
df['_']=str(" ")

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
os.remove("file2.csv")
# below code for adding sove string in certain column
for i in range(0,leng):
    if df['Octant ID'][i]=='mod ':
        df['_'][i]='Input'  
    if df['Octant ID'][i]=='1':
         df['_'][i]='From'
# ------------------------------------------saving out data frame as xlsx file--------------------------------------------------------
with pd.ExcelWriter('output_octant_transition_identify.xlsx') as writer:
    df.to_excel(writer, sheet_name='Sheet_name_1')
print("sucssesfully done!")
