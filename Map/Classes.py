class Enemy():
    def __init__(self):
        self.id = "enemy"
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
        self.id = "text"
        self.text = [" Line 1 - Change Me"," Line 2 - Me Too"]
    
class Door():
    def __init__(self):
        self.id = "door"
        self.room_number = 0

class Spawn():
    def __init__(self):
        self.id = "spawn"

class Decoration(): 
    def __init__(self, decor): 
        self.id = "decoration"
        self.decoration = decor
