import random
import sys
def PlayNumberGame():
	goalnumber = random.randint(1,100)
	found = False
	guesses = []
	while found == False:
		print('Guess a number between 1 and 100')
		guessednumber = int(input())
		guesses.append(guessednumber)
		if guessednumber == goalnumber:
			found = True
		elif guessednumber > goalnumber:
			print('Too High')
		elif guessednumber < goalnumber:
			print('Too Low')
	print('Congratulations, you won!')
	print(f'It only took you {len(guesses)} guesses!')
	print(f'Your guesses were {guesses}')
	playagain = input('Would you like to play again?')
	if playagain == 'Yes' or playagain =='yes' or playagain =='y' or playagain =='Y':
		PlayNumberGame()

PlayNumberGame()









