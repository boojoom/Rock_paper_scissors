import sys
start = str(input('Enter "start" to start a game: '))
while start != 'start':
  start = str(input('Enter "start" to start a game: '))

def game():
	usr1 = str(input("User 1, please choose between rock, paper and scissors: "))
	usr2 = str(input("User 2, please choose between rock, paper and scissors: "))
	while True:
		if usr1 == 'rock' or usr1 == 'paper' or usr1 == 'scissors':
			print("User 1 chose", usr1)
			break
		else:
			usr1 = str(input("User 1, please choose between rock, paper and scissors: "))
	while True:
		if usr2 == 'rock' or usr2 == 'paper' or usr2 == 'scissors':
			print("User 2 chose", usr2)
			break
		else:
			usr2 = str(input("User 2, please choose between rock, paper and scissors: "))

	if usr1 == 'rock' and usr2 == 'paper':
		print('Paper beats rock. User 2 wins!')
	elif usr1 =='rock' and usr2 == 'scissors':
		print("Rock beats scissors. User 1 wins!")
	elif usr1 == 'paper' and usr2 == 'rock':
		print('Paper beats rock. User 1 wins!')
	elif usr1 == 'paper' and usr2 == 'scissors':
		print('Scissors beat paper. User 2 wins!')
	elif usr1 == 'scissors' and usr2 == 'rock':
		print("Rock beats scissors. User 2 wins!")
	elif usr1 == 'scissors' and usr2 == 'paper':
		print('Scissors beat paper. User 2 wins!')
	elif usr1 == usr2:
		print("It's a tie!")

game()

exit = str(input("Continue? [Yes/No]: "))
while exit == 'Yes':
  game()
  exit = str(input("Continue? [Yes/No]: "))
  if exit == 'No':
    sys.exit()
