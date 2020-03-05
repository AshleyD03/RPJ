from Display import screen, battleFormat
import msvcrt
import random
import math

# Moves to Use
def move_damage(usr_stats, target_stats, move):
    if random.randint(1,100) > move["misschance"] - usr_stats["accuracy"] * 3 + target_stats["evasiveness"] * 3:
        dmg = math.ceil((random.randint(move["min"],move["max"]) * usr_stats["attack"] * 0.5) / (target_stats["defence"] * 0.5))
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
    move_function = move_set.get(movename, {"effect": "miss", "max":0,"min":0,"misschance":1})
    return(move_function)

def turn(move, usr, target, attack_Sprites):
    damage = move_damage(usr.stats, target.stats, move)
    # if attack is a miss
    if move["effect"] == "miss" or str(damage) == "miss":
        text = " "*18+"You missed"
        usr_sprite = usr.sprites["hurt"]; target_sprite = target.sprites["hurt"]; attack_sprite = attack_Sprites["miss"]
        damage = 0

    # if attack chosen is damage
    elif move["effect"] == "none" or move["effect"] == "priority":
        text = (" " * 10 + move["name"] + " hit for " + str(damage))
        target._damage(int(damage))
        usr_sprite = usr.sprites["attack"]; target_sprite = target.sprites["hurt"]; attack_sprite = attack_Sprites[move["name"]]
    
    # Possible changes returned to imply effect
    return({"usr" : usr,
            "target" : target,
            "usr_sprite" : usr_sprite,
            "target_sprite": target_sprite,
            "attackSprite" : attack_sprite,
            "damage" : damage,
            "bot_text" : text
            })

def battle(usr, enemy, attack_Sprites, usr_lvl):
    # Move list and possibleMoves (to check input validity)
    moves = usr.moves
    possibleMoves = []
    for i in range (len(moves)):
        possibleMoves.append(str(i+1))

    instructions = ["",""]
    # Text for Moves
    for i in range (len(moves)):
        instructions[i%2] += " "+str(i+1)+": "+moves[i]+" "*11

    # Begin Fight Loop
    while True:
        # Take normal sprite
        current_hero = usr.sprites["normal"]; current_enemy = enemy.sprites["normal"]; attackSprite = attack_Sprites["clear"]
        damage = " "
        
        display = battleFormat({"sprite": current_hero, "health": str(usr.health)}, {"sprite": current_enemy, "health": str(enemy.health)}, attackSprite, damage)
        screen(display, usr_lvl, str(usr.health), instructions, "battle")
        entry = str(msvcrt.getch())[2]
        
        # Check if move number exists and if True begin turn
        if entry in possibleMoves:
            # Collect move from move_finder
            usr_move = move_finder(moves[int(entry)-1], attack_Sprites)
            enemy_move = move_finder(random.choice(enemy.moves), attack_Sprites)
            
            bot_text = ["","tits"]

            # if usr is faster attack first
            if usr.stats["speed"] >= enemy.stats["speed"] and enemy_move["effect"] != "priority" or usr_move["effect"] == "priority":
                
                results = turn(usr_move, usr, enemy, attack_Sprites)
                usr = results["usr"]; enemy = results["target"]; bot_text[0] = results["bot_text"]

                display = battleFormat({"sprite": results["usr_sprite"], "health": str(usr.health)}, {"sprite": results["target_sprite"], "health": str(enemy.health)}, attackSprite, results["damage"])
                screen(display, usr_lvl, usr.health, bot_text, "battle")

                msvcrt.getch()

            results = turn(enemy_move, enemy, usr, attack_Sprites)
            enemy = results["usr"]; usr = results["target"]
            display = battleFormat({"sprite": results["target_sprite"], "health": str(usr.health)}, {"sprite": results["usr_sprite"], "health": str(enemy.health)}, attackSprite, results["damage"])
            screen(display, usr_lvl, usr.health, bot_text, "battle")

            msvcrt.getch()

            if usr.stats["speed"] < enemy.stats["speed"] and usr_move["effect"] != "priority" or enemy_move["effect"] == "priority":
                results = turn(usr_move, usr, enemy, attack_Sprites)
                usr = results["usr"]; enemy = results["target"]; bot_text[0] = results["bot_text"]

                display = battleFormat({"sprite": results["usr_sprite"], "health": str(usr.health)}, {"sprite": results["target_sprite"], "health": str(enemy.health)}, attackSprite, results["damage"])
                screen(display, usr_lvl, usr.health, bot_text, "battle")

                msvcrt.getch()

        if str(entry) == "q":
            break

    # After Fight Processes : return death / win / treasure / xp 
    
        


        

