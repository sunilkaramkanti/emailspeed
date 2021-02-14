import speedtest
import smtplib
def sendspeed():
    st =speedtest.Speedtest()
    print(st.download())
    print(st.upload())
    servernames =[]
    st.get_servers(servernames)
    print(st.results.ping)
sendspeed()



to = input("enter the recipient email:\n")

content = input("enter the content:\n")

def sendemail(to,content):
    server= smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("your_email","password")
    server.sendmail("your_email",to,content)
    server.close()
sendemail(to,content)
