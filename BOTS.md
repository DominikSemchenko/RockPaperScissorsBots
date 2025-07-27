# TEN LEVELS OF ROCK PAPER SCISSORS AIS

## Level 1 - The random AI
The script generates a random move (1-3).
The output is unpredictable.
You have to get lucky to win.

## Level 2 - The copycat AI
The script generates a move that wins against the previous move of the player.
The output is easily predictable.
You have to not repeat your previous move to win.

## Level 3 - The anti-copycat AI
The script first gets the previous move of the player, then assumes that the player will play a move that beats the previous move of the AI. (If the AI previously played a rock, the player might think that the AI will play paper to win against the rock in the next round so the player plays scissors. Instead of playing paper, though, the AI plays rock, to win against the scissors)
The output is easily predictable.
You have to play the same move every round or play a move that would not be what the AI would play (if the AI played rock, play rock as well).

## Level 4 - The frequency AI
The script keeps track of all the moves of the player. The script generates a move that beats the most used move of the player.
The output is not easily predictable.
You have to vary your moves a lot.

## Level 5 - The frequency deque AI
The script keeps track of the last 10 moves of the player. The script generates a move that beats the most used move of the player in the last 10 moves.
The output is not easily predictable.
You have to vary your moves a lot.

## Level 6 - The markov chain AI
The script keeps track of all the moves of the player. The script generates a move that is the most likely to be played after each move of the player.
The output is not easily predictable.
You have to vary your moves a lot.

## Level 7 - The adaptive pattern AI
The script uses a pattern recognition technique, learning from the sequence of player moves, to predict the player's next move. It generates a move that beats the predicted move.
The output is not easily predictable.
You have to vary your move patterns a lot and avoid falling into predictable sequences.

## Level 8 - The ensemble AI
This script has not one mind, but three. It runs three different sub-models simultaneously.
The output is highly adaptive. If you are playing randomly, it will be unpredictable. If you fall into any kind of simple or complex pattern, the corresponding sub-model will gain reputation, and the Meta-Mind will begin to exploit that pattern against you.
You have to be more unppredictable than the three models.

## Level 9 - The sreak AI
The script keeps track of all the moves of the player and remembers the last 10 moves. The script generates a move that beats the most used move of the player in the last 10 moves. If the player has won 3 times in a row, the script generates a random move.
The output is highly unpredictable but can be exploited if the player keeps winning.
You have to be unpredictable but also make sure not to win 3 times in a row.

## Level 10 - The oracle AI
The script uses a real Machine Learning model (Scikit-learn's SGDClassifier) to learn the player's patterns in real-time (online learning) and predict their next move.
The output is highly adaptive. If you are playing randomly, it will be unpredictable. If you fall into any kind of simple or complex pattern, the AI will learn from it and use it against you.
You have to be more unpredictable than the AI.

## Level 11 - The smart ensemble AI
The script runs multiple sub-models (bots) simultaneously, each with its own strategy. The script grades each bot's prediction and updates its reputation (+1 for correct, -1 for wrong). The script then chooses the best move based on which bot has the highest reputation. Essentially, this is using the same logic as level 8, but with smarter bots.
The output is highly adaptive. If you are playing randomly, it will be unpredictable. If you fall into any kind of simple or complex pattern, the AI will learn from it and use it against you.
You have to be more unpredictable than the multiple models.