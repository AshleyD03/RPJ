import random
import math

class Character:
    def __init__(self, sprites, moves, stats):
        self.sprites = sprites

        self.moves = moves
        if len(self.moves) >= 4:
            for i in range(4-len(self.moves)):
                self.moves.append("none")

        # stats made of health, attack, defence, speed and xp
        self.stats = stats
        self.health = self.stats["health"]

    # Take damage Function
    def _damage(self, damage):
        self.health -= damage

    # Check if dead function
    def _alive(self):
        if self.health <= 0:
            return(False)
        else:
            return(True)

def import_sprites():
    return({
        "character": {
            "hero": {"normal": ["  _      ",
                                "_|^|_    ",
                                "(*_*) O  ",
                                ",-|-,|   ",
                                "_||_|    "],
                     "attack": ["  _      ",
                                "_|^|_ * $",
                                "(*_*) 0* ",
                                ",-|-,|   ",
                                "_||_|    "],
                     "hurt": ["  _      ",
                              "_|^|_    ",
                              "(X_X)    ",
                              ",-|-,    ",
                              "_||_ ___o"]},
            "enemy1": {"normal": ["         ",
                                  "  ¬¬_¬¬  ",
                                  "  ('_')  ",
                                  "  !-|-   ",
                                  "  _||_   "],
                       "attack": ["         ",
                                  "  ¬¬_¬¬  ",
                                  "  (^O^)  ",
                                  "  !-|-   ",
                                  "  _||_   "],
                       "hurt": ["         ",
                                "  ¬¬_¬¬  ",
                                "  (X-X)  ",
                                "   -|-   ",
                                "  _||_   "]},
            "enemy2": {"normal": ["^  ___   ",
                                  "| ('_')  ",
                                  "|'=|O|=[]",
                                  "|  V|V ']",
                                  " _|| ||_ "],
                       "attack": ["^  ___   ",
                                  "| (UwU)  ",
                                  "|'=|O|=[]",
                                  "|  V|V ']",
                                  " _|| ||_ "],
                       "hurt": ["   ___   ",
                                "^ (x-x)  ",
                                "| .|O|.  ",
                                "|' V|V ']",
                                "|_|| ||_]"]},
            "clear": ["         "]*5},
        "attacks": {
            "fireBall": ["  ,oO",
                         " ,oO ",
                         ",oO  "],
            "miss": ["?    ",
                     "  ?  ",
                     " ?   "],
            "clear": ["     "]*3}
    })
