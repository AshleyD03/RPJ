from Display import screen, change
from Room import Room
from Characters import import_sprites
import msvcrt

#Global Values
usr = {"lvl": 1,
       "hp": 10,
       "x": 18,
       "y": 7,
       "last": " ",
       "room": 0}

rooms = [Room({"y": usr["y"], "x": usr["x"]},[[18, 7, "door", 1],[18,0,"door", 1]])]
rooms[usr["room"]].room[rooms[usr["room"]].spawn["y"]][rooms[usr["room"]].spawn["x"]] = "8"

possibleMoves = ["w", "s", "a", "d"]
spriteDictionary = import_sprites()

botText = ["line 1", "line 2"]
topText = "  LVL: " + str(usr["lvl"]) + " "*33 + "HP: " + str(usr["hp"]) + " " * (5 - len(str(usr["hp"])))

entry = "hi there"
while True:
    # Ouput Map and Take Input
    screen(rooms[usr["room"]].room, topText, botText, "room"); print(usr); print(entry); print(rooms[usr["room"]].doors)
    entry = str(msvcrt.getch())[2]
    
    # WSAD Controls
    if entry in possibleMoves:
        changes = change(entry, rooms[usr["room"]].room, usr["x"], usr["y"], usr["last"])
        rooms[usr["room"]].room = changes[0]; usr["x"] = changes[1]; usr["y"] = changes[2]; usr["last"] = changes[3]
        if usr["last"] != " ":
            possibleMoves = possibleMoves[possibleMoves.index(entry) + (possibleMoves.index(entry) % 2) * -2 + 1]
        else:
            possibleMoves = ["w", "s", "a", "d"]

    # Interact Control
    elif entry == "e":
        for i in range (len(rooms[usr["room"]].doors)):
            if usr["x"] == rooms[usr["room"]].doors[i]["x"] and usr["y"] == rooms[usr["room"]].doors[i]["y"]:
                # Door object, contains x, y, request & data
                door = rooms[usr["room"]].doors[i] 

                # Door Request
                if door["request"] == "door":
                    rooms[usr["room"]].room[usr["y"]][usr["x"]] = usr["last"]
                    if int(len(rooms)) <= door["data"]: #{"y": usr["y"], "x": usr["x"]}  
                        rooms.append(Room({"y": door["y"], "x": door["x"]},[[18, 7, "door", 0]]))
                    usr["room"] = door["data"]
                    usr["y"] = rooms[usr["room"]].spawn["y"]; usr["x"] = rooms[usr["room"]].spawn["x"]
                    rooms[usr["room"]].room[usr["y"]][usr["x"]] = "8"
                    
                # Battle Request
                if door["request"] == "battle":

                    print("fix this")

    # Quit Control
    elif entry == "q":
        break