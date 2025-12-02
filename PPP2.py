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

happiness = 0
class Pet: 
    def __init__(self, name, happiness):
        self.name == name
        self.__happiness == happiness

    def play(happiness):
        playIn = input("Enter in any text to increase the happiness: ")
    
    def show_status():
        print(happiness)

