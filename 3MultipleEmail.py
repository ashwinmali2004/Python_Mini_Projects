import smtplib as s
ob = s.SMTP('smtp.gmail.com',535)
ob.ehlo()
ob.starttls()
ob.login('rajdharohar24@gmail.com',"******")
subject="test python"
body="I Love Python"
message="subject:{}\n\n{}".format(subject,body)
ob.sendmail('rajdharohar24@gmail.com','ashwinmali2004@gmail.com',message)
print("send mail")
ob.quit()
# It will show first connection failed!!!