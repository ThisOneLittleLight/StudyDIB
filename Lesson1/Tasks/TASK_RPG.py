#NR 1)
#Create a class named "Character" that has the following attributes
#name
#health
#damage
#
#And set those in the constructor

#NR 2)
#Create 2 functions inside the Character class
#
#The first is a hit function that takes the amount of damage and substracts it from the health
#
#The second is an attack function that takes the character to attack and calls their hit function
#
#The third is to print its stats to the console (health and damage)

#NR 3)
#Create a player class that inherits from Character
#
#The player has an inventory attribute which is a list containing the items (With items I just mean Strings that depict what would be real Item names in a real game)
#
#Now add a function that adds a item to the inventory. It should take a string as an agrument to add to the list
#
#Add a print_inventory function that prints every item of the player

#NR 4)
#Create an Enemy class that has a battle cry varible
#
#Set the battle cry variable in the enemies constructor (Make sure everything else is still set from the Character class HINT: use super.)
#
#Create a function for the enemy to shout out its battle cry to the console

#NR 5)
#Now test out your program in the following way:
#   -The Enemy shouts its battlecry
#   -The Enemies stats are printed
#   -The Player attacks the Enemy
#   -The Enemies stats are printed again
#   -The Player gets two items dropped (added to the inventory)
#   -Print the players inventory