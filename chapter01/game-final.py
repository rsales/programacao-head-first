from random import randint
secret = randint(1, 10)

print("Welcome!")
guess = 0
while guess != secret:
  g = input("Guess the number: ")  # pt. Adivinhe o número:
  guess = int(g)
  if guess == secret:
    print("You win!")  # pt. Você venceu!
  else:
    if guess > secret:
      print("Too high")  # pt. Alto de mais
    else:
      print("Too low")  # pt. Baixo de mais
print("Game over!")
