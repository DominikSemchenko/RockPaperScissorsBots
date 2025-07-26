# GEMINI BEAUTIFIED THE SCRIPT.

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
            return "Scissors"
        elif move == 3:
            return "Paper"

prev = 0

data_example = {
    1: {
        1: 0,
        2: 0,
        3: 0
    },
    2: {
        1: 0,
        2: 0,
        3: 0
    },
    3: {
        1: 0,
        2: 0,
        3: 0
    }
}
player_data = copy.deepcopy(data_example)

print(f"Player 1: {plr1}")
print(f"Player 2: {plr2}")

def learn(previous_move, current_move, data_matrix):
    if previous_move != 0:
        data_matrix[previous_move][current_move] += 1

def get_winning_move(move):
    for key, value in game.win_combinations.items():
        if value == move:
            win_combination = key
    return win_combination

def generate_move():
    if prev == 0:
        return random.randint(1, 3)
    
    next_possible_moves = player_data[prev]

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
    print(f"Player 2 Move: {move_to_string(move1)} ({move1})")
    move2 = generate_move()
    if move1 == "0":
        break
    if move1 == "4":
        print(player_data)
        continue
    if move1 == "5":
        player_data = copy.deepcopy(data_example)
        prev = 0
        continue
    if move1 == "6":
        try:
            i = int(input("How many simulation rounds? "))
            print("--- Starting Simulation ---")
            player_wins = 0
            bot_wins = 0
            for round_num in range(i):
                sim_player_move = random.randint(1, 3)
                
                sim_ai_move = generate_move() 
                
                print(f"Round {round_num+1}: Sim Player chose {sim_player_move}, AI chose {sim_ai_move}")
                
                learn(prev, sim_player_move, player_data)

                prev = sim_player_move
                
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
    learn(prev, current_move, player_data)
    prev = current_move
    game.move(plr1, current_move)
    if str(move2) not in ["1", "2", "3"]:
        print("Invalid move")
        continue
    print(f"Player 2 Move: {move_to_string(move2)} ({move2})")
    winner = game.move(plr2, move2)
    if winner:
        print(f"Winner: {winner}")