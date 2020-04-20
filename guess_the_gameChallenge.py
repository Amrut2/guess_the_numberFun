import random

print("GUESS THE NUMBER CHALLENGE ")
print(" -*-*-*-*-*-*-*-*-*-*-*-")

def guess():
  a=int(input("\nguess the number : "))
  number = (random.randint(0,100))
  if (a == number):
    print("Your right congrats")
    print(number)

    print(" o   o   o  ")
    print("\ / \ / \ / ")
    print(" |   |   |  ")
    print("/ \ / \ / \ ")

  elif(a<number):
    print("little more")
    print(number)

    print(" o   o   o  ")
    print("\|  \|  \|   ")
    print(" |\  |\  |\ ")
    print("/ \ / \ / \ ")

  else:
    print("little less")
    print(number)

    print(" o   o   o  ")
    print("/|\ /|\ /|\ ")
    print(" |   |   |  ")
    print("/ \ / \ / \ ")

guess()
