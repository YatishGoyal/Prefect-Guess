import random

def game():
  n = random.randint(1, 100)
  a = -1
  global guesses
  guesses = 0
  while(a != n):
    a = int(input("Guess The No.(1-100): "))
    if(a>n):
      print("Lower No. pls!")
      guesses+=1
    elif(n>a):
      print("Higher No pls!")
      guesses+=1
    elif(n==a):
     print(f"You Have Guessed The no in {guesses+1} attempt")
game()
while True:
   user = input("Do you want to continue the Game.\nYes/NO: ")

   if user.lower() == "yes":
      game()
   else:
     print("Bye")
     break
      