from Display import screen, change
from Room import Room
from Characters import import_sprites, Character
from Combat import battle
import msvcrt

spriteDictionary = import_sprites()

#Global Values
usr = {"lvl": 1,
       "x": 18,
       "y": 7,
       "last": " ",
       "room": 0,
       "floor": 1,
       "character": Character(spriteDictionary["character"]["hero"], ["fireblast","tictoc","woosh"], {"health": 10, "attack": 2, "defence": 2, "speed": 5, "accuracy": 5, "evasiveness": 5, "xp": 0})}

# Create Room List 
rooms = [Room({"y": usr["y"], "x": usr["x"]},["eaea","6f02fff","5fff","4ff00f","3ff","23"],[{"x": 18, "y": 7, "request": "door", "data": 1},{"x": 18, "y": 0, "request": "door", "data": 1},{"x": 12, "y": 3, "request": "text", "data": [" Bottom"," Top"]},{"x": 17, "y": 6, "request": "battle", "data": Character(spriteDictionary["character"]["enemy2"], ["fireblast"], {"health": 5, "attack": 2, "defence": 2, "speed": 5, "accuracy": 5,"evasiveness": 5})}])]
# Spawn Player
rooms[usr["room"]].room[rooms[usr["room"]].spawn["y"]][rooms[usr["room"]].spawn["x"]] = "8"

possibleMoves = ["w", "s", "a", "d"]

botText = ["line 1", "line 2"]#("  LVL: " + str(usr["lvl"]) + " "*33 + "HP: " + str(usr["character"].health) + " " * (5 - len(str(usr["character"].health))))

entry = "hi there"
while True:
    # Ouput Map and Take Input
    screen(rooms[usr["room"]].room, usr["lvl"], usr["character"].health, botText, "room")
    #print(usr); print(entry); print(rooms[usr["room"]].doors)
    entry = str(msvcrt.getch())[2]
    
    # WSAD Controls
    if entry in possibleMoves:
        # Reset text
        botText = ["line 1", "line 2"]

        changes = change(entry, rooms[usr["room"]].room, usr["x"], usr["y"], usr["last"])
        rooms[usr["room"]].room = changes[0]; usr["x"] = changes[1]; usr["y"] = changes[2]; usr["last"] = changes[3]
        if usr["last"] != " ":
            possibleMoves = possibleMoves[possibleMoves.index(entry) + (possibleMoves.index(entry) % 2) * -2 + 1]
        else:
            possibleMoves = ["w", "s", "a", "d"]

    # Interact Control / Interact with door dictionary in current room.doors 
    elif entry == "e":
        # Find current door
        for door in rooms[usr["room"]].doors:
            if usr["x"] == door["x"] and usr["y"] == door["y"]:
                # Door Request
                if door["request"] == "door":
                    rooms[usr["room"]].room[usr["y"]][usr["x"]] = usr["last"]

                    # -= Delete This =-
                    if int(len(rooms)) <= door["data"]: #{"y": usr["y"], "x": usr["x"]}  
                        rooms.append(Room({"y": door["y"], "x": door["x"]},["eeeea","abab08","b00b","beeb","a001","787878"],[{"x": 18, "y": 7, "request": "door", "data": 0}]))
                    # -= Delete This =-

                    usr["room"] = door["data"]
                    usr["y"] = rooms[usr["room"]].spawn["y"]; usr["x"] = rooms[usr["room"]].spawn["x"]
                    rooms[usr["room"]].room[usr["y"]][usr["x"]] = "8"
                    
                # Battle Request
                elif door["request"] == "battle":
                    battle(usr["character"], door["data"], spriteDictionary["attacks"], usr["lvl"])
                    
                # Text Request
                elif door["request"] == "text":
                    botText = [door["data"][0],door["data"][1]]


    # Quit Control
    if entry == "q":
        break