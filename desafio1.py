
import csv
csvarray = []
def lercsv():
    with open('usuarios.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            csvarray.append(row)

    return csvarray

import string
import random
special_char = "!@%/()=?"

def randompassword():
    chars=string.ascii_uppercase + string.ascii_lowercase + string.digits + special_char
    size=4
    return ''.join(random.choice(chars) for x in range(size,12))

def criarsenha():
    i = 1
    while (i <= (len(csvarray)-1)):
        csvarray[i].insert(len(csvarray[0]),randompassword())
        i += 1

import smtplib

def enviaremail():
    i = 1
    # Credenciais
    remetente    = 'contadeemail@gmail.com'
    senha        = 'SenhadoEMAIL'
 
    # Informações da mensagem
    while (i <= (len(csvarray)-1)):
        destinatario = csvarray[i][3]
        assunto      = 'Usuario e Senha'
        texto        = ("Seu usuario : " + csvarray[i][2] + " e sua senha : " + csvarray[i][4] )

        # Preparando a mensagem
        msg = '\r\n'.join([
        'From: %s' % remetente,
        'To: %s' % destinatario,
        'Subject: %s' % assunto,
        '',
        '%s' % texto
        ])
        i += 1
        # Enviando o email
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(remetente,senha)
        server.sendmail(remetente, destinatario, msg)
    server.quit()

lercsv()
criarsenha()
enviaremail()