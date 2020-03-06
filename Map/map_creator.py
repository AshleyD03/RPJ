import msvcrt
from colored import fg, bg, attr
from Classes import Enemy

lines = [[" "] * 35 for _ in range(8)]
lines[0] = ["/"] * 35; lines[7] = ["/"] * 35
for i in range(1,8):
    lines[i][0] = "/"; lines[i][34] = "/"

settings = [["none"]*35 for _ in range(38)]

pos = {"x": 2,
     "y": 2}

current = " "
last = " "

# Colors
col_clear = attr('reset')
col_current = bg(196)

def change_current(icon, colour):
    lines[pos["y"]][pos["x"]] = (col_current + icon + col_clear)

def revert(last):
    if last == "":
        last = " "
    lines[pos["y"]][pos["x"]] = last + col_clear
    settings[pos["y"]][pos["x"]] = "none"

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

def remove(symbol):
    for y in range (8):
        for x in range (35):
            if symbol in lines[y][x]: 
                lines[y][x] = " "; break

def output_grid():
    print("X"*37)
    for y in range (8):
        print("X", end="")
        for x in range(35):
            print(lines[y][x], end="")   
        print("X")
    print("X"*37)

change_current(current, col_current)
help_line = "Helpy: Hi there Ashley o/"
while True:
    output_grid(); print("(B) - Wall    (N) - Enemy  (M) - Spawn\n(C) - Edit    (V) - Door   (,) - Delete\n"+help_line)
    entry = str(msvcrt.getch())[2]; 

    # W/A/S/D command : move commands
    if entry in ["w","a","s","d"]:
        last = move(entry, last)
        change_current(last, col_current)
        help_line = "Helpy: Move "+entry

    # Inner Rim commands check position is possible
    elif entry in ["n","m","b"] and pos["x"] not in [0,34] and pos["y"] not in [0,7]:   
        # add Enemy
        if entry == "n": 
            change_current("@", col_current); last = "@"
            settings[pos["y"]][pos["x"]] = Enemy()
            help_line = "Helpy: Enemy spawned"

        # add Spawn 
        elif entry == "m": 
            remove("S")
            change_current("S", col_current); last = "S"
            help_line = "Helpy: Spawn Moved"

        # add Wall
        elif entry == "b":
            change_current("/", col_current);  last = "/"
            help_line = "Helpy: Added Wall"

    # Inner rim used in outer check
    elif entry in ["n","m","b"]:
        help_line = "Helpy: Can't use these on outer rim"

    # add Door
    elif entry == "v":
        # horizontal door
        if pos["y"] == 0 or pos["y"] == 7:
            # Check wall distance
            if pos["x"] > 1 and pos["x"] < 33: 
                wall_touch = False
                for i in range (-1,2):
                    wall_scan = lines[pos["y"]][pos["x"] + i]
                    print(wall_scan)
                    if "[" in wall_scan  or "[" in wall_scan :
                        wall_touch = True
            
                if wall_touch == True:
                    help_line = "Helpy: Horizontal door touching door error"
                    
                else:
                    lines[pos["y"]][pos["x"] - 1] = "["; lines[pos["y"]][pos["x"] + 1] = "]"
                    change_current(" ", col_current); last = " "
                    help_line = "Helpy: Horizontal door added"
            else:
                help_line = "Helpy: Horizontal door too close to sides"

        # vertical door
        elif pos["x"] == 0 or pos["x"] == 34:
            # Chck wall distance
            if pos["y"] > 1 and pos["y"] < 6:
                wall_touch = False
                for i in range (-1,2):
                    wall_scan = lines[pos["y"] + i][pos["x"]]
                    if " " in wall_scan or "[" in wall_scan or "]" in wall_scan:
                        wall_touch = True
                if wall_touch == True:
                    help_line = "Helpy: Vertical door touching door error"
                else:
                    lines[pos["y"] - 1][pos["x"]] = "-"; lines[pos["y"] +1][pos["x"]] = "-"
                    change_current(" ", col_current); last = " "
                    help_line = "Helpy: Vertical door added"
            else:
                help_line = "Helpy: Vertical door to close to sides"

        else:
            help_line = "Helpy: Sorry, doors can only go on sides"

    # Q command : quit command
    elif entry == "q":
        break