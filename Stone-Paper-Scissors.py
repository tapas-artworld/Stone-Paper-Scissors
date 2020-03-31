from random import randint

while True:
	player_choice = (str(input("\n\nWhat do you want to Choice \nstone \npaper \nscissors \nYour Choice => "))).strip()
	random_move = randint(0, 2)
	moves = ['stone','paper','scissors']

	boot_choice = moves[random_move]
	# print(player_choice)
	print('Computer choice =>',boot_choice)

	if player_choice == boot_choice:
		print('Match Draw')
	elif player_choice == 'stone' and boot_choice == 'scissors':
		print('You Win!!')
	elif player_choice == 'paper' and boot_choice == 'scissors':
		print('You Lose!!')
	elif player_choice == 'scissors' and boot_choice == 'paper':
		print('You Win!!')
	elif player_choice == 'scissors' and boot_choice == 'stone':
		print('You Lose!!')
	elif player_choice == 'paper' and boot_choice == 'stone':
		print('You Win!!')
	elif player_choice == 'stone' and boot_choice == 'paper':
		print('You Lose!!')

	play_again = str(input('Do you want to play again ?(y or n)')).strip().upper()
	if play_again == "n":
		break
