from Display import screen, battleFormat
import msvcrt

import random
import math

# Moves to Use
def move_damage(usr, enemy, move):
    print(usr)
    print(enemy)
    if random.randint(1,100) > move["misschance"] - usr["character"].stats["accuracy"] * 3 + enemy.stats["evasiveness"] * 3:
        dmg = math.ceil((random.randint(move["min"],move["max"]) * usr["attack"] * 0.5) / (usr["defence"] * 0.5))
    else:
        dmg = "miss"
    return(dmg)

def move_finder(movename, attackSprites):
    # Dictionary with move_name : move_function
    move_set = {
        "fireblast": {"name": "fireBlast", "misschance" : 10, "max": 4, "min": 2, "effect" : "none"},
        "spark": {"name": "spark","misschance": 1, "max": 2, "min": 1, "effect": "priority"}
    }
    # Take function from dictionary, if not there return miss function
    move_function = move_set.get(movename, {"effect": "miss"})
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
            usr_move = move_finder(moves[int(entry)-1], attackSprites)
            enemy_move = move_finder(random.choice(enemy.moves), attackSprites)
            
            bot_text = [""," "*20+"Press to Continue"]

            # if usr is faster attack first
            if usr["character"].stats["speed"] >= enemy.stats["speed"] and enemy_move["effect"] != "priority" or usr_move["effect"] == "priority":
                if usr_move["effect"] == "miss":
                    bot_text[0] = " "*20+"You missed"

                damage = move_damage(usr, enemy, usr_move)
                enemy._damage(damage)
                current_hero == usr["character"].sprites["attack"]; current_enemy = enemy.sprites["enemy"]; attackSprite = attackSprites[usr_move["name"]]

                display = battleFormat({"sprite": current_hero, "health": str(usr["character"].health)}, {"sprite": current_enemy, "health": str(enemy.stats["health"])}, attackSprite, damage)
                screen(display, usr["lvl"], usr["floor"], bot_text, "battle")

                msvcrt.getch()

            # Enemy takes turn
            if enemy_move["effect"] == "miss":
                bot_text[0] = " "*20+"They Missed"

            
            name = "They"


            # Then if usr didnt go first attack
            if usr["character"].stats["speed"] < enemy.stats["speed"] and usr_move["effect"] != "priority" or enemy_move["effect"] == "priority":
                print("then you go")

        if str(entry) == "q":
            break

    # After Fight Processes : return death / win / treasure / xp 
    
        


        

