import random
n = random.randint(1, 100)

def game():
  a = -1
  global guesses
  guesses = 0
  while(a != n):
    a = int(input("Guess The No.: "))
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
      