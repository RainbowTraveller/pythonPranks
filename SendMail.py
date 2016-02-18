import smtplib
from email.mime.text import MIMEText

msg = MIMEText("This is Test mail from python")

#me = "GreenMeadow"
me  = ""
you = ""
msg['Subject'] = "Test mail from python script"
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server, but don't include the
# envelope header.
#s = smtplib.SMTP('localhost', 1025)
s = smtplib.SMTP('smtp.saavn.com', 25)
s.sendmail(me, [you], msg.as_string())
s.quit()
