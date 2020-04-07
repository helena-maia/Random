import smtplib
import numpy as np

fromaddr = 'helena.almaia@gmail.com'
subject = "[MC102] Acesso ao susy"
username = 'helena.almaia@gmail.com'
password = ''
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)

lines = np.loadtxt("semNomeN_senhas.txt", dtype=str, delimiter=':')

for l in lines:
	toaddrs  = l[2]
	text = "Prezad* "+l[1]+",\n\nPara utilizar o SuSy, identifique-se como:\n\tUsuario: "+l[0]+"\n\tSenha: "+l[3]+"\n\nAtt,\nHelena."
	print text
	msg = 'Subject: {}\n\n{}'.format(subject, text)
	server.sendmail(fromaddr, toaddrs, msg)
server.quit()	
