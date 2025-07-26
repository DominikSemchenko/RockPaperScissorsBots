import rps
import random

game = rps.RPSGame()

plr1, plr2 = game.get_players()

print(f"Player 1: {plr1}")
print(f"Player 2: {plr2}")

def generate_move():
    return random.randint(1, 3)

while True:
    move1 = input("Player 1 Move: ")
    if move1 not in ["1", "2", "3"]:
        print("Invalid move")
        continue
    game.move(plr1, int(move1))
    move2 = generate_move()
    if str(move2) not in ["1", "2", "3"]:
        print("Invalid move")
        continue
    print(f"Player 2 Move: {move2}")
    winner = game.move(plr2, move2)
    if winner:
        print(f"Winner: {winner}")
        break