# Longevity
# Demonstrates text and entry widgets, and the grid layout manager

from tkinter import *

class Application(Frame):
    """ GUI application which can reveal the secret of longevity. """ 
    def __init__(self, master):
        """ Initialize the frame. """
        super(Application, self).__init__(master)  
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create button, text, and entry widgets. """
        # create instruction label

        self.bttn1 = Button(self, text = "row=0,column=0")
        self.bttn1.grid(row = 0, column = 0)

        self.bttn2 = Button(self, text = "row=0,column=1")
        self.bttn2.grid(row = 0, column = 1)

        self.bttn3 = Button(self, text = "row=0,column=2")
        self.bttn3.grid(row = 0, column = 2)

        self.bttn4 = Button(self, text = "row=1,column=0")
        self.bttn4.grid(row = 1, column = 0)

        self.bttn5 = Button(self, text = "row=1,column=1")
        self.bttn5.grid(row = 1, column = 1)

        self.bttn6 = Button(self, text = "row=1,column=2")
        self.bttn6.grid(row = 1, column = 2)     

      

    def reveal(self):
        """ Display message based on password. """
        contents = self.pw_ent.get()
        if contents == "secret":
            message = "Here's the secret to living to 100: live to 99 " \
                      "and then be VERY careful."            
        else:
            message = "That's not the correct password, so I can't share " \
                      "the secret with you."
        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, message)

# main
root = Tk()
root.title("Longevity")
root.geometry("300x150")

app = Application(root)

root.mainloop()
