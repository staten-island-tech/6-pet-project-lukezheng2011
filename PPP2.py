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

    # def show_status2(self):
    #     if self.__happiness >=100:
    #         print("The end. You've made your pet very happy!")
    #         self.unhappy=1
    #     print(f"{self.name}'s happiness is {self.__happiness}. To be a good boy, make it happier or put it to sleep!")


#         actions:





class Pet:
    def __init__(self, name, happiness,tired):
        self.name = name
        self.__happiness = happiness
        self.__tired = tired
        self.hasWon = False

    def show_status1(self):
        print(f"{self.name}'s happiness is {self.__happiness}.")
        print(f"Your pet's sleepiness level is {self.__tired}")
        print("  ")
      


    def play(self):
        play1 = input("To play with your pet, enter Y. To be an abusive owner, enter N: ")

        if play1.upper() == "Y":
            self.__happiness += 5
            self.__tired += 1
        elif play1.upper() == "N":
            self.__happiness -= 50
    
    def feed(self):
        feed1 = input("If you're gonna feed your pet like a good boy, enter Y. To be an abusive owner, enter N: ")

        if feed1.upper() == "Y":
            option = int(input("What would you like your pet to eat? Enter 1 to feed a luxurious steak dinner, 2 to feed canned dog food, 3 to feed fresh vegetables, and 4 to feed sleep pills: "))
            if option == 1: 
                self.__happiness += 30
                self.__tired += 1
            elif option == 2:
                self.__happiness += 5
                self.__tired += 1
            elif option == 3:
                self.__happiness += 10
                self.__tired += 1
            elif option == 4:
                self.__happiness -= 100
                self.__tired += 10
                print("You've put your pet to sleep, you evil being.")
            
        elif feed1.upper() == "N":
            self.__happiness -= 5

    def sleep(self):
        print("Your pet is too sleepy!")
        sleep1 = input("To put your pet to sleep, enter Y. To be an abusive owner, enter N: ")

        if sleep1.upper() == "Y":
            self.__tired = 0
            
        elif sleep1.upper() == "N":
            self.__tired = 10 

    def is_tired(self):
        return self.__tired > 9 #used chatgpt to do this part - still not completely sure why it works
    
    def victory(self):
        if self.__happiness > 200:
            print("Your pet's happpiness has exceeded 200! You've won!")
            self.hasWon = True
            
            
          


pet = Pet(input("What's your pet's name: "),0,0)



pet.show_status1()


while not pet.hasWon:
    nextAction = int(input("Enter 1 to play with your pet, and 2 to feed it: "))

    if nextAction == 1 and not pet.is_tired():
        pet.play()
        pet.show_status1()
    elif nextAction == 2 and not pet.is_tired():
        pet.feed()
        pet.show_status1()
    else:
        pet.sleep()
        pet.show_status1()

    






