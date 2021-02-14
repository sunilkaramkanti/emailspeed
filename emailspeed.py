import speedtest
import smtplib
def sendspeed():
    st =speedtest.Speedtest()

    d=st.download()
    u=st.upload()
    servernames =[]
    st.get_servers(servernames)
    ping= st.results.ping
    return (d,u,ping)
x = sendspeed()

to = input("enter the recipient email:\n")

content = str(x[0])+"\n"+str(x[1])+"\n"+str(x[2])

def sendemail(to,content):
    server= smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("your_email","password") #your email and password
    server.sendmail("your_email",to,content) #your email, recipient, content you want to send
    server.close()
sendemail(to,content)
