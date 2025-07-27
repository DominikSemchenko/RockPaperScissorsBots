import rps
import random

game = rps.RPSGame()

plr1, plr2 = game.get_players()
prev = 0

print(f"Player 1: {plr1}")
print(f"Player 2: {plr2}")

def generate_move(prev):
    if prev == 0:
        return random.randint(1, 3)
    # get the win for the prev move
    for key, value in game.win_combinations.items():
        if value == prev:
            new_move = key
    # get the win for the win of the prev move
    for key, value in game.win_combinations.items():
        if value == new_move:
            player_move = key

    # get the win for the player move
    for key, value in game.win_combinations.items():
        if value == player_move:
            win_combination = key
    return win_combination

while True:
    move1 = input("Player 1 Move: ")
    move2 = generate_move(prev)
    if move1 == "0":
        break
    if move1 not in ["1", "2", "3"]:
        print("Invalid move")
        continue
    prev = int(move1)
    game.move(plr1, int(move1))
    if str(move2) not in ["1", "2", "3"]:
        print("Invalid move")
        continue
    print(f"Player 2 Move: {move2}")
    winner = game.move(plr2, move2)
    if winner:
        if winner == plr1:
            print("Winner: Player")
        elif winner == plr2:
            print("Winner: AI")
        else:
            print("Tie")