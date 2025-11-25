class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)

Billybob = Hero("Billybob", 67, ['Johnnys Shoes', 'Williams Backpack'])

Billybob.buy(input("What items would you like to add to Billybob's inventory: "))

