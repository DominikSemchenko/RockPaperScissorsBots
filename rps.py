import uuid

class RPSGame:
    def __init__(self):
        self.player1 = str(uuid.uuid4())
        self.player2 = str(uuid.uuid4())
        self.moves = {}
        self.win_combinations = {
    3: 2,  # Scissors beat Paper
    2: 1,  # Paper beats Rock
    1: 3   # Rock beats Scissors
} 
    def get_players(self):
        return self.player1, self.player2
    
    def move(self, player, move):
        if player == self.player1:
            self.moves["player1"] = move
        else:
            self.moves["player2"] = move

        if "player1" in self.moves and "player2" in self.moves:
            if self.win_combinations[self.moves["player1"]] == self.moves["player2"]:
                winner = self.player1
            elif self.win_combinations[self.moves["player2"]] == self.moves["player1"]:
                winner = self.player2
            else:
                winner = "tie"

            self.moves = {}
            return winner

        return