import smtplib
import os
import datetime

servers = ['192.168.50.163','192.168.50.147']
serverisdown = []
timeping = datetime.datetime.now()

for ipaddress in servers:
    response = os.system('ping -n 4 {}' . format(ipaddress))
    if response == 0:
        with open("control.txt", "a") as text_file:
            text_file.write(ipaddress + " Funciona correctamente - " + str(timeping) + "\n")
    else:
        serverisdown.append(ipaddress)
        with open("control.txt", "a") as text_file:
            text_file.write(ipaddress + " No funciona correctamente - " + str(timeping) + "\n")

sender = "script <python@grupopublimovil.com>"
receiver = "for person <help.desk@grupopublimovil.com>"
separator = ',\n'
serv = separator.join(serverisdown)
message = f"""\
Subject: Estado de servidores
To: {receiver}
From: {sender}

Los siguientes servidores no responden \n
{serv} """

with smtplib.SMTP("smtp.mailtrap.io", 25) as server:
    if len(serverisdown) > 0:
        server.login("250696872927da", "30c17c4bc21b1f")
        server.sendmail(sender, receiver, message)