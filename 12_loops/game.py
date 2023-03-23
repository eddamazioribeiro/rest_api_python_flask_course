secret_number = 8

while True:
  user_input = input("Enter 'Y' if you would like to play a game:\n>> ").lower()

  if user_input == 'n':
    break

  user_guess = int(input("Guess the secret number:\n>> "))

  if user_guess == secret_number:
    print("You guessed correctly! You won!\n")
    break
  elif abs(secret_number - user_guess) in (1, -1):
    print("You're close, try again\n") 
  else:
    print("Sorry, it's wrong\n")
