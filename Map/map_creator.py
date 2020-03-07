import msvcrt
from colored import fg, bg, attr
from Classes import Enemy, Text, Door
from Functions import output_grid

rooms = []

lines = [[" "] * 35 for _ in range(8)]
lines[0] = ["/"] * 35; lines[7] = ["/"] * 35
for i in range(1,8):
    lines[i][0] = "/"; lines[i][34] = "/"
background_settings = [["none"]*35 for _ in range(38)]

pos = {"x": 2,
     "y": 2}
current = " "
last = " "

controlls = {"wall" : "1", 
             "enemy" : "2", 
             "text" : "3", 
             "spawn" : "4", 
             "door" : "5", 
             "decoration" : "6", 
             "delete" : "7", 
             "values" : "8",
             "other rooms" : "9",
             "floor code" : "0"}
# Colors
col_clear = attr('reset')
col_current = bg(196)

def change_current(icon, colour):
    lines[pos["y"]][pos["x"]] = (col_current + icon + col_clear)

def revert(last):
    if last == "":
        last = " "
    lines[pos["y"]][pos["x"]] = last + col_clear

def move(cmd, last):
    if cmd == "w":
        if pos["y"] - 1 < 0 :
            return(last)
        revert(last); pos["y"] -= 1
    if cmd == "a":
        if pos["x"] - 1 < 0 :
            return(last)
        revert(last); pos["x"] -= 1
    if cmd == "s":
        if pos["y"] + 1 > 7 :
            return(last)
        revert(last); pos["y"] += 1
    if cmd == "d":
        if pos["x"] + 1 > 34 :
            return(last)
        revert(last); pos["x"] += 1
    return(lines[pos["y"]][pos["x"]])

def remove_All(symbol):
    for y in range (8):
        for x in range (35):
            if symbol in lines[y][x]:
                lines[y][x] = " "; break

change_current(current, col_current)
help_line = "\n Helpy: Hi there Ashley o/"
while True:
    print(background_settings[7])
    output_grid(lines); print("(B) - Wall    (N) - Enemy  (M) - Spawn\n(C) - Edit    (V) - Door   (,) - Delete\n"+help_line)
    entry = str(msvcrt.getch())[2]; 

    # W/A/S/D command : move commands
    if entry in ["w","a","s","d"]:
        last = move(entry, last)
        change_current(last, col_current)
        help_line = "\n Helpy: Moved ya in direction ("+entry+")"

    # Q command : quit command
    elif entry == "q":
        break

    # Adding commands : 
    else: 
        
        if background_settings[pos["y"]][pos["x"]] != "none":
            help_line = "\n Helpy: Sorry, but an obejcts already there"

        # add Enemy
        elif entry == "n": 
            change_current("@", col_current); last = "@"
            background_settings[pos["y"]][pos["x"]] = Enemy()
            help_line = "\n Helpy: I'll spawn you an Enemy :D "

        # add Spawn 
        elif entry == "m": 
            remove_All("S")
            change_current("S", col_current); last = "S"
            help_line = "\n Helpy: I've moved your spawn :>"

        # add Wall
        elif entry == "b":
            change_current("/", col_current);  last = "/"
            help_line = "\n Helpy: I've added a wall :D "

        # add Door
        elif entry == "v":
            # horizontal door
            if pos["y"] == 0 or pos["y"] == 7:
                # Check wall distance
                if pos["x"] > 1 and pos["x"] < 33: 
                    wall_touch = False
                    for i in range (-1,2):
                        wall_scan = background_settings[pos["y"]][pos["x"] + i ]
                        print(wall_scan)
                        if wall_scan != "none":
                            wall_touch = True  

                    if wall_touch == True:
                        help_line = "\n Helpy: I Can't do that, it's touching a door :I"
                        
                    else:
                        lines[pos["y"]][pos["x"] - 1] = "["; lines[pos["y"]][pos["x"] + 1] = "]"; background_settings[pos["y"]][pos["x"] - 1] = "door_side"; background_settings[pos["y"]][pos["x"]] = Door(); background_settings[pos["y"]][pos["x"] + 1] = "door_side"
                        change_current(" ", col_current); last = " "
                        help_line = "\n Helpy: I'll add a horizontal door ;D"
                else:
                    help_line = "\n Helpy: Sorry, but that door's too close to the sides :3"

            # vertical door
            elif pos["x"] == 0 or pos["x"] == 34:
                # Chck wall distance
                if pos["y"] > 1 and pos["y"] < 6:
                    wall_touch = False
                    for i in range (-1,2):
                        wall_scan = background_settings[pos["y"] + i][pos["x"]]
                        print(wall_scan)
                        if wall_scan != "none":
                            wall_touch = True

                    if wall_touch == True:
                        help_line = "\n Helpy: I Can't do that, it's touching a door :I"
                    else:
                        lines[pos["y"] - 1][pos["x"]] = "-"; lines[pos["y"] + 1][pos["x"]] = "-";background_settings[pos["y"] - 1][pos["x"]] = "door_side"; background_settings[pos["y"]][pos["x"]] = Door(); background_settings[pos["y"] + 1][pos["x"]] = "door_side"
                        change_current(" ", col_current); last = " "

                        help_line = "\n Helpy: I'll add a vertical door ;D"
                else:
                    help_line = "\n Helpy: Sorry, but that door's too close to the sides :3"

            else:
                help_line = "\n Helpy: Sorry, but doors go on the side line :I"
