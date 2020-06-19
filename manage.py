import smtplib
import subprocess as sp
import datetime

servers = []
serverisdown = []
timeping = datetime.datetime.now()

with open('servers.txt', mode='r', encoding='utf-8') as listserver:
    for itemserver in listserver:
        servers.append(itemserver.split()[0])

for ipaddress in servers:
    status,result = sp.getstatusoutput("ping -c 4 " + ipaddress)
    if status == 0:
        with open("control.txt", "a") as text_file:
            text_file.write(ipaddress + " Funciona correctamente - " + str(timeping) + "\n")
    else:
        serverisdown.append(ipaddress)
        with open("control.txt", "a") as text_file:
            text_file.write(ipaddress + " No funciona correctamente - " + str(timeping) + "\n")

sender = "server.status@grupopublimovil.com"
receiver = "help.desk@grupopublimovil.com"
separator = ',\n'
serv = separator.join(serverisdown)
message = f"""\
Subject: Estado de servidores
To: {receiver}
From: {sender}

Los siguientes servidores no responden \n
{serv} """

with smtplib.SMTP("mail.grupopublimovil.net", 587) as server:
    if len(serverisdown) > 0:
        server.starttls()
        server.login("server.status@grupopublimovil.com", "4ppM0v1l")
        server.sendmail(sender, receiver, message)