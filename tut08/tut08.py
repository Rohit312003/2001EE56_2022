
from datetime import datetime
start_time = datetime.now()

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
from openpyxl.styles.borders import Border, Side
from openpyxl import load_workbook
import re
#Check if the string starts with "The" and ends with "Spain":

# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)

# if x:
#   print("YES! We have a match!")
# else:
#   print("No match")

#Help

#open workbook

 
#definging the property of border

def scorecard():

    
	
	with open ('scorecard.txt', 'w') as file7:  
		
 
    # Pass this file object to csv.writer()
    # and get a writer object
		
		with open('teams.txt','r') as file:
			# bowler={"bol":{"player":" ","O":0,"M":0,"R":0,"W":0,"N":0,"B":0,"W":0,"D":0,"E":0,"C":0,"O":0}}
			bolo={}
			bolR={}
			bolW={}
			bolD={}
			run={}
			run4={}
			runR={}
			run6={}
			runD={}


			     
			bat={"player":" ","R":0,"B":0, "4s":0, "6s":0,"S":0,"R":0}
		# reading each line 
			hdjd = file.readlines()
			lo=0
			playername={}
			for line in hdjd:
		        
				# reading each word 
				print(line)  
				ll=0     
				for word in line.split(','):
				
					# displaying the words
					if ll==0:
						try:
							a=[]
							lll=word.split(":")
							print(lll[0])
							a.append(lll[0])
							file7.write(lll[0])  
							file7.write('\n')  
							
							a=[]
							print(lll[1])
							a.append(lll[1])
							file7.write(lll[1])  
							file7.write('\n') 
							
							
							
							lo+=1

							
							ll+=1
						except:
							pass

					else:
						a=[]
						
						a.append(word)
						file7.write(word)  
						file7.write('\n') 
						print(word)

		file7.write('\n') 
		file7.write('\n') 
		file7.write('\n') 
		total=0
		wic=0
		file7.write('pak_inns1.txt') 
		with open('pak_inns1.txt','r') as file2:
			a=[]
			lines= file2.readlines()
			for i in lines:
				if(i!='\n'):
					qwer=i.split(",",4)
					yu=qwer[0].split("to",1)
					kl=yu[0].split(" ",1)
					kiu=kl[1]
					bolR[kiu]=0
					bolo[kiu]=0
					bolW[kiu]=0
					bolD[kiu]=0
					run[yu[1]]=0
					run4[yu[1]]=0
					runR[yu[1]]=0
					run6[yu[1]]=0
					runD[yu[1]]=0
                    
			for i in lines:
				if(i!='\n'):
					qwer=i.split(",",4)
					yu=qwer[0].split("to",1)
					kl=yu[0].split(" ",1)
					kiu=kl[1]
                    
                    
					
					
					
					
					if(qwer[1]==' 1 run'):
						total+=1
						bolR[kiu]+=1
						bolo[kiu]
						bolW[kiu]
						bolD[kiu]
						run[yu[1]]+=1
						run4[yu[1]]
						runR[yu[1]]+=1
						run6[yu[1]]
						runD[yu[1]]
					elif(qwer[1]==" 2 runs"):
						total+=2
						bolR[kiu]+=2
						bolo[kiu]
						bolW[kiu]
						bolD[kiu]
						run[yu[1]]+=2
						run4[yu[1]]
						runR[yu[1]]+=1
						run6[yu[1]]
						runD[yu[1]]
						
					elif(qwer[1]==" 3 runs"):
						total+=3
						bolR[kiu]+=3
						bolo[kiu]
						bolW[kiu]
						bolD[kiu]
						run[yu[1]]+=3
						run4[yu[1]]
						runR[yu[1]]+=1
						run6[yu[1]]
						runD[yu[1]]=0
						
					elif(qwer[1]==" wide"):
						total+=1
						bolR[kiu]+=1
						bolo[kiu]
						bolW[kiu]
						bolD[kiu]
						run[yu[1]]
						run4[yu[1]]
						runR[yu[1]]
						run6[yu[1]]
						runD[yu[1]]=0
						
					elif(qwer[1]==" 2 wides"):
						total+=2
						bolR[kiu]+=2
						bolo[kiu]
						bolW[kiu]
						bolD[kiu]
						run[yu[1]]+=2
						run4[yu[1]]
						runR[yu[1]]
						run6[yu[1]]
						runD[yu[1]]=0
						
					elif(qwer[1]==" 3 wides"):
						total+=3
						bolR[kiu]+=3
						bolo[kiu]
						bolW[kiu]
						bolD[kiu]
						run[yu[1]]+=2
						run4[yu[1]]
						runR[yu[1]]
						run6[yu[1]]
						runD[yu[1]]
						
					elif(qwer[1]==" FOUR"):
						total+=4
						bolR[kiu]+=4
						bolo[kiu]
						bolW[kiu]
						bolD[kiu]
						
						run[yu[1]]+=4
						run4[yu[1]]+=1
						runR[yu[1]]+=1
						run6[yu[1]]
						runD[yu[1]]
						
					elif(qwer[1]==" SIX"):
						total+=6
						bolR[kiu]+=6
						bolo[kiu]
						bolW[kiu]
						bolD[kiu]
						
						run[yu[1]]+=6
						run4[yu[1]]
						runR[yu[1]]+=1
						run6[yu[1]]+=1
						runD[yu[1]]=0
						
					elif(qwer[1]==" leg byes"):
						runR[yu[1]]+=1
						if(qwer[2]==' 1 run'):
							total+=1
							bolR[kiu]+=1
							bolo[kiu]
							bolW[kiu]
							bolD[kiu]
							
						elif(qwer[2]==" 2 runs"):
							total+=2
							bolR[kiu]+=2
							bolo[kiu]
							bolW[kiu]
							bolD[kiu]
							
							
						elif(qwer[2]==" 3 runs"):
							total+=3
							
							bolR[kiu]+=3
							bolo[kiu]
							bolW[kiu]
							bolD[kiu]
							
						elif(qwer[2]==" wide"):
							total+=1
							
							bolR[kiu]+=1
							bolo[kiu]
							bolW[kiu]
							bolD[kiu]
							
						elif(qwer[2]==" 2 wides"):
							total+=2
							bolR[kiu]+=2
							bolo[kiu]
							bolW[kiu]
							bolD[kiu]

						elif(qwer[2]==" 3 wides"):
							total+=3
							
							bolR[kiu]+=3
							bolo[kiu]
							bolW[kiu]
							bolD[kiu]

						elif(qwer[2]==" FOUR"):
							total+=4
							
							bolR[kiu]+=4
							bolo[kiu]
							bolW[kiu]
							bolD[kiu]

						elif(qwer[2]==" SIX"):
							total+=6
							
							bolR[kiu]+=6
							bolo[kiu]
							bolW[kiu]
							bolD[kiu]
	
					elif(qwer[1]==" no ball"):
						total+=1
						
						bolR[kiu]
						bolo[kiu]
						bolW[kiu]
						bolD[kiu]
						
					elif(qwer[1]==" no run"):
						total+=0
						runR[yu[1]]+=1
						
						bolD[kiu]=+1
					else:
						runR[yu[1]]+=1
						bolW[kiu]+=1
						
			for key in run:
				print(key,"-> run ",run[key]," in ",runR[key]," balls")
				print(key,"-> 6s ",run6[key])
				print(key,"-> 4s ",run4[key])
			
			
			print("\n")
			for key in bolR:
				print(key,"-> run ",bolR[key])
				print(key,"-> wicket ",bolW[key])
			
			for i in lines:
				if(i!='\n'):
					a.append(i[:len(i)])
					

					pp=re.search(r"\d*(\W*(\d*)\)\W)",i[:len(i)])
					if pp!=None:
						wic+=1
						ind=len(i[:len(i)])-i[:len(i)][::-1].find(".")
						
						print(i[:len(i)-1][ind:])
						file7.write(i[:len(i)-1][ind:])  
						file7.write('\n') 
						
			
			# print(a)
			print(total,"-",wic)

				
					
						
			
		
			
			
		   
            
			# Pass this file object to csv.writer()
			# and get a writer object
				
		
			# Pass the list as an argument into
			# the writ


###Code

from platform import python_version
ver = python_version()

if ver == "3.8.10":
	print("Correct Version Installed")
else:
	print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


scorecard()


end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
