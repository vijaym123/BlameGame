import gmail
import string


def loginGmail(filename):
	f = open(filename,"r")
	username, password = f.read().split('\n')
	gKey = gmail.login(username, password)
	return gKey

gKey = loginGmail("accountDetails")
mails=gKey.inbox().mail(sender="MD06JDIMA@mail.house.gov",prefetch=True)

for i in mails:
	print i.fr
	print str(i.sent_at)
	print i.body