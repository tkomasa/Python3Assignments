from random import randint

# Welcome message
print("Greetings, traveller! Perhaps you would like to play a game of chance?")
print("\nPlease select how many sides you would like your die to have. You can even choose dice that are"
      "\nimpossible in the real world!")

# Input dice size
sides = int(input("\nNumber of sides: "))

# Create and print random roll
# randint is imported from random module: randint(minVal, maxVal)
roll = randint(1, sides)
if roll == 20 and sides == 20:
    print("Critical Roll! You rolled a", roll)
else:
    print("\nYou rolled a", roll)

# Repeat structure
print("\nWould you like to roll again?")
again = int(input("Yes or No = 1 or 2: "))
while again == int(1):
    sides = int(input("\nNumber of sides: "))
    roll = randint(1, sides)
    if roll == 20 and sides == 20:
        print("Critical Roll! You rolled a", roll)
    else:
        print("\nYou rolled a", roll)

    print("\nWould you like to roll again?")
    again = int(input("Yes or No = 1 or 2: "))
if again == int(2):
    exit()
