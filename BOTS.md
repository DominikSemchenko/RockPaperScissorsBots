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