import rps
import random

prev = 0

def generate_move(prev, game):
    if prev == 0:
        return random.randint(1, 3)
    for key, value in game.win_combinations.items():
        if value == prev:
            win_combination = key
    return win_combination

if __name__ == "__main__":
    global game, plr1, plr2
    game = rps.RPSGame()

    plr1, plr2 = game.get_players()
    
    print(f"Player 1: {plr1}")
    print(f"Player 2: {plr2}")
    while True:
        move1 = input("Player 1 Move: ")
        move2 = generate_move(prev, game)
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
            break