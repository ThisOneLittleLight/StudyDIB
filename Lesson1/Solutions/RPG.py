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
        char.hit(self.damage)
        print(self.name, " attacked ", char.name)
        print("")
    
    def print_stats(self):
        print(self.name,"'s stats are:")
        print("HEALTH: ", self.health, " DAMAGE: ", self.damage)
        print("")

        

class Player(Character):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)

class Enemy(Character):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)


player = Player("Player" ,10, 4)
enemy = Enemy("Enemy", 4, 1)

enemy.print_stats()

player.attack(enemy)

enemy.print_stats()