from random import *

# board setup
board = []
for x in range(10):
  board.append(["O"] * 10)

def print_board(board):
  for row in board:
    print(" ".join(row))

def random_coords(board):
    return randint(0, len(board) - 1), randint(0, len(board[0]) - 1)

def place_ship(board, shipSize):
  # place a ship of a given shipSize on the board
  while True:
    # choose a random orientation to place a ship
    orientation = choice(['horizontal', 'vertical'])
    if orientation == 'horizontal':
      ship_row = randint(0, len(board) - 1)
      ship_col = randint(0, len(board[0]) - shipSize)
      coords = [(ship_row, ship_col + i) for i in range(shipSize)]
    else: # vertical
      ship_row = randint(0, len(board) - shipSize)
      ship_col = randint(0, len(board[0]) - 1)
      coords = [(ship_row + i, ship_col) for i in range(shipSize)]

    # check for conflicts with other ships, if so restart at while true
    conflict = False
    for r, c in coords:
      if board[r][c] == "S":
        conflict = True
        break
    if not conflict:
      for r, c in coords:
        board[r][c] = "S" # S marks where the ship is
      print(coords)
      return coords

def main_game():
  global board
  board = [["O"] * 10 for _ in range(10)]
  
  # place ships (1x1 and 2x2)
  ship1_coords = place_ship(board, 1)
  ship2_coords = place_ship(board, 2)
  
  # Hide the ships for the player
  for r in range(10):
    for c in range(10):
      if board[r][c] == "S":
        board[r][c] = "O"

  ships_remaining = [ship1_coords, ship2_coords]
  turns_left = 5
  
  while turns_left > 0 and len(ships_remaining) > 0:
    print_board(board)
    print("Turns left:", turns_left)
    
    try:
      guess_row = int(input("Guess Row: "))
      guess_col = int(input("Guess Column: "))
    except ValueError:
      print("Invalid input! Please enter a number.")
      continue
        
    if not (0 <= guess_row < 10 and 0 <= guess_col < 10):
      print("Oops, that's not even in the ocean.")
      turns_left -= 1
      continue
        
    if board[guess_row][guess_col] == "X":
      print("You guessed that one already.")
      turns_left -= 1
      continue

    is_hit = False
    ship_sank = -1
    for i, ship in enumerate(ships_remaining):
      if (guess_row, guess_col) in ship:
        ship.remove((guess_row, guess_col))
        if not ship:
          print("You sank a battleship!")
          ship_sank = i
          board[guess_row][guess_col] = "X"
          is_hit = True
        else:
          print("I've been hit!")
          board[guess_row][guess_col] = "H"
          is_hit = True
        break
    
    if is_hit and ship_sank != -1:
      ships_remaining.pop(ship_sank)
    elif not is_hit:
      print("You missed my battleship!")
      board[guess_row][guess_col] = "X"

    turns_left -= 1

  print_board(board)
  if not ships_remaining:
    print("Congratulations! You won!")
  else:
    print("Game Over")

rematch = "yes"
while rematch.lower() in ["y", "yes"]:
  main_game()
  rematch = input("Do you want a rematch?")