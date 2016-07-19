from Tkinter import *

class Application(Frame):  

    def createWidgets(self):
     
        topContainer = Frame(root, padx=30, pady=5)
        bottomContainer = Frame(root, padx=30, pady=5)
        leftFrame = Frame(topContainer, padx=30, pady=30)
        centralFrame = Frame(topContainer, padx=30, pady=30)
        rightFrame = Frame(topContainer, padx=30, pady=30)
        bottomFrame = Frame(bottomContainer, padx=30, pady=30)

        #left side
        #List of victims
        leftTopFrame = Frame(leftFrame, padx=30, pady=30)
        leftBottomFrame = Frame(leftFrame, padx=30, pady=30)        

        #left top frame
        leftTopTitle = Entry(leftFrame, width=35)
        leftTopTitle.insert(0, "LIST OF VICTIMS")
        leftTopTitle.configure(state='readonly')

        leftTopLb = Listbox(leftTopFrame, height=23, width=40)
        leftTopLb.insert(END, "first")
        leftTopLb.insert(END, "second")
        leftTopLb.insert(END, "third")
        leftTopLb.insert(END, "fourth")        


        leftTopSb = Scrollbar(leftTopFrame, orient=VERTICAL)

        leftTopSb.configure(command=leftTopLb.yview)
        leftTopLb.configure(yscrollcommand=leftTopSb.set)

            
        #left bottom frame

        leftBottomBt = Button(leftBottomFrame, text="Update", bg="gray", fg="black", padx=12, pady=7)

        
        #left pack
        leftTopTitle.pack(side=TOP)
        leftTopLb.pack(side=LEFT)
        leftTopSb.pack(side=LEFT, fill=Y)
        leftBottomBt.pack(side=LEFT)
        leftTopFrame.grid(row=0, column=0)
        leftTopFrame.pack(side=TOP)
        leftBottomFrame.grid(row=1, column=0)
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
        centralTopLb.insert(END, "result.txt")
        centralTopLb.insert(END, "fbi.jpg")
        centralTopLb.insert(END, "confidential.doc")
        centralTopLb.insert(END, "result2.txt")        


        centralTopSb = Scrollbar(centralTopFrame, orient=VERTICAL)

        centralTopSb.configure(command=centralTopLb.yview)
        centralTopLb.configure(yscrollcommand=centralTopSb.set)

        #central bottom Frame


        centralBottomBt = Button(centralBottomFrame, text="Open Folder", bg="gray", fg="black", padx=12, pady=7)

        
        #central pack
        centralTopTitle.pack(side=TOP)
        centralTopLb.pack(side=LEFT)
        centralTopSb.pack(side=LEFT, fill=Y)
        centralBottomBt.pack(side=LEFT)
        centralTopFrame.grid(row=0, column=0)
        centralTopFrame.pack(side=TOP)
        centralBottomFrame.grid(row=1, column=0)
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
        rightTopLb.insert(END, "cd Documents")
        rightTopLb.insert(END, "dir")
        rightTopLb.insert(END, "cd Documents/confidential")
        rightTopLb.insert(END, "dir")    

        rightTopSb = Scrollbar(rightTopFrame, orient=VERTICAL)

        rightTopSb.configure(command=rightTopLb.yview)
        rightTopLb.configure(yscrollcommand=rightTopSb.set)

        #right bottom Frame
        #next command

        rightBottomTitle = Entry(rightBottomFrame, width=35)
        rightBottomTitle.insert(0, "NEXT COMMAND")
        rightBottomTitle.configure(state='readonly')

        rightBottomText = Text(rightBottomFrame, height=9, width=35)

        rightBottomBt = Button(rightBottomFrame, text="Execute", bg="gray", fg="black", padx=12, pady=7)
        
        #right pack       
                
        rightBottomBt.pack(side=BOTTOM, pady=15)
        rightBottomText.pack(side=BOTTOM)  
        rightBottomTitle.pack(side=BOTTOM, pady=20)               
        rightTopTitle.pack(side=TOP)        
        rightTopLb.pack(side=LEFT)
        rightTopSb.pack(side=LEFT, fill=Y)        
        rightTopFrame.grid(row=0, column=0)
        rightTopFrame.pack(side=TOP)
        rightBottomFrame.grid(row=1, column=0)
        rightBottomFrame.pack(side=BOTTOM)
        rightFrame.pack(side=LEFT)    



        #Bottom side

        bottomBottomBt = Button(bottomFrame, text="CHECK MALWARE STATUS", bg="gray", fg="black", padx=12, pady=7)
        bottomBottomTitle = Entry(bottomFrame, width=35)
        bottomBottomTitle.insert(0, "STATUS")
        bottomBottomTitle.configure(state='readonly', fg="red")

        bottomBottomBt.pack(side=TOP)
        bottomBottomTitle.pack(side=BOTTOM, padx=30, pady=30)
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
