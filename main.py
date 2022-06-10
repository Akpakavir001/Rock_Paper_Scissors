import random

print("\nWelcome to Rock,Paper and Scissors Game App.\n")

print("To play this game, you have to choose 'R' for Rock 'P' for Paper or 'S' for Scissors from the options below.\n")

#list of moves
moves = ['R','P','S']
#CPU choice
c_choice = random.choice(moves)


player_score = 0

cpu_score = 0

#simulating the game
run = True
while run:
		#player choice
		p_choice = input("Enter R,P or S:").strip()
		#if player choice is not valid
		if p_choice not in moves[:]:
			print("\nSorry, that's an invalid choice. Try again.\n")
		else:
			if p_choice == 'R' and c_choice == 'S':
				print(f"Player({p_choice}) : CPU({c_choice})")
				print("\nRock beats scissors")
				print("Player wins!")
				player_score+=1
				print(f"Player({player_score}) : CPU({cpu_score})")
				break
			elif p_choice == 'P' and c_choice == 'S':
				print(f"Player({p_choice}) : CPU({c_choice})")
				print("\nScissors beat paper")
				print("Computer wins!")
				cpu_score+=1
				print(f"Player({player_score}) : CPU({cpu_score})")
				break
			#if it is a tie
			elif p_choice == 'S' and c_choice == 'S':
				print(f"Player({p_choice}) : CPU({c_choice})")
				print(f"Player({player_score}) : CPU({cpu_score})")
				print("\nIt's a tie")
							
			elif p_choice == 'P' and c_choice == 'R':
				print(f"Player({p_choice}) : CPU({c_choice})")
				print("\nPaper beats rock")
				print("Player wins!")
				player_score+=1
				print(f"Player({player_score}) : CPU({cpu_score})")
				break
			elif p_choice == 'S' and c_choice == 'R':
				print(f"Player({p_choice}) : CPU({c_choice})")
				print("\nRock beats scissors")
				print("Computer wins!")
				cpu_score+=1
				print(f"Player({player_score}) : CPU({cpu_score})")
				break
				
			#if it is a tie
			elif p_choice == 'R' and c_choice == 'R':
				print(f"Player({p_choice}) : CPU({c_choice})")
				print(f"Player({player_score}) : CPU({cpu_score})")
				print("\nIt's a tie")
				
			elif p_choice == 'R' and c_choice == 'P':
				print(f"Player({p_choice}) : CPU({c_choice})")
				print("\nPaper beats rock")
				print("Computer wins!")
				cpu_score+=1
				print(f"Player({player_score}) : CPU({cpu_score})")
				break
				
			elif p_choice == 'S' and c_choice == 'P':
				print(f"Player({p_choice}) : CPU({c_choice})")
				print("\nScissors beat paper")
				print("Player wins!")
				player_score+=1
				print(f"Player({player_score}) : CPU({cpu_score})")
				break
				
			#if it is a tie
			elif p_choice == 'P' and c_choice == 'P':
				print(f"Player({p_choice}) : CPU({c_choice})")
				print(f"Player({player_score}) : CPU({cpu_score})")
				print("\nIt's a tie")
				
			else:
				print("That's not correct, please check your spellings and try again.")
							
				while run:
				#player choice
					p_choice = input("Enter R,P or S:").strip()
			#if player choice is not valid
				if p_choice not in moves[:]:
					print("\nSorry, that's an invalid choice.\n")
				else:
					#p_choice = input("Enter R,P or S:")
					if p_choice == 'R' and c_choice == 'S':
						print(f"Player({p_choice}) : CPU({c_choice})")
						print("\nRock beats scissors")
						print("Player wins!")
						player_score+=1
						print(f"Player({player_score}) : CPU({cpu_score})")
						break
					elif p_choice == 'P' and c_choice == 'S':
						print(f"Player({p_choice}) : CPU({c_choice})")
						print("\nScissors beat paper")
						print("Computer wins!")
						cpu_score+=1
						print(f"Player({player_score}) : CPU({cpu_score})")
						break
					#if it is a tie
					elif p_choice == 'S' and c_choice == 'S':
						print(f"Player({p_choice}) : CPU({c_choice})")
						print(f"Player({player_score}) : CPU({cpu_score})")
						print("\nIt's a tie")
						
					elif p_choice == 'P' and c_choice == 'R':
						print(f"Player({p_choice}) : CPU({c_choice})")
						print("\nPaper beats rock")
						print("Player wins!")
						player_score+=1
						print(f"Player({player_score}) : CPU({cpu_score})")
						break
					elif p_choice == 'S' and c_choice == 'R':
						print(f"Player({p_choice}) : CPU({c_choice})")
						print("\nRock beats scissors")
						print("Computer wins!")
						cpu_score+=1
						print(f"Player({player_score}) : CPU({cpu_score})")
						break
					#if it is a tie
					elif p_choice == 'R' and c_choice == 'R':
						print(f"Player({p_choice}) : CPU({c_choice})")
						print(f"Player({player_score}) : CPU({cpu_score})")
						print("\nIt's a tie")
						
					elif p_choice == 'R' and c_choice == 'P':
						print(f"Player({p_choice}) : CPU({c_choice})")
						print("\nPaper beats rock")
						print("Computer wins!")
						cpu_score+=1
						print(f"Player({player_score}) : CPU({cpu_score})")
						break
					elif p_choice == 'S' and c_choice == 'P':
						print(f"Player({p_choice}) : CPU({c_choice})")
						print("\nScissors beat paper")
						player_score+=1
						print(f"Player({player_score}) : CPU({cpu_score})")
						print("Player wins!")
						break	
					#if it is a tie
					elif p_choice == 'P' and c_choice == 'P':
						print(f"Player({p_choice}) : CPU({c_choice})")
						print("\nIt's a tie")
					else:
						print("That's not correct, please check your spellings and try again.")
					run = False