class Stats:
    def __init__(self, health, sprites):
        self.health = health
        self.sprites = sprites


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
        "attack": {
            "fireBall": ["  ,oO",
                         " ,oO ",
                         ",oO  "],
            "miss": ["?    ",
                     "  ?  ",
                     " ?   "],
            "clear": ["     "]*3}
    })
