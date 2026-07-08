# ─────────────────────────────────────────────────────────────
# SDE Escape Room
#
# This file grows across SDE lessons 5–9 and is polished in L10.
#   L5  Input & If/Else      — print intro + ask the player's name
#   L6  Random & While Loops — random rooms + a main game loop
#   L7  2D Maps & Movement   — grid map + N/S/E/W movement
#   L8  Puzzle Functions     — refactor puzzles into functions + walls
#   L9  Final Customization  — theme, story, win/lose screens
#   L10 Polish & Stretch     — pick from key item, time limit,
#                              hunger, math puzzle, etc.
#
# Keep working in this single file unless your instructor says
# otherwise. Save often — your work persists between lessons.
# ─────────────────────────────────────────────────────────────
name = input('What is your name?: ')
print(f'{name}, welcome to the secret spacestation located near mars.')
print(f'{name}, your mission is to head to the console room since the computer is having technical issues.')

room = [
    "xxxxxx",
    "x.k..x",
    "x.p..x",
    "x.p.ex",
    "xxxxxx",
]

import random
import time
import os
key = False
posY = 1
posX = 1


  
neighbors =[(-1, 0, "above"),(1,0,"below"),(0,-1,"left"),(0,1,"right")]
def announce_walls(current_row, current_col):
    global key
    for d_row, d_col, label in neighbors:
        if room[current_row + d_row][current_col+ d_col] == "x":
            print(f'There is a wall {label}')
    if room[current_row][current_col] == room[3][2]:
        puzzle2()
    if room[current_row][current_col] == room[2][2]:
        puzzle1()
    if room[current_row][current_col] == 'k':
        key = True
        print('You got the key!')
      

def save_state(player_row, player_col, has_key):
    with open("save.txt", "w") as file:
         file.write(f"{player_row}\n")
         file.write(f"{player_col}\n")
         file.write(f"{has_key}\n")
    print("💾 Game autosaved.")

def load_state():
    """Reads save.txt and returns (posY, posX, key) converted to proper data types."""
    with open("save.txt", "r") as file:
        lines = file.readlines()
        
    saved_row = int(lines[0].strip())
    saved_col = int(lines[1].strip())
    saved_key = lines[2].strip() == "True"
    
    return saved_row, saved_col, saved_key




if os.path.exists("save.txt"):
    resume = input("\nA save file was found! Do you want to resume? (yes/no): ").lower().strip()
    if resume == 'yes' or resume == 'y':
        posY, posX, key = load_state()
        print(f"✨ Welcome back, {name}! Resuming mission at coordinates ({posY}, {posX}).")
        if key:
            print("🔑 Access key detected in your inventory.")
    else:
        print("Starting a completely new mission.")



def puzzle1():
    passwords = ["fire", "water", "earth", "wind"]
    correct = random.choice(passwords)
    
    for word in passwords:
        if word == correct:
            print(word.capitalize())
        else:
            print(word)
          
    while True:
        guess = input("Guess the password: ")
        if guess == correct:
            print("You got it!")
            break
        else:
            print("Wrong — try again next time.")

def puzzle2():
  answers = ["A","B","C"]
  answer = random.choice(answers)

  guess = input('There are three space buttons. A, B, and C')

  while True:
        guess = input("Guess A, B, or C: ")
        if guess == answer:
            print("You got it!")
            break
        else:
            print("Wrong — try again next time.")


def move(direction):
  global posY
  global posX
  if direction == 'up':
    posY -=1
  elif direction == 'down':
    posY +=1
  elif direction == 'left':
    posX -=1
  else:
    posX +=1

    

escaped = False
# TODO (L5): ask the player for their name and greet them.







while escaped == False:
  movement = input('Where do you move in the map? (u,d,l,r)?')
  move(movement)
  time.sleep(1)
  
  print(f'You are in room coordinates ({posY},{posX})')
  announce_walls(posY, posX)
  
  if room[posY][posX] == room[3][4] and key == True:
      print("You escaped!")
      escaped = True
      if os.path.exists("save.txt"):
                os.remove("save.txt")
  else:
      print("The door is locked. Try again next door.")

  if not escaped:
      save_state(posY, posX, key)


