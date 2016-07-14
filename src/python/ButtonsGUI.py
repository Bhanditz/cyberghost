from Tkinter import *

class Application(Frame):
    def openFolder(self):
        print "hi there, everyone!"

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.openFolder = Button(self)
        self.openFolder["text"] = "Open Folder"
        self.openFolder["command"] = self.openFolder

        self.openFolder.pack({"side": "left"})

    def __init__(self, parent):
        Frame.__init__(self, parent, background = "white")
        self.parent = parent
        self.parent.title("Send Signal")
        self.pack(fill = BOTH, expand = 1)
        self.createWidgets()
        self.centerWindow()
        
#Centralizes the window        
    def centerWindow(self):
        w = 290
        h = 150
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d'% (w, h, x, y))

root = Tk()
app = Application(root)
app.mainloop()
root.destroy()
