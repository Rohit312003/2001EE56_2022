# importing required libraries
from operator import concat
import pandas as pd
import itertools
import csv
import numpy as np
import os
from datetime import datetime 


# reading the input csv file
df=pd.read_csv('input_attendance.csv')
print(df)
dt=pd.read_csv('input_registered_students.csv')
print(dt)

	 

 
# dropping null value columns to avoid errors
df.dropna(inplace = True)
 
# new data frame with split value columns
new = df["Timestamp"].str.split(" ", n = 1, expand = True)

rollna = df["Attendance"].str.split(" ", n = 1, expand = True)
df["Roll"]=rollna[0]
df["Name"]=rollna[1]
# making separate first name column from new data frame
df["Date"]= new[0]
 
# making separate last name column from new data frame
df["time"]= new[1]
 
# Dropping old Name columns
df.drop(columns =["Timestamp"], inplace = True)
df.drop(columns =["Attendance"], inplace = True)
# df display

import datetime  
from datetime import date 
df['Name'] = df['Name'].str.upper()
df['Roll'] = df["Roll"].str.upper()
a=[]

for x in df["Date"]:
    date=x

    day, month, year = date.split('/')     
    day_name = datetime.date(int(year), int(month), int(day)) 
    a.append(day_name.strftime("%A"))
df["days"]=a

leng=df["Date"].count()

print(leng)
k=0
fq={}
for i in df["days"]:
    if (i=="Thursday" or i=="Monday"):
        try:
            
            fq[df["Roll"][k]]=0
            
        except:
            print("error")

    k+=1

k=0
for i in df["days"]:
    if (i=="Thursday" or i=="Monday"):
        try:
            print(df["Roll"][k]+" "+df["time"][k]+"  "+i)
            fq[df["Roll"][k]] +=1
            print(fq[df["Roll"][k]])
        except:
            print("error")

    k+=1

    


        
                       
    
print(df)
       



        

df.to_csv('octant_output.csv', mode='w', header=True,index=False)