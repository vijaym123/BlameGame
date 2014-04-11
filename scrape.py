import gmail
import re
import os

def loginGmail(filename):
	f = open(filename,"r")
	username, password = f.read().split('\n')
	gKey = gmail.login(username, password)
	return gKey

def filterBody(string):
	string = re.sub(r'<https?://[^>]+>',"",string)
	string = re.sub(r'Click here[^\d]+window',"",string)
	string = re.sub(r'Click here[^\d]+email',"",string)
	return string

def writeToFile(data):
	for mail in data:
		dirname = mail.fr.split('<')[1].split('@')[0]
		filename = str(mail.sent_at).replace("-","").replace(" ","").replace(":","") + ".txt"
		dirpath = os.path.dirname(dirname+"/"+filename)
		if not os.path.exists(dirpath) :
			os.makedirs(dirpath)
		f = open( dirpath + "/" + filename ,"w")
		line = mail.fr + "\n" + str(mail.sent_at) + "\n" + mail.body + "\n"
		f.write(filterBody(line))
	return True

if __name__ == "__main__":
	gKey = loginGmail("accountDetails")
	sender = "MD06JDIMA@mail.house.gov"
	mails=gKey.inbox().mail(sender=sender,prefetch=True)
	writeToFile(mails)

