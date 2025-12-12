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
increase = 0
class Pet: 
    def __init__(self, name, happiness):
        self.name == name
        self.__happiness == happiness
    
    def show_status(self):
        print(f"Your pet's happiness is {happiness}.")



    def play(self,increase):

        increase = input("To play with your pet (like a good person), enter Y. To commit animal abuse, enter N.")



    def sleep(self):
        print("test")
        

Pet("Bob",11)
Pet.play(5)



# 6767676767676767676767
# Pet.play(5)
# Pet.show_status()

# pet = ("Johnny",0)
# Pet.play(int(input("How long did you play for: ")))

