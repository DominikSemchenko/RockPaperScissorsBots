import rps
import random
from collections import deque
import level2
import level5
import level7
import level10

def move_to_string(move):
    if move == 1: return "Rock"
    if move == 2: return "Paper"
    if move == 3: return "Scissors"
    return "Unknown"

def get_winning_move(move_to_beat, game_engine):
    for winner, loser in game_engine.win_combinations.items():
        if loser == move_to_beat:
            return winner
    return random.randint(1, 3)

bots = {
    "L2_Copycat": {
        "generate_move": level2.generate_move,
        "learn": None,
        "data": None
    },
    "L5_Frequency": {
        "generate_move": level5.generate_move,
        "learn": level5.learn,
        "data": deque(maxlen=10)
    },
    "L7_Pattern": {
        "generate_move": level7.generate_move,
        "learn": level7.learn,
        "data": level7.generate_data()
    },
    "L10_Oracle": {
        "generate_move": level10.generate_move,
        "learn": level10.learn,
        "data": level10.create_model()
    }
}

def learn_reputation(current_player_move, predicted_bot_moves, reputation, game_engine):
    
    for name, bot_counter_move in predicted_bot_moves.items():
        predicted_player_move = game_engine.win_combinations[bot_counter_move]
        if predicted_player_move == current_player_move:
            reputation[name] += 1
        else:
            reputation[name] -= 1

def choose_champion_move(predicted_bot_moves, reputation):    
    """
    Chooses the move of the bot with the highest reputation.

    If all bots have a reputation of 0, this function returns a random move.

    Parameters
    ----------
    predicted_bot_moves : dict
        A dictionary where the key is the name of the bot and the value is the move that the bot predicts.
    reputation : dict
        A dictionary where the key is the name of the bot and the value is the reputation of the bot.

    Returns
    -------
    int
        The move of the champion bot.
    """

    if all(v == 0 for v in reputation.values()):
        return random.choice(list(predicted_bot_moves.values()))
    max_rep = max(reputation.values())
    best_bots = [name for name, rep in reputation.items() if rep == max_rep]
    champion_name = random.choice(best_bots)
    return predicted_bot_moves[champion_name]

if __name__ == "__main__":
    game = rps.RPSGame()
    plr1, plr2 = game.get_players()
    reputation = {name: 0 for name in bots.keys()}
    prev_1, prev_2 = 0, 0
    ai_wins, player_wins = 0, 0

    while True:
        try:
            predicted_moves = {}
            for name, bot in bots.items():
                if "L2" in name:
                    predicted_moves[name] = bot["generate_move"](prev_1, game)
                elif "L5" in name:
                    predicted_moves[name] = bot["generate_move"](bot["data"], game, get_winning_move)
                elif name in ["L7_Tactician", "L10_Oracle"]:
                    predicted_moves[name] = bot["generate_move"](prev_2, prev_1, bot["data"], game)

            ai_move = choose_champion_move(predicted_moves, reputation)
            player_input = input("Your Move (1=R, 2=P, 3=S) | 4=view reps | 5=reset | 0=quit: ")
            if player_input == "0": break
            if player_input == "4":
                sorted_reps = sorted(reputation.items(), key=lambda item: item[1], reverse=True)
                for name, rep in sorted_reps:
                    print(f"{name}: {rep}")
                continue
            if player_input == "5":
                for name, bot in bots.items():
                    if bot["data"] is not None:
                        bot["data"] = deque(maxlen=10)
                reputation = {name: 0 for name in bots.keys()}
                prev_1, prev_2 = 0, 0
                ai_wins, player_wins = 0, 0
                continue

            current_move = int(player_input)
            if current_move not in [1, 2, 3]: continue

            print(f"You played: {move_to_string(current_move)}")
            print(f"AI plays:   {move_to_string(ai_move)}")

            learn_reputation(current_move, predicted_moves, reputation, game)

            for name, bot in bots.items():
                if bot["learn"] is not None:
                    if "L5" in name:
                        bot["learn"](current_move, bot["data"])
                    elif "L7" in name or "L10" in name:
                        bot["learn"](prev_2, prev_1, current_move, bot["data"])

            prev_2 = prev_1
            prev_1 = current_move
            game.move(plr1, current_move)
            winner = game.move(plr2, ai_move)

            if not winner:
                print("🤝 It's a tie.")
            elif winner == plr1:
                player_wins += 1
                print("🎉 You win!")
            elif winner == plr2:
                ai_wins += 1
                print("🤖 The AI wins!")
            print("-" * 30)

        except ValueError:
            print("Invalid input. Please enter a number.")
        except KeyboardInterrupt:
            break

    print("\n--- Game Over ---")
    print(f"Final Scores -> You: {player_wins} | AI: {ai_wins}")
    print(f"Final Reputations: {reputation}")
    print("Thanks for playing!")
