import rps
import random

game = rps.RPSGame()

plr1, plr2 = game.get_players()

prev = 0
player_data = {
    "1": 0,
    "2": 0,
    "3": 0
}

print(f"Player 1: {plr1}")
print(f"Player 2: {plr2}")

def get_winning_move(move):
    for key, value in game.win_combinations.items():
        if value == move:
            win_combination = key
    return win_combination

def generate_move():
    # Check if there's any data yet
    if all(v == 0 for v in player_data.values()):
        return random.randint(1, 3)

    # Find the highest score
    max_value = max(player_data.values())
    
    # Find all moves that are tied for the highest score
    most_frequent_moves = []
    for move, count in player_data.items():
        if count == max_value:
            most_frequent_moves.append(int(move))
    
    # Randomly pick one of the "best" moves to predict
    predicted_move = random.choice(most_frequent_moves)
    
    # Return the counter to that predicted move
    return get_winning_move(predicted_move)

while True:
    move1 = input("Player 1 Move: ")
    move2 = generate_move()
    if move1 == "0":
        break
    if move1 == "4":
        print(player_data)
        continue
    if move1 == "5":
        player_data = {
            "1": 0,
            "2": 0,
            "3": 0
        }
        continue
    if move1 == "6":
        print("Starting random moves")
        i = input("How many times? ")
        for _ in range(int(i)):
            moveRandom = random.randint(1, 3)
            move2 = generate_move()
            player_data[str(moveRandom)] += 1
            game.move(plr1, moveRandom)
            winner = game.move(plr2, move2)
            if winner:
                print(f"Winner: {winner}")
        continue

    if move1 not in ["1", "2", "3"]:
        print("Invalid move")
        continue
    player_data[move1] += 1
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