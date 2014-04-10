import gmail
import string


def loginGmail(filename):
	f = open(filename,"r")
	username, password = f.read().split('\n')
	gKey = gmail.login(username, password)
	return gKey

def writeToFile(data,filename):
	f = open(filename,"w")
	line = ""
	for mail in data:
		line = line + mail.fr + "," + str(mail.sent_at) + "," + mail.body + "\n"
	f.write(line)
	return True

if __name__ == "__main__":
	gKey = loginGmail("accountDetails")
	sender = "MD06JDIMA@mail.house.gov"
	mails=gKey.inbox().mail(sender=sender,prefetch=True)
	writeToFile(mails,"test.csv")

