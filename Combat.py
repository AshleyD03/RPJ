from Display import screen, battleFormat
import msvcrt

import random
import math

# Moves to Use
def move_damage(usr, enemy, move):
    if random.randint(1,100) > move["misschance"] - usr["accuracy"] * 3 + enemy["evasiveness"] * 3:
        dmg = math.ceil((random.randint(move["min"],move["max"]) * usr["attack"] * 0.5) / (usr["defence"] * 0.5))
    else:
        dmg = "miss"
    return(dmg)

def move_finder(movename):
    # Dictionary with move_name : move_function
    move_set = {
        "fireblast": {"misschance" : 10, "max": 4, "min": 2, "effect" : "none"},
        "spark": {"misschance": 1, "max": 2, "min": 1, "effect": "priority"}
    }
    # Take function from dictionary, if not there return miss function
    move_function = move_set.get(movename, {"effcet": "none"})
    return(move_function)

def battle(usr, enemy, attackSprites):
    # Move list and possibleMoves (to check input validity)
    moves = usr["character"].moves
    possibleMoves = []
    for i in range (len(moves)):
        possibleMoves.append(str(i+1))

    instructions = ["",""]
    # Text for Moves
    for i in range (len(moves)):
        instructions[i%2] += " "+str(i+1)+": "+moves[i]+" "*11

    # Take normal sprite
    current_hero = usr["character"].sprites["normal"]; current_enemy = enemy.sprites["normal"]

    # Begin Fight Loop
    while True:
        damage = " "
        attackSprite = attackSprites["clear"]
        
        display = battleFormat({"sprite": current_hero, "health": str(usr["character"].health)}, {"sprite": current_enemy, "health": str(enemy.stats["health"])}, attackSprite, damage)
        screen(display, usr["lvl"], usr["floor"], instructions, "battle")
        entry = str(msvcrt.getch())[2]
        
        # Check if move number exists and if True begin turn
        if entry in possibleMoves:
            # Collect move from move_finder
            usr_move = move_finder(moves[int(entry)-1])
            enemy_move = move_finder(random.choice(enemy.moves))
            
            # if usr is faster attack first
            if usr["character"].stats["speed"] >= enemy.stats["speed"] and enemy:
                print("you go first")

            # Enemy takes turn
            print("they go first")

            # Then if usr didnt go first attack
            if usr["character"].stats["speed"] >= enemy.stats["speed"] and :

        if str(entry) == "q":
            break

    # After Fight Processes : return death / win / treasure / xp 
    
        


        

