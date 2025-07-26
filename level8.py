import rps
import random
import copy
import level2, level5, level7
from collections import deque

game = rps.RPSGame()

plr1, plr2 = game.get_players()

level5_data = deque(maxlen=10)
level7_data = level7.generate_data()

def move_to_string(move):
    if move in [1, 2, 3]:
        if move == 1:
            return "Rock"
        elif move == 2:
            return "Paper"
        elif move == 3:
            return "Scissors"
    return "None"

prev1, prev2 = 0, 0

model_reputation = {
    "level2": 0,
    "level5": 0,
    "level7": 0
}

print(f"Player 1: {plr1}")
print(f"Player 2: {plr2}")

def get_winning_move(move):
    for key, value in game.win_combinations.items():
        if value == move:
            return key

def learn(current_player_move, predicted_bot_moves, reputation):
    """Updates reputation based on which models correctly predicted the player's move."""
    for model_name, bot_move in predicted_bot_moves.items():
        if bot_move in game.win_combinations:
            predicted_player_move = game.win_combinations[bot_move]
            if predicted_player_move == current_player_move:
                reputation[model_name] += 1
    return reputation

def generate_move(predicted_bot_moves, reputation):
    """Chooses a move from the suggestions based on model reputation."""
    if all(v == 0 for v in reputation.values()):
        return random.choice(list(predicted_bot_moves.values()))

    max_rep = max(reputation.values())
    best_models = [model for model, rep in reputation.items() if rep == max_rep]
    
    chosen_model = random.choice(best_models)
    return predicted_bot_moves[chosen_model]

while True:
    if prev1 == 0: # Not enough history
        predicted_bot_moves = {"level2": random.randint(1,3), "level5": random.randint(1,3), "level7": random.randint(1,3)}
    else:
        predicted_bot_moves = {
            "level2": level2.generate_move(prev1, game),
            "level5": level5.generate_move(level5_data, game),
            "level7": level7.generate_move(prev1, prev2, level7_data, game)
        }

    move2 = generate_move(predicted_bot_moves, model_reputation)

    move1 = input("Player 1 Move: ")
    # testing
    if move1 == "0":
        break
    if move1 == "4":
        print(model_reputation)
        continue
    if move1 == "5":
        model_reputation = {"level2": 0, "level5": 0, "level7": 0}
        level5_data.clear()
        level7_data = level7.generate_data()
        prev1, prev2 = 0, 0
        print("--- All models reset ---")
        continue
    if move1 == "6":
        try:
            i = int(input("How many simulation rounds? "))
            print("--- Starting Simulation ---")
            player_wins, bot_wins = 0, 0
            
            for round_num in range(i):
                sim_player_move = random.randint(1, 3)

                sim_predicted_moves = {
                    "level2": level2.generate_move(prev1, game),
                    "level5": level5.generate_move(level5_data, game),
                    "level7": level7.generate_move(prev1, prev2, level7_data, game)
                }
                sim_ai_move = generate_move(sim_predicted_moves, model_reputation)

                print(f"Round {round_num+1}: Sim Player chose {move_to_string(sim_player_move)}, AI chose {move_to_string(sim_ai_move)}")
                
                level5_data.append(sim_player_move)
                level7.learn(prev1, prev2, sim_player_move, level7_data)
                model_reputation = learn(sim_player_move, sim_predicted_moves, model_reputation)

                prev2 = prev1
                prev1 = sim_player_move

                game.move(plr1, sim_player_move)
                winner = game.move(plr2, sim_ai_move)

                if winner:
                    print(f"Winner: {winner}")
                    if winner == "player1": player_wins += 1
                    elif winner == "player2": bot_wins += 1
            
            print("--- Simulation Complete ---")
            print(f"Player wins: {player_wins}")
            print(f"AI wins: {bot_wins}")
            print(f"Final Reputations: {model_reputation}")
        except (ValueError, KeyError):
            print("An error occurred during simulation. Please reset (5) and try again.")
        continue

    if move1 not in ["1", "2", "3"]:
        print("Invalid move")
        continue
    
    current_move = int(move1)
    print(f"Player 1 Move: {move_to_string(current_move)} ({current_move})")

    model_reputation = learn(current_move, predicted_bot_moves, model_reputation)
    level5_data.append(current_move)
    level7.learn(prev1, prev2, current_move, level7_data)
    
    prev2 = prev1
    prev1 = current_move
    
    game.move(plr1, current_move)
    
    print(f"Player 2 Move: {move_to_string(move2)} ({move2})")
    winner = game.move(plr2, move2)
    if winner:
        print(f"Winner: {winner}")