# class Hero:
#     def __init__(self, name, money, inventory):
#         self.name = name
#         self.money = money
#         self.inventory = inventory

#     def buy(self, item):
#         self.inventory.append(item)
#         print(self.inventory)

# Billybob = Hero("Billybob", 67, ['Johnnys Shoes', 'Williams Backpack'])

# Billybob.buy(input("What items would you like to add to Billybob's inventory: "))

#---------------------------------------------------------------------------------------
# Create a class Pet that has:

# A name
# A private variable for happiness level (e.g., __happiness)

# A method to play() that increases happiness
# A method to show_status() that prints how happy the pet is

class Pet:
    def __init__(self, name, happiness):
        self.name = name
        self.__happiness = happiness

    def show_status(self):
        print(f"{self.name}'s happiness is {self.__happiness}.")

    def play(self):
        willPlay = input(
            "To play with your pet, enter Y. To be an abusive owner, enter N: "
        )

        if willPlay.upper() == "Y":
            self.__happiness += 5
        elif willPlay.upper() == "N":
            self.__happiness -= 5

    def sleep(self):
        self.__happiness += 67

pet = Pet("Bob", 11)

unhappy = 0
while unhappy == 0:
    pet.show_status()
    pet.play()
    pet.show_status()




# 6767676767676767676767
# Pet.play(5)
# Pet.show_status()

# pet = ("Johnny",0)
# Pet.play(int(input("How long did you play for: ")))

