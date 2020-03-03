from Display import screen, battleFormat
import msvcrt

import random
import math

# Moves to Use
def fireblast(usr, enemy):
    if random.randint(1,100) > 10 - usr["accuracy"] * 3 + enemy["evasiveness"] * 3:
        dmg = math.ceil((random.randint(2,4) * usr["attack"] * 0.5) / (usr["defence"] * 0.5))
    else:
        dmg = "miss"
    return(dmg) 

def miss(usr, enemey): 
    dmg = "miss"
    return(dmg)

def move_finder(movename):
    # Dictionary with move_name : move_function
    move_set = {
        "fireblast": fireblast,
    }
    # Take function from dictionary, if not there return miss function
    move_function = move_set.get(movename, miss)
    return(move_function)

def battle(usr, enemy, attackSprites):
    moves = usr["character"].moves
    instructions = ["",""]
    for i in range (len(moves)):
        instructions[i%2] += " "+str(i+1)+": "+moves[i]+" "*11

    current_hero = usr["character"].sprites["normal"]
    current_enemy = enemy.sprites["normal"]

    while True:
        damage = " "
        attackSprite = attackSprites["clear"]
        
        display = battleFormat({"sprite": current_hero, "health": str(usr["character"].health)}, {"sprite": current_enemy, "health": str(enemy.stats["health"])}, attackSprite, damage)
        screen(display, usr["lvl"], usr["floor"], instructions, "battle")
        entry = str(msvcrt.getch())[2]
        
        # Check if move number exists and if True begin turn  
        if int(entry) <= len(moves):
            # Collect move from move_finder
            move = move_finder(moves[int(entry)-1])

            # Pre-choose enemies move
            random.choice
            
            # Compare usr and enemy speed, higher attacks first 
            if usr["character"].stats["speed"] >= enemy.stats["speed"] and :
                print("you go first")

            else:
                print("they go first")
        
        if str(entry) == "q":
            break
    
        


        

