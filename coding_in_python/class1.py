#! /usr/bin/env python3

class GameCharacter:
     def __init__(self, name, life):
         self.name = name
         self.life = life

     def attack(self):
         print(self.name + " kicks the enemy.")

     def life_check(self):
         if self.life <= 0:
             print(self.name + " was defeated.")
         else:
             print(self.name + " is still in the fight.")

class GameEnemy:
     def __init__(self, name, life):
         self.name = name
         self.life = life

     def attack(self):
         print(self.name + " attacks the heroes!")

     def life_check(self):
         if self.life <= 0:
             print(self.name + " was defeated.")
         else:
             print(self.name + " is still in the fight.")

def attack_enemy(enemy, damage):
     print(enemy.name + " attacks!")
     enemy.life -= damage
     print(enemy.name + " takes " + str(damage) + " damage, and has " + str(enemy.life) + " life remaining.")
     enemy.life_check()

def attack_player(player, damage):
     print(player.name + " attacks!")
     player.life -= damage
     print(player.name + " takes " + str(damage) + " damage, and has " + str(player.life) + " life remaining.")
     player.life_check()

# Initialize player and enemy
player1 = GameCharacter("Mario", 100)
enemy1 = GameEnemy("Bowser", 150)

# Battle
attack_enemy(enemy1, 60)
attack_player(player1, 60)
attack_enemy(enemy1, 40)
attack_player(player1, 40)
attack_enemy(enemy1, 50)
