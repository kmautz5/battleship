from random import randint

board = []

for x in range(0, 10):
  board.append(["O"] * 10)

def print_board(board):
  for row in board:
    print " ".join(row)

#print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)


game_is_finished = False
turn = 0

while game_is_finished is False:
  
  print_board(board)
  print "Turn", turn + 1
  
  if turn == 0:
    ship_row = random_row(board)
    ship_col = random_col(board)
    
  raw_row = raw_input("Guess Row: ")
  raw_col = raw_input("Guess Column: ") #check if raw input is a digit, also catches empty string
  if raw_row.isdigit() and raw_col.isdigit():
    guess_row = int(raw_row)
    guess_col = int(raw_col)
  
    if guess_row == ship_row and guess_col == \
        ship_col:
      print "Congratulations! You sank my battleship!"
      turn = 3 #this triggers rematch
    else:
      if guess_row not in range(10) or \
         guess_col not in range(10):
         print "Oops, that's not even in the ocean."
         turn += 1
      elif board[guess_row][guess_col] == "X":
         print( "You guessed that one already." )
         turn += 1
      else:
         print "You missed my battleship!"
         board[guess_row][guess_col] = "X"
         turn += 1
    #this is where invalid raw input terminates program
  else:
     print "Invalid input! Terminating!"
     game_is_finished = True #exits the loop
###
  if turn == 3:
    print "Game Over"
    rematch = raw_input("Do you want a rematch? ")
    if rematch == "Y" or rematch =="y" or \
        rematch == "yes":
      turn = 0 #if user wants a rematch, set turn back to 0
    else:
      print "I guess not.."
      game_is_finished = True

#after the loop
