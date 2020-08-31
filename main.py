#import required modules 
import smtplib 
  
# list of email_id to send the mail 
li = ["test@gmail.com","test2@gmail.com"] 
  
for dest in li: 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login("your_mail@gmail.com", "your_password") 
    message = "Message_you_need_to_send"
    s.sendmail("sender_email_id", dest, message) 
    s.quit() 
