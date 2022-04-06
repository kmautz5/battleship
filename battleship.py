#from random import randint, randrange   imports only these two functions...
from random import * #import all from random

board = []

for x in range(0, 10):
  board.append(["O"] * 10)



def print_board(board):
  for row in board:
    print(" ".join(row))

#print_board(board)

def random_row(board):
  return randint(0, len(board) - 1) #prevents it from choosing a value beyond the board

def random_col(board):
  return randint(0, len(board[0]) - 1)


game_is_finished = False
turn = 0
ship_sank = 0

while game_is_finished is False:
  
  print_board(board)
  print("Turn", turn + 1)
  
  if turn == 5 or ship_sank == 2: #if player loses or wins, exit the while loop
    game_is_finished = True

  if turn == 0:
    #generate 1x1 ship at random location on the board
    ship1_row = random_row(board)
    ship1_col = random_col(board)
      
    #generate 2x2 ship at random location on the board
    #right now this may randomely choose the same coordinates..
    ship2_row_firstpoint = random_row(board)
    ship2_col_firstpoint = random_col(board)
    #firstpoint = (ship2_col_firstpoint,ship2_row_firstpoint)

    #not getting second point off the board!
    if ship2_row_firstpoint == 0: #[?,0]
      ship2_row_secondpoint = randrange(0,1)
      if ship2_col_firstpoint == 0 and ship2_row_secondpoint == 0: #[0,0] [?,0]
        ship2_col_secondpoint = 1 #[0,0] [1,0]
      elif ship2_col_firstpoint == 0 and ship2_row_secondpoint == 1: #[0,0] [?,1]
        ship2_col_secondpoint = 0 #[0,0] [0,1]
    #not getting second point off the board!
    elif ship2_row_firstpoint == 9: #[?,9]
      ship2_row_secondpoint = randrange(8,9)
      if ship2_col_firstpoint == 9 and ship2_row_secondpoint == 9: #[9,9] [?,9]
        ship2_col_secondpoint = 8 #[9,9] [8,9]
      elif ship2_col_firstpoint == 9 and ship2_row_secondpoint == 8: #[9,9] [?,8]
        ship2_col_secondpoint = 9 #[9,9] [9,8]
    else:
      ship2_row_secondpoint = randrange(ship2_row_firstpoint-1,ship2_row_firstpoint+1) #get the nearest neighboring point
      if ship2_row_secondpoint == ship2_row_firstpoint:
        ship2_col_secondpoint = choice(ship2_row_firstpoint-1,ship2_row_firstpoint+1) #ship2 is horizontal
      else:
        ship2_col_secondpoint = ship2_col_firstpoint #ship2 is vertical

  raw_row = input("Guess Row: ")
  raw_col = input("Guess Column: ") #check if raw input is a digit, also catches empty string
  if raw_row.isdigit() and raw_col.isdigit():
    guess_row = int(raw_row)
    guess_col = int(raw_col)
  
    
    if guess_row not in list(range(10)) or guess_col not in list(range(10)):
      print("Oops, that's not even in the ocean.") 
      turn += 1

    if guess_row == ship1_row and guess_col == ship1_col:
      print("You sank my battleship!")
      turn += 1
      ship_sank += 1

    if guess_row == ship2_row_firstpoint and guess_col == ship2_col_firstpoint:
      print("I've been hit!")
      turn += 1
      
      
    if board[guess_row][guess_col] == "X":
       print( "You guessed that one already." )
       turn += 1
    else:
       print("You missed my battleship!")
       board[guess_row][guess_col] = "X"
       turn += 1
    
  else:
     print("Invalid input! Terminating!")
     game_is_finished = True #exits the loop

#end of game prompts
  if ship_sank == 2:
    print("Congratulations! You won!")
  else:
    print("Game Over")
    rematch = input("Do you want a rematch? ")
    if rematch == "Y" or rematch =="y" or rematch == "yes":
      print("Regenerating board!")
      turn = 0 #if user wants a rematch, set turn back to 0
    else:
      print("I guess not..")
      game_is_finished = True

#after the loop
