import StringIO, rfc822
import poplib
import string, random

servidor = "pop.gmail.com"
usuario  = "contadeemail@gmail.com"
pwd = "Senhadaconta"

conectar_srv = poplib.POP3_SSL(servidor)
conectar_srv.user(usuario)
conectar_srv.pass_(pwd)
resp, items, octets = conectar_srv.list()

i = 0
while(i <= (len(items)-1)):
    id, size = string.split(items[i])
    resp, text, octets = conectar_srv.retr(id)
    text = string.join(text, "\n")
    file = StringIO.StringIO(text)
    message = rfc822.Message(file)
    if "DevOps".lower() in message['Subject'].lower():
         print("Devops em Assunto")
         print(message['From'] +  '\n'),
         print(message['Subject'] + '\n'),
         print(message['Date'] + '\n'),
         print("*"*40) 
    elif "DevOps".lower() in message.fp.read().lower():
         print("Devops no Corpo")
         print(message['From'] +  '\n'),
         print(message['Subject'] + '\n'),
         print(message['Date'] + '\n'),
         print("*"*40) 
    i += 1

    


        