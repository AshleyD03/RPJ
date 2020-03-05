import msvcrt
from colored import fg, bg, attr

lines= [[" "] * 35 for _ in range(8)]
lines[0] = ["/"] * 35; lines[7] = ["/"] * 35
for i in range(1,8):
    lines[i][0] = "/"; lines[i][34] = "/"

pos = {"x": 2,
     "y": 2}

current = "o"
last = " "

# Colors
col_clear = attr('reset')
col_current = bg(196)

def change_colour(colour):
    last = lines[pos["y"]][pos["x"]]
    lines[pos["y"]][pos["x"]] = (col_current + current + col_clear)

def revert(last):
    if last == "":
        last = " "
    lines[pos["y"]][pos["x"]] = last + col_clear

def move(cmd, last):
    if cmd == "w":
        if pos["y"] - 1 < 0 :
            return()
        revert(last); pos["y"] -= 1
    if cmd == "a": 
        if pos["x"] - 1 < 0 :
            return()
        revert(last); pos["x"] -= 1
    if cmd == "s":
        if pos["y"] + 1 > 7 :
            return()
        revert(last); pos["y"] += 1
    if cmd == "d": 
        if pos["x"] + 1 > 34 :
            return()
        revert(last); pos["x"] += 1
    return(lines[pos["y"]][pos["x"]])
    
def output_grid():
    print("X"*37)
    for y in range (8):
        print("X", end="")
        for x in range(35):
            print(lines[y][x], end="")   
        print("X")
    print("X"*37)

while True:
    change_colour(col_current)
    output_grid()
    entry = str(msvcrt.getch())[2]; print(entry)

    # W/A/S/D command : move commands
    if entry in ["w","a","s","d"]:
        last = move(entry, last)

    # R command : output room value
    #elif entry == "r": 

    # Q command : quit command
    elif entry == "q":
        break