import rps
import random
from collections import deque

player_data = deque(maxlen=10)
player_win_streak = 0

def get_winning_move(move, game):
    for key, value in game.win_combinations.items():
        if value == move:
            win_combination = key
            return win_combination

def generate_move(data, game):
    if len(data) == 0:
        return random.randint(1, 3)

    if player_win_streak >= 3:
        return random.randint(1,3)

    counts = {1: 0, 2: 0, 3: 0}
    for move in data:
        counts[move] += 1

    max_value = max(counts.values())

    most_frequent_moves = []
    for move, count in counts.items():
        if count == max_value:
            most_frequent_moves.append(move)

    predicted_move = random.choice(most_frequent_moves)

    return get_winning_move(predicted_move, game)

if __name__ == "__main__":
    global game, plr1, plr2
    game = rps.RPSGame()

    plr1, plr2 = game.get_players()
    
    print(f"Player 1: {plr1}")
    print(f"Player 2: {plr2}")

    while True:
        try:
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
                # TODO: ADD UPDATED WIN HANDLING. WINNER RETURNS UUID.
                if winner == plr1:
                    print("Winner: Player")
                    player_win_streak += 1
                elif winner == plr2:
                    print("Winner: AI")
                    player_win_streak = 0
                else:
                    print("Tie")
        except KeyboardInterrupt:
            print("KB INTERRUPT")
            print(player_win_streak)