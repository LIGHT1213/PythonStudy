# Mad Lib
# Create a story based on user input

from tkinter import *
money=0

class Application(Frame):
    """ GUI application that creates a story based on user input. """
    def __init__(self, master):
        """ Initialize Frame. """
        super(Application, self).__init__(master)  
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create widgets to get story information and to display story. """
        # create instruction label
        Label(self,
              text = "Enter information to order"
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)

        # create a label and text entry for the name of a person
        Label(self,
              text = "Your Name: "
              ).grid(row = 1, column = 0, sticky = W)
        self.person_ent = Entry(self)
        self.person_ent.grid(row = 1, column = 1, sticky = W)

        # create a label and text entry for a plural noun
        Label(self,
              text = "Mr or miss/mis"
              ).grid(row = 2, column = 0, sticky = W)
        self.noun_ent = Entry(self)
        self.noun_ent.grid(row = 2, column = 1, sticky = W)

        # create a label and text entry for a verb
        Label(self,
              text = "sit"
              ).grid(row = 3, column = 0, sticky = W)
        self.verb_ent = Entry(self)
        self.verb_ent.grid(row = 3, column = 1, sticky = W)
     
        # create a label for adjectives check buttons
        Label(self,
              text = "meat"
              ).grid(row = 4, column = 0, sticky = W)

        # create itchy check button
        self.is_itchy = BooleanVar()
        Checkbutton(self,
                    text = "pork",
                    variable = self.is_itchy
                    ).grid(row = 4, column = 1, sticky = W)

        # create joyous check button
        self.is_joyous = BooleanVar()
        Checkbutton(self,
                    text = "fish",
                    variable = self.is_joyous
                    ).grid(row = 4, column = 2, sticky = W)

        # create electric check button
        self.is_electric = BooleanVar()
        Checkbutton(self,
                    text = "beef",
                    variable = self.is_electric
                    ).grid(row = 4, column = 3, sticky = W)

        # create a label for body parts radio buttons
        Label(self,
              text = "vegetble"
              ).grid(row = 5, column = 0, sticky = W)

        # create variable for single, body part
        self.body_part = StringVar()
        self.body_part.set(None)
  
        # create body part radio buttons
        body_parts = ["cabbage", "carrot", "potato"]
        column = 1
        for part in body_parts:
            Radiobutton(self,
                        text = part,
                        variable = self.body_part,
                        value = part
                        ).grid(row = 5, column = column, sticky = W)
            column += 1

        # create a submit button
        Button(self,
               text = "How much is it",
               command = self.tell_story
               ).grid(row = 6, column = 0, sticky = W)

        self.story_txt = Text(self, width = 75, height = 10, wrap = WORD)
        self.story_txt.grid(row = 7, column = 0, columnspan = 4)

    def tell_story(self):
        """ Fill text box with new story based on user input. """
        # get values from the GUI
        person = self.person_ent.get()
        noun = self.noun_ent.get()
        verb = self.verb_ent.get()
        money=0
        adjectives = ""
        if self.is_itchy.get():
            adjectives += "pork, "
            money+=10
        if self.is_joyous.get():
            adjectives += "fish, "
            money+=15
        if self.is_electric.get():
            adjectives += "beaf, "
            money+=20
        body_part = self.body_part.get()
        if body_part =="cabbage":
            money+=5
        elif body_part =="carrot":
            money+=6
        elif body_part =="potato":
            money+=7
        # create the story
        story = noun
        story += " "+person
        story += " you had took meat incloude"
        story += adjectives
        story += " you had took vegetable incloude"
        story += body_part
        story += "you should sit in "+verb
        story += " it will took you "
        story += str(money)+"YUAN"
        '''
        story += "A strong, "
        story += adjectives
        story += "peculiar feeling overwhelmed the explorer. "
        story += "After all this time, the quest was finally over. A tear came to "
        story += person + "'s "
        story += body_part + ". "
        story += "And then, the "
        story += noun
        story += " promptly devoured "
        story += person + ". "
        story += "The moral of the story? Be careful what you "
        story += verb
        story += " for."
        '''
        # display the story                                
        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)

# main
money =0
root = Tk()
root.title("Mad Lib")
app = Application(root)
root.mainloop()
