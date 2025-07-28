import rps
import random
import numpy as np
from sklearn.linear_model import SGDClassifier

def move_to_string(move):
    if move == 1:
        return "Rock"
    elif move == 2:
        return "Paper"
    elif move == 3:
        return "Scissors"
    return "Unknown"

def get_winning_move(move_to_beat, game_engine):
    for winner, loser in game_engine.win_combinations.items():
        if loser == move_to_beat:
            return winner
    return random.randint(1, 3)

def create_model():
    return SGDClassifier(max_iter=1000, tol=1e-3)

def learn(p2, p1, current, model):
    """
    Update the machine learning model with the player's move pattern.

    This function uses the previous two player moves (p2 and p1) and the current move to 
    create a feature vector and label, which are then used to update the given machine 
    learning model. The model predicts the player's next move by learning patterns from 
    the sequence of moves.

    Args:
        p2 (int): The player's move two rounds ago.
        p1 (int): The player's move in the previous round.
        current (int): The player's current move.
        model (SGDClassifier): The machine learning model to be updated.

    Returns:
        None: The function updates the model in place.
    """

    if p1 == 0 or p2 == 0:
        return
    feature_vector = np.array([p2, p1]).reshape(1, -1)
    label = np.array([current])
    if not hasattr(model, "classes_"):
        model.partial_fit(feature_vector, label, classes=np.array([1, 2, 3]))
    else:
        model.partial_fit(feature_vector, label)

def generate_move(p2, p1, model, game_engine):
    """
    Use the given machine learning model to predict the player's next move based on their previous two moves (p2 and p1).

    Args:
        p2 (int): The player's move two rounds ago.
        p1 (int): The player's move in the previous round.
        model (SGDClassifier): The machine learning model to use for prediction.
        game_engine (rps.RPSGame): The game engine used to get the winning move.

    Returns:
        int: The AI's move, which is the winning move against the predicted player move.
    """
    if not hasattr(model, "classes_"):
        return random.randint(1, 3)
    feature_vector = np.array([p2, p1]).reshape(1, -1)
    predicted_move = model.predict(feature_vector)[0]
    return get_winning_move(predicted_move, game_engine)

if __name__ == "__main__":
    game = rps.RPSGame()
    plr1, plr2 = game.get_players()
    ai_model = create_model()
    prev_1 = 0
    prev_2 = 0
    ai_wins, player_wins = 0, 0
    print("Welcome to RPS v10: The Oracle!")
    while True:
        try:
            ai_move = generate_move(prev_2, prev_1, ai_model, game)
            player_input = input("Your Move (1=R, 2=P, 3=S) | 5=reset | 0=quit: ")
            if player_input == "0": break
            if player_input == "5":
                ai_model = create_model()
                prev_1, prev_2 = 0, 0
                ai_wins, player_wins = 0, 0
                print("--- AI Oracle has been reset to a blank slate. ---")
                continue
            current_move = int(player_input)
            if current_move not in [1, 2, 3]:
                print("Invalid move. Please choose 1, 2, or 3.")
                continue
            print(f"You played: {move_to_string(current_move)}")
            print(f"AI plays:   {move_to_string(ai_move)}")
            learn(prev_2, prev_1, current_move, ai_model)
            prev_2 = prev_1
            prev_1 = current_move
            game.move(plr1, current_move)
            winner = game.move(plr2, ai_move)
            if winner == "tie":
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
    print(f"Final Score -> You: {player_wins} | AI: {ai_wins}")
    print("Thanks for playing!")
