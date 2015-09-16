import mailbox
import time
import email.Header

def getFrom(text):
    text = text.replace("\n","")
    text = ''.join(text.split(r'\r'))
    name = text.split("<")[0].replace("\"","")
    try :
        email = text.split("<")[1].replace(">","")
    except IndexError:
        name = ""
        email = text.strip()
    return name + "`" + email

def getTo(text):
    if not(text):
        return "dj724530@gmail.com"
    if text.find("dj724530@gmail.com")>=0:
        return "dj724530@gmail.com"
    else:
        return text

def getDate(text):
    timeStr = ""
    if len(text.strip().split()) == 6 or len(text.strip().split()) == 7:
        timeStr = time.strftime("%d/%m/%Y",time.strptime('/'.join(text.strip().split()[1:4]), "%d/%b/%Y")) + "`" + text.strip().split()[4]
    elif len(text.strip().split()) == 5:
        timeStr = time.strftime("%d/%m/%Y",time.strptime('/'.join(text.strip().split()[0:3]), "%d/%b/%Y")) + "`" + text.strip().split()[3]
    elif len(text.strip().split()) == 2:
        timeStr = "`".join(text.strip().split())
    else:
        print text.split()
    return timeStr

def getNotNone(text):
    if not(text):
        return ""
    else:
        return text

count = 0
to="dj724530@gmail.com"
f = open("headers.txt","w")
mbox = mailbox.mbox('Inbox.mbox')

for message in mbox:
    textline=""
    textline+=email.Header.decode_header(getFrom(message["From"]))[0][0]+ "`"
    textline+=getTo(message["To"]) + "`"
    textline+=getDate(message["Date"]) + "`"
    textline+=email.Header.decode_header(message["Subject"])[0][0]+ "`"
    textline+='NP%05d' % count
    f.write(textline+"-|||||-");
    count+=1
f.close()

#textfile = " ".join(textfile.replace("^M$","").replace("\n","").split())