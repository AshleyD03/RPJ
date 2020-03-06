class Enemy():
    def __init__(self):
        self.spritename = "enemy2"
        self.moves = ["fireblast"]
        self.health = 5
        self.attack = 2
        self.defence = 2
        self.speed = 5
        self.accuracy = 5
        self.evasiveness = 5

    def _cMove(self, move, position):
        # Moves filled
        if len(self.moves) > 3:
            self.moves[position] = move
        elif position > len(self.moves):
            self.moves.append(move)
        else:
            self.moves[position] = move

class Text():
    def __init__(self):
        self.text = [" Line 1"," Line 2"]
    
class Door():
    def __init__(self):
        self.room_number = 0