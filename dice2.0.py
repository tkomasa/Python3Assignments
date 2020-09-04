# More advanced version of dice.py, after learning more
import random

# Beginning prompt
print('''       ________            
      /\       \           
     /()\   ()  \          
    /    \_______\         
    \    /()     /         
     \()/   ()  /          
      \/_____()/
    ''')
print("Welcome to dice2.0.py. \nThis short project takes your inputs and rolls the dice. \nEnjoy.")


# Rolls the die based upon input of size and amount
def roll(x, y):
    global rand
    rand = random.sample(range(1, x), y)

    # Stripping brackets from roll list
    rand_sans = str(rand)[1:-1]

    # To find the total
    total = 0
    for num in range(0, len(rand)):
        total = total + rand[num]

    # Print rolls and play again
    print("\nRoll(s):", rand_sans)
    print("Total:", total)
    again = input("\nWould you like to roll again? (yes or no): ")
    if again.__contains__("yes"):
        prompt()

    if again.__contains__("no"):
        exit()
    return


# Asks player what kind of dice they would like to roll and stores that info for the roll function
def prompt():
    global int_amount
    global int_size
    amount = input("\nPlease enter the amount of di(c)e you would like to roll: ")
    size = input("Please indicate the size of your di(c)e: ")
    if amount.isdigit() and size.isdigit():
        int_size = int(size)
        int_amount = int(amount)
        if int_amount >= int_size:
            print("\n!!!The amount of dice cannot be larger-than/equal-to the size of dice. Please try again!!!")
            prompt()
        if int_amount < int_size:
            roll(int_size, int_amount)
        return
    else:
        print("\nThose are not numbers, please input again.")
        prompt()
        return


prompt()
