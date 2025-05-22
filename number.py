import random

def easy_level(c_guess):
   chances = 0
   while chances < 10:
      u_guess = int(input(f"Enter your number: "))
      if u_guess == c_guess:
         attempts = chances+1
         print(f"Congratulations, you have guessed the correct number after {attempts} attempts.")
         break
      elif u_guess != c_guess:
         if c_guess < u_guess:
            print("The number is less than your guess.")
         elif c_guess > u_guess:
            print("The number is greater than your guess.")
         else:
            print("You have entered an invalid number.")
            exit
      chances += 1
   else:
      print("Sorry, you lost. After 10 attempts.")


def medium_level(c_guess):
   chances = 0
   while chances < 5:
      u_guess = int(input(f"Enter your number: "))
      if u_guess == c_guess:
         attempts = chances+1
         print(f"Congratulations, you have guessed the correct number after {attempts} attempts.")
         break
      elif u_guess != c_guess:
         if c_guess < u_guess:
            print("The number is less than your guess.")
         elif c_guess > u_guess:
            print("The number is greater than your guess.")
         else:
            print("You have entered an invalid number.")
            exit
      chances += 1
   else:
      print("Sorry, you lost. After 5 attempts.")

def hard_level(c_guess):
   chances = 0
   while chances < 3:
      u_guess = int(input(f"Enter your number: "))
      if u_guess == c_guess:
         attempts = chances+1
         print(f"Congratulations, you have guessed the correct number after {attempts} attempts.")
         break
      elif u_guess != c_guess:
         if c_guess < u_guess:
            print("The number is less than your guess.")
         elif c_guess > u_guess:
            print("The number is greater than your guess.")
         else:
            print("You have entered an invalid number.")
            break
      chances += 1
   else:
      print("Sorry, you lost. After 3 attempts.")

      
def main():
   print("Welcome to the number game. \n You will have to select the level of the game you want. \n If you select level 1 (Easy) you have 10 chances to guess \n if you select level 2 (Medium) you have 5 chances \n and if you select level 3 (Hard) you have 3 chances.")

   print("Choose a level")
   print("1. Easy")
   print("2. Medium")
   print("3. Hard")

   level = int(input(f"Choose a level (1,2 or 3): "))
   c_guess = random.randint(1, 9)

   if level == 1:
      easy_level(c_guess)
   elif level == 2:
      medium_level(c_guess)
   elif level == 3:
      hard_level(c_guess)
   else:
      print("Choose a valid level.")
      exit
   
if __name__ == "__main__":
   main()


