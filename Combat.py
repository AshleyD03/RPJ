from Display import screen, battleFormat

def battle(player, enemy, attackSprites):
    moves = []
    instructions = ["",""]
    for i in range (len(player.moves)):
        moves.append(str(i+1))
        instructions[i%2] += "player.moves"

    

    while True:
        damage = " "
        attackSprite = attackSprites["clear"]
        
        screen(battleFormat({"sprite": player.sprites, "health": player.health}, 
                            {"sprite": enemy.sprites, "health": enemy.sprites}, 
                             attackSprite, damage) 
              ,usr["lvl"]
              ,usr["floor"]
              ,
              ,"battle")
        entry = str(msvcrt.getch())
        


        

