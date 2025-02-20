#! /usr/bin/env python3

class GameCharacter:
     def __init__(self, name, life):
          self.name = name
          self.life = life

     def life_check(self):
         if self.life <= 0:
              print(self.name + " was defeated.")
         else:
              print(self.name + " is still in the fight.")

class Player(GameCharacter):
     def attack(self):
          print(self.name + " kicks the enemy.")

class Enemy(GameCharacter):
     def attack(self):
          print(self.name + " breathes fire!")

def fight(character, target, damage):
     print("\n\n")
     character.attack()
     target.life -= damage
     print(target.name + " takes " + str(damage) + " damage")
     print(target.name + " has " + str(target.life) + " life remaining.")
     target.life_check()

# Initialize player and enemy
player1 = Player("Mario", 100)
enemy1 = Enemy("Bowser", 150)

# Battle
fight(player1, enemy1, 50)
fight(enemy1, player1, 20)
fight(player1, enemy1, 30)
fight(enemy1, player1, 40)
fight(player1, enemy1, 70)
