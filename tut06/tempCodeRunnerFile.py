# importing required libraries
from operator import concat
import pandas as pd
import itertools
import csv
import numpy as np
import os
from datetime import datetime
from csv import writer
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from IPython.display import display, HTML
import datetime  
from datetime import date 
import smtplib

# reading the input csv file
df=pd.read_csv('input_attendance.csv')

dt=pd.read_csv('input_registered_students.csv')

k=df['Attendance'].isnull().sum()  
print(k)
                                                                                                            
# some the value are missing so i have to remove those values from my data set
df['Attendance'].replace('', np.nan, inplace=True)
print(df)
df.dropna(subset=['Attendance'], inplace=True)
print(df)

# after removing the Null values we again reading the data set with no null values
df.to_csv('input_attendance.csv', mode='w', header=True,index=False)
df=pd.read_csv('input_attendance.csv')

# dropping null value columns to avoid errors
df.dropna(inplace = True)
#  in the below code we extracting the date and time from timestamp
# new data frame with split value columns
new = df["Timestamp"].str.split(" ", n = 1, expand = True)
# spliting the attendance column into roll no and name column
rollna = df["Attendance"].str.split(" ", n = 1, expand = True)
df["Roll"]=rollna[0]
df["Name"]=rollna[1]
# making separate first name column for roll no from new data frame
df["Date"]= new[0]
 
# making separate last name column for name from new data frame
df["time"]= new[1]

# extracting the hours from time column
hour = df["time"].str.split(":", n = 1, expand = True)
df['hour']=hour[0]
 
# Dropping old attendance and time columns

df.drop(columns =["time"], inplace = True)
df.drop(columns =["Attendance"], inplace = True)

#  in the name and roll no column may values are in lower and uper case so we make all the values in upper case

df['Name'] = df['Name'].str.upper()
df['Roll'] = df["Roll"].str.upper()
a=[]

# in the below code we are trying to know the day wether  it is monday or thrusday or any other day

for x in df["Date"]:
    date=x

    day, month, year = date.split('/')     
    day_name = datetime.date(int(year), int(month), int(day)) 
    a.append(day_name.strftime("%A"))
df["days"]=a

leng=df["Date"].count()





with open('output\\attendance_report_duplicate.csv','w') as f_object:
 
    # Pass this file object to csv.writer()
            # and get a writer object
    writer_object = writer(f_object)
    list=["Timestamp","Roll No","Name","Total count of attendance on that day"]
    writer_object.writerow(list)    
            # Pass the list as an argument into
            # the writerow()
    print("kk")       
    for (qq,ww,j) in zip(df['Date'],df['days'],df['hour']):
        
        if (ww=="Thursday" or ww=="Monday"):
            rr=int(j)
            try:
                if(rr==14):
                    
                    fqd={}
                    fqdt={}
                    
                    for i in dt["Roll No"]:
                            try:
                            
                                
                                fqd[i]=0
                                fqdt[i]=-1
                            except:
                                print("error in line no 97")    
                            
                    qw=0
                    
                    for i in df["Date"]:
                        try:
                            if qq==i and rr==int(df['hour'][qw]):
                                
                                fqd[df['Roll'][qw]]+=1

                                if fqd[df['Roll'][qw]]==1:
                                    fqdt[df['Roll'][qw]]=df['Timestamp'][qw]
                        except:
                                print(df['Roll'][qw]," note found"," error in line no 107")
                        qw+=1
                    
                    qw=0
                    try:
                        for i in dt["Roll No"]:
                            z=[]
                            if fqd[i]>1:
                                
                                z.append(fqdt[i])
                                z.append(i)
                                z.append(dt['Name'][qw])
                                z.append(fqd[i])
                                writer_object.writerow(z)
                            qw+=1   
            
                    except:
                        print("error")
            except:
                    print("error in j")

    f_object.close()
   
dkk=pd.read_csv('output\\attendance_report_duplicate.csv')
dkk.drop_duplicates(inplace=True)
dkk.to_csv('output\\attendance_report_duplicate.csv', mode='w', header=True,index=False)            
                      
df.to_csv('output\Attendance_report_consolidated.csv', mode='w', header=True,index=False)
dk=pd.read_csv('output\Attendance_report_consolidated.csv')

List = ['Roll', 'Name', 'total_lecture_taken', 'attendance_count_actual', 'attendance_count_fake','attendance_count_absent','Percentage (attendance_count_actual/total_lecture_taken) 2 digit decimal']
 
# Open our existing CSV file in append mode
# Create a file object for this file

count=0
datee=" "
for i,j in zip(df['days'],df['Date']):

    print(i)
    if(j!=datee and (i=="Thursday" or i=="Monday")):
        datee=j
        count+=1



print(count)


