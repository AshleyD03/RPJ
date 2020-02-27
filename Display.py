# Display screen with display[8], botText[2] and stats{lvl, lives}
def screen(display, topText, botText, style):
    print("\n" * 20) 
    # Top
    line = "@-"+"=-"*24 + "=@" 
    print(line + "\n@" + topText + "@\n" + line)
    # Center
    if style == "room": # room Styling and 36 x 8 fit
        for y in range (8):
            print(" "*6 + "@@", end="")
            for x in range (36):
                print((display[y][x]), end="")
            print("@@")

    else: # Battle Styling, just prints each line
        for y in range (8):
            print(display[y])
            
    # Bottom 
    print(line)
    for i in range (2):
        print("@  " + botText[i] + " " * (48 - len(botText[i])) + "@")
    print(line)

# Fix Me 
def battleFormat():
    hero = {"sprite" : []*5,
            "health" : 10}
    enemy = {"sprite" : []*5,
            "health" : 10}
    attack = ["   "]*3
    damage = 10
    return([" " * 40 + enemy["sprite"][0],
               " " * 40 + enemy["sprite"][1],
               "   HP:", str(hero["health"]) + " "*15-int(len(str(hero["healthy"])))+attack[0]+" "*13+enemy["sprite"][2],
               "   "+hero["sprite"][0]+" "*10+attack[1]+" "*13+enemy["sprite"][3],
               "   "+hero["sprite"][1]+" "*10+attack[2]+" "*13+enemy["sprite"][4],
               "   "+hero["sprite"][2],
               "   "+hero["sprite"][3]+" "*6+str(damage)+" "*(23-int(len(str(damage))))+"HP: "+str(enemy["health"]),
               "   "+hero["sprite"]])

def change(cmd, room, x, y, last):
    # List of barrier blocks
    barrier = ["/", "[", "]"]
    # Check possible movement
    if cmd == "w":
        if y - 1 < 0 or room[y-1][x] in barrier:
            return(room, x, y, last)
        room[y][x] = last; y -= 1
    if cmd == "a": 
        if x - 1 < 0 or room[y][x-1] in barrier:
            return(room, x, y, last)
        room[y][x] = last; x -= 1
    if cmd == "s":
        if y + 1 > 7 or room[y+1][x] in barrier:
            return(room, x, y, last)
        room[y][x] = last; y += 1
    if cmd == "d": 
        if x + 1 > 35 or room[y][x+1] in barrier:
            return(room, x, y, last)
        room[y][x] = last; x += 1
    last = room[y][x]; room[y][x] = "8"
    return([room, x, y, last])