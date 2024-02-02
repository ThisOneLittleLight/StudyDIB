class Character:
    name = "undefined"
    health = 0
    damage = 0

    #We first set all the stats in the constructor
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    #This function decreases the health by the amount
    def hit(self, amount):
        self.health = self.health - amount
    
    #This function takes a character that we want to attack and calls their hit function
    def attack(self, char):
        char.hit(self.damage)   #Call the chars hit function and give it the classes damage

        #This is just to organize the console
        print(self.name, " attacked ", char.name)
        print("")
    
    #Print the stats of the character
    def print_stats(self):
        print(self.name,"'s stats are:")
        print("HEALTH: ", self.health, " DAMAGE: ", self.damage)
        print("")

        

class Player(Character):
    inventory = []
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)

class Enemy(Character):
    battlecry = ""
    def __init__(self, name, health, damage, battlecry):
        super().__init__(name, health, damage)
        self.battlecry = battlecry
    
    def cry_battlecry(self):
        print(self.name, " screams: ", self.battlecry)
        print("")


player = Player("Player" ,10, 4)
enemy = Enemy("Enemy", 4, 1, "REEEEEEEEEEEE")

enemy.cry_battlecry()
enemy.print_stats()

player.attack(enemy)

enemy.print_stats()