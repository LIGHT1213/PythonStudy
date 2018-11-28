# Property Critter
# Demonstrates properties

class Critter(object):
    """A virtual pet"""
    def __init__(self, name):
        print("A new critter has been born!")
        self.__name = name

    @property
    def name1(self):
        return self.__name
    
    @name1.setter
    def name2(self, new_name):
        if new_name == "":
            print("A critter's name can't be the empty string.")
        else:
            self.__name = new_name
            print("Name change successful.")

    def talk(self):
        print("\nHi, I'm", self.name1)

# main
crit = Critter("Poochie")
crit.talk()

print("\nMy critter's name is:", end= " ")
print(crit.name1)

print("\nAttempting to change my critter's name to Randolph...")
crit.name2= "Randolph"
print("My critter's name is:", end= " ")
print(crit.name1)

print("\nAttempting to change my critter's name to the empty string...")
crit.name2 = ""
print("My critter's name is:", end= " ")
print(crit.name1)

input("\n\nPress the enter key to exit.")
