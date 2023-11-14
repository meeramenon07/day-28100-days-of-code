print("Character Builder")
import random,os,time
def rollDice(side):
 result = random.randint(1,side)
 return result
def health():
  healthStat = ((rollDice(6) * rollDice(12))/2) + 10
  return healthStat
def strength():
  strengthStat = ((rollDice(6)*rollDice(8))/2) + 12
  return strengthStat
print("It's time for Battle!")
print()

#character creation
char1_name = input("Name your legend")
char1_type = input("character type(Human,Elf,Wizard,Orc)\n")
print()
print(char1_name)
char1_health = health()
char1_strength = strength()
print("Health",char1_health)
print("Strength", char1_strength)
print()
print("Who are they battling with?")
print()
char2_name = input("Name your Legend: \n")
char2_type = input("character type(Human,Elf,Wizard,Orc)\n")
print()
print(char2_name)
char2_health = health()
char2_strength = strength()
print("Health", char2_health)
print()
print("Strength", char2_strength)
print()
round = 1
winner = None

while True:
  time.sleep(1)
  os.system("clear")
  print("Battle time!")
  print()
  print("The battle begins!")
  char1_dice = rollDice(6)
  char2_dice = rollDice(6)
  difference = abs(char1_strength - char2_strength) + 1
  if char1_dice > char2_dice:
   char2_health -= difference
   if round == 1:
   
    print(char1_name, "wins the first blow!")
   else:
    print(char1_name, "wins round", round)
  elif char2_dice > char1_dice:
    char1_health -= difference
    if round == 1:
      print(char2_name, "wins the first blow!")
    
    else:
      print(char2_name, "wins the round", round)
  else:
    print("They draw a round",round)
  print()
  print(char1_name)
  print("Health",char1_health)
  print()
  print(char2_name)
  print("Health",char2_health)
  print()
  if char1_health <= 0:
    print(char1_name,  "has died")
    winner = char2_name
    break
  elif char2_health <= 0:
   
    
    print(char2_name, "has died ")
    winner = char1_name
    break

  else:
    print("Both continuebto play for next round")
    round += 1

  time.sleep(1)
  os.system("clear")
  print("battle time")
  print()
  print(winner,"has won in",round,"rounds")

     
  








  
  




  
  
  
  
     
      