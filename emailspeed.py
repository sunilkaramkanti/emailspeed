import speedtest
import smtplib
def sendspeed():
    st =speedtest.Speedtest()
    print(st)
    print(st.download())
    print(st.upload())
    servernames =[]
    st.get_servers(servernames)
    print(st.results.ping)

sendspeed()
