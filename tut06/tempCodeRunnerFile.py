


# df.to_csv('output\Attendance_report_consolidated.csv', mode='w', header=True,index=False)
# dk=pd.read_csv('output\Attendance_report_consolidated.csv')

# List = ['Roll', 'Name', 'total_lecture_taken', 'attendance_count_actual', 'attendance_count_fake','attendance_count_absent','Percentage (attendance_count_actual/total_lecture_taken) 2 digit decimal']
 
# # Open our existing CSV file in append mode
# # Create a file object for this file


# total_attend=14
# with open('output\Attendance_report_consolidated.csv','w') as f_object:
 
#     # Pass this file object to csv.writer()
#     # and get a writer object
#     writer_object = writer(f_object)
 
#     # Pass the list as an argument into
#     # the writerow()
#     writer_object.writerow(List)
 
#         # Close the file object






#     q=" "
#     k=0
#     fq={}
#     fqfake={}
    
    
#     for i in dk["days"]:
#         if (i=="Thursday" or i=="Monday"):
            
                
#                 fq[dk["Roll"][k]]=0
#                 fqfake[dk["Roll"][k]]=0
               
        

#         k+=1

#     k=0
#     dk["countooo"]=0
#     a=[]
#     for (i,j,e) in zip(dk["days"],dk["hour"],df["Name"]):
#             fqfake[dk["Roll"][k]] +=1
#             if (i=="Thursday" or i=="Monday" ):
            
#                 if(j==14 and q!=e):
#                     q=e 
#                     fq[dk["Roll"][k]] +=1
                    
#                     dk["countooo"][k]=fq[dk["Roll"][k]]
                
#             k+=1
#     k=0
#     for j in dt['Roll No']:
#         try:  
#             a=[]
#             a.append(dt['Roll No'][k])
#             a.append(dt['Name'][k])
#             a.append(total_attend)
#             a.append(fq[j])
#             a.append(fqfake[j]-fq[j])
#             a.append(total_attend-fq[j])
#             a.append(round((fq[j]*100)/total_attend,2))
             
#             writer_object.writerow(a)
#             print(fq[j])
#         except:
#             a=[]
#             a.append(dt['Roll No'][k])
#             a.append(dt['Name'][k])
#             try:
#                 a.append(total_attend)
#             except:
#                 a.append(0)
#             try:
#                 a.append(fq[j])
#             except:
#                 a.append(0)

#             try:
#                 a.append(fqfake[j]-fq[j])
#             except:
#                 a.append(0)
#             a.append(14)
#             a.append(0)
            

#             writer_object.writerow(a)
#             print(j+"error")
#         k+=1

            
        
#     f_object.close()
       
# dk=pd.read_csv('output\Attendance_report_consolidated.csv')
# dk['Name'].replace('', np.nan, inplace=True)
# print(dk)
# dk.dropna(subset=['Name'], inplace=True)
# dk.to_csv('output\Attendance_report_consolidated.csv', mode='w', header=True,index=False)
# dp=pd.read_csv('output\Attendance_report_consolidated.csv')


# for k in range(0,dp['Roll'].count()):
    
#     with open('output\\'+(str)(dp['Roll'][k]+'.csv'),'w') as f_object:
 
#     # Pass this file object to csv.writer()
#     # and get a writer objet
#           writer_object = writer(f_object)
#           List1 = ['Roll', 'Name', 'total_lecture_taken', 'attendance_count_actual', 'attendance_count_fake','attendance_count_absent','Percentage (attendance_count_actual/total_lecture_taken) 2 digit decimal']
#           writer_object.writerow(List1)
#           List2=[dp['Roll'][k],dp['Name'][k],dp['total_lecture_taken'][k],dp['attendance_count_fake'][k],dp['attendance_count_absent'][k],dp['Percentage (attendance_count_actual/total_lecture_taken) 2 digit decimal'][k]]
          
 
#     # Pass the list as an argument into
#     # the writerow()
#           writer_object.writerow(List2)
#           f_object.close()
#     k+=1


# # from email.mime.multipart import MIMEMultipart
# # from email.mime.application import MIMEApplication
# # from email.mime.text import MIMEText
# # import email, smtplib, ssl
# # from email import encoders
# # from email.mime.base import MIMEBase

# # import smtplib

# # def send_email():                                                                           # Function to send email to cs3842022@gmail.com
# #         try:
# #             subject = "Consolidated Attendace Report"                                           
# #             body = "The report is attached with this mail."
# #             sender_email = input("Enter sender email : ")                                       # Sender e-mail
# #             receiver_email = "parashuramyadav670@gmail.com"                                        # Receiver e-mail => cs3842022@gmail.com
# #             password = input("Type your password and press enter:")                             # Password of sender e-mail

# #             # Create a multipart message and set headers
# #             message = MIMEMultipart()                                                       
# #             message["From"] = sender_email
# #             message["To"] = receiver_email
# #             message["Subject"] = subject
# #             message["Bcc"] = receiver_email  # Recommended for mass emails

# #             # Add body to email
# #             message.attach(MIMEText(body, "plain"))

# #             filename = "output\Attendance_report_consolidated.csv"  # In same directory as script

# #             # Open csv file in binary mode
# #             with open(filename, "rb") as attachment:
# #                 # Add file as application/octet-stream
# #                 # Email client can usually download this automatically as attachment
# #                 part = MIMEBase("application", "octet-stream")
# #                 part.set_payload(attachment.read())

# #             # Encode file in ASCII characters to send by email    
# #             encoders.encode_base64(part)

# #             # Add header as key/value pair to attachment part
# #             part.add_header(
# #                 "Content-Disposition",
# #                 f"attachment; filename= {filename}",
# #             )
# #             # Add attachment to message and convert message to string
# #             message.attach(part)
# #             text = message.as_string()

# #             # Log in to server using secure context and send email
# #             context = ssl.create_default_context()
# #             with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
# #                 server.login(sender_email, password)
# #                 server.sendmail(sender_email, receiver_email, text)
# #         except:
# #             print("Error in sending the file.")
# # send_email()
# # tbvvrtbtmqivlliq