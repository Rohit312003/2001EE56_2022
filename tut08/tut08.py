
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
		nameofplayer=[]
		with open('teams.txt','r') as file:
			# bowler={"bol":{"player":" ","O":0,"M":0,"R":0,"W":0,"N":0,"B":0,"W":0,"D":0,"E":0,"C":0,"O":0}}
			


			     
			bat={"player":" ","R":0,"B":0, "4s":0, "6s":0,"S":0,"R":0}
		# reading each line 
			hdjd = file.readlines()
			lo=0
			
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
							nameofplayer.append(lll[0])  
							file7.write('\n')  
							
							a=[]
							print(lll[1])
							a.append(lll[1])
							nameofplayer.append(lll[1] )
							file7.write(lll[1])  
							file7.write('\n') 
							
							
							
							lo+=1

							
							ll+=1
						except:
							pass

					else:
						a=[]
						
						a.append(word)
						nameofplayer.append(word) 
						file7.write(word)  
						file7.write('\n') 
						print(word)

		file7.write('\n') 
		file7.write('\n') 
		file7.write('\n') 
		nameofteam=['pak_inns1.txt','india_inns2.txt']
		nameofteam2=['Pakistan Innings ','India Innings ']
		play=0
		print("-------------------------------------------------------------------------------------")
		
		print("-------------------------------------------------------------------------------------")
		for o in nameofteam:
			bolo={}
			bolR={}
			bolW={}
			bolD={}
			run={}
			run4={}
			runR={}
			run6={}
			runD={}
			total=0
			wic=0
			file7.write("\n")
			file7.write(nameofteam2[play])
			file7.write("\n")
			play+=1
			with open(o,'r') as file2:
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
							bolo[kiu]+=1
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
							bolo[kiu]+=1
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
							bolo[kiu]+=1
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
							bolo[kiu]+=1
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
							bolo[kiu]+=1
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
								bolo[kiu]+=1
								bolW[kiu]
								bolD[kiu]
								
							elif(qwer[2]==" 2 runs"):
								total+=2
								bolR[kiu]+=2
								bolo[kiu]+=1
								bolW[kiu]
								bolD[kiu]
								
								
							elif(qwer[2]==" 3 runs"):
								total+=3
								
								bolR[kiu]+=3
								bolo[kiu]+=1
								bolW[kiu]
								bolD[kiu]
								
							elif(qwer[2]==" wide"):
								total+=1
								
								bolR[kiu]+=1
								
								bolW[kiu]
								bolD[kiu]
								
							elif(qwer[2]==" 2 wides"):
								total+=2
								bolR[kiu]+=2
								
								bolW[kiu]
								bolD[kiu]

							elif(qwer[2]==" 3 wides"):
								total+=3
								
								bolR[kiu]+=3
								
								bolW[kiu]
								bolD[kiu]

							elif(qwer[2]==" FOUR"):
								total+=4
								
								bolR[kiu]+=4
								bolo[kiu]+=1
								bolW[kiu]
								bolD[kiu]

							elif(qwer[2]==" SIX"):
								total+=6
								
								bolR[kiu]+=6
								bolo[kiu]+=1
								bolW[kiu]
								bolD[kiu]
		
						elif(qwer[1]==" no ball"):
							total+=1
							
							bolR[kiu]
							
							bolW[kiu]
							bolD[kiu]
							
						elif(qwer[1]==" no run"):
							total+=0
							runR[yu[1]]+=1
							bolo[kiu]+=1
							bolD[kiu]=+1
						else:
							runR[yu[1]]+=1
							bolW[kiu]+=1
							bolo[kiu]+=1
                
				
				dictactualname={}
				for key in run:
					for w in nameofplayer:
						if w.find(key)>=0:
							dictactualname[key]=w
				file7.write("\n")
				file7.write("Batting")	
				file7.write("\n")
				file7.write(f"{'NAME':<50}{'RUNS':<10}{'BALLS':<10}{'6s':<10}{'4s':<10}{'SR':<10}")
				file7.write("\n")	
				for key in run:
					
					file7.write(f"{dictactualname[key]:<50}{run[key]:<10}{runR[key]:<10}{run6[key]:<10}{run4[key]:<10}{round((run[key]*100)/runR[key],2):<10}") 
					file7.write('\n')
					
				
				
				file7.write("\n")
				file7.write("Bowling")
				file7.write("\n")
				file7.write(f"{'NAME':<50}{'WICKET':<10}{'':<10}{'RUNS':<10}{'ECO':<10}")
				
				for key in bolR:
					file7.write("\n")
					file7.write(f"{key:<50}{bolW[key]:<10}{'':<10}{bolR[key]:<10}{round((bolR[key]*6)/bolo[key],2):<10}")
					file7.write("\n") 
				file7.write("\n")
				file7.write(" WICKETS ")
				file7.write("\n")
				for i in lines:
					if(i!='\n'):
						a.append(i[:len(i)])
						pp=re.search(r"\d*(\W*(\d*)\)\W)",i[:len(i)])
						if pp!=None:
							wic+=1
							ind=len(i[:len(i)])-i[:len(i)][::-1].find(".")
							file7.write("\n")
							file7.write(i[:len(i)-1][ind:])
							file7.write("\n")
							
							
							
							
				
			# file7.write(a)
			file7.write("\n")
			wer=str(total)+"-"+str(wic)
			file7.write(f"{'SCORE:':<80}{wer:>10}")
			file7.write("\n")
				
					
						
			
		
			
			
		   
            
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
