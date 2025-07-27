import rps
import random
from collections import deque, Counter

player_data = deque(maxlen=10)

def generate_data():
    return deque(maxlen=10)

def learn(current_move, data):
    data.append(current_move)

def generate_move(data, game_engine, get_winning_move_func):
    if not data:
        return random.randint(1, 3)
    counts = Counter(data)
    most_common = counts.most_common()
    max_count = most_common[0][1]
    best_moves = [move for move, count in most_common if count == max_count]
    predicted_move = random.choice(best_moves)
    return get_winning_move_func(predicted_move, game_engine)

if __name__ == "__main__":
    global game, plr1, plr2
    game = rps.RPSGame()
    plr1, plr2 = game.get_players()
    print(f"Player 1: {plr1}")
    print(f"Player 2: {plr2}")

    while True:
        move1 = input("Player 1 Move: ")
        move2 = generate_move(player_data, game)
        if move1 == "0":
            break
        if move1 == "4":
            print(player_data)
            continue
        if move1 == "5":
            player_data = deque(maxlen=10)
            continue
        if move1 == "6":
            try:
                i = int(input("How many times? "))
                print("Starting random moves")
                for _ in range(int(i)):
                    moveRandom = random.randint(1, 3)
                    move2 = generate_move(player_data, game)
                    player_data.append(moveRandom)
                    game.move(plr1, moveRandom)
                    winner = game.move(plr2, move2)
                    if winner:
                        print(f"Winner: {winner}")
            except ValueError:
                print("Please enter a valid number.")
            continue

        if move1 not in ["1", "2", "3"]:
            print("Invalid move")
            continue
        player_data.append(int(move1))
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
