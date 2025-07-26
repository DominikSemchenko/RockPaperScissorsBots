import rps
import random
import copy

game = rps.RPSGame()

plr1, plr2 = game.get_players()

def move_to_string(move):
    if move in [1, 2, 3]:
        if move == 1:
            return "Rock"
        elif move == 2:
            return "Paper"
        elif move == 3:
            return "Scissors"

prev1, prev2 = 0, 0

def generate_data():
    patterns = {}
    for i in range(1, 4):
        for j in range(1, 4):
            patterns[(i, j)] = {1: 0, 2: 0, 3: 0}
    return copy.deepcopy(patterns)
patterns_data = generate_data()

print(f"Player 1: {plr1}")
print(f"Player 2: {plr2}")

def learn(prev1, prev2, current_move, data):
    if prev1 != 0 and prev2 != 0:
        data[prev2, prev1][current_move] += 1

def get_winning_move(move):
    for key, value in game.win_combinations.items():
        if value == move:
            win_combination = key
    return win_combination

def generate_move(prev1, prev2):
    if prev1 == 0 or prev2 == 0:
        return random.randint(1, 3)
    
    next_possible_moves = patterns_data[prev2, prev1]

    if all(v == 0 for v in next_possible_moves.values()):
        return random.randint(1, 3)
    
    max_value = max(next_possible_moves.values())
    most_frequent_moves = []
    for move, count in next_possible_moves.items():
        if count == max_value:
            most_frequent_moves.append(move)

    predicted_move = random.choice(most_frequent_moves)
    return get_winning_move(predicted_move)

while True:
    move1 = input("Player 1 Move: ")
    print(f"Player 1 Move: {move_to_string(move1)} ({move1})")
    move2 = generate_move(prev1, prev2)
    if move1 == "0":
        break
    if move1 == "4":
        print(patterns_data)
        continue
    if move1 == "5":
        patterns_data = generate_data()
        prev1, prev2 = 0, 0
        continue
    if move1 == "6":
        try:
            i = int(input("How many simulation rounds? "))
            print("--- Starting Simulation ---")
            player_wins = 0
            bot_wins = 0
            for round_num in range(i):
                sim_player_move = random.randint(1, 3)
                
                sim_ai_move = generate_move(prev1, prev2) 
                
                print(f"Round {round_num+1}: Sim Player chose {sim_player_move}, AI chose {sim_ai_move}")
                
                learn(prev1, prev2, sim_player_move, patterns_data)
                
                prev2 = prev1
                prev1 = sim_player_move
                
                game.move(plr1, sim_player_move)
                winner = game.move(plr2, sim_ai_move)

                if winner:
                    print(f"Winner: {winner}")
                    if winner == "player1":
                        player_wins += 1
                    elif winner == "player2":
                        bot_wins += 1
                
            print("--- Simulation Complete ---")
            print(f"Player wins: {player_wins}")
            print(f"AI wins: {bot_wins}")
        except ValueError:
            print("Please enter a valid number.")
        continue

    if move1 not in ["1", "2", "3"]:
        print("Invalid move")
        continue
    current_move = int(move1)
    learn(prev1, prev2, current_move, patterns_data)
    prev2 = prev1
    prev1 = current_move
    game.move(plr1, current_move)
    if str(move2) not in ["1", "2", "3"]:
        print("Invalid move")
        continue
    print(f"Player 2 Move: {move_to_string(move2)} ({move2})")
    winner = game.move(plr2, move2)
    if winner:
        print(f"Winner: {winner}")