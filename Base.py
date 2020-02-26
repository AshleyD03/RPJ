from Display import screen, change
from Room import Room
import msvcrt

#Global Values
usr = {"lvl": 1,
       "hp": 10,
       "x": 18,
       "y": 6,
       "last": " ",
       "room": 0}
rooms = [Room([usr["y"],usr["x"]],[[18, 7, "door", 1]])]

botText = ["line 1", "line 2"]
topText = "  LVL: " + str(usr["lvl"]) + " "*33 + "HP: " + str(usr["hp"]) + " " * (5 - len(str(usr["hp"])))

entry = "hi there"
while True:
    # Ouput Map and Take Input
    screen(rooms[usr["room"]].room, topText, botText, "room"); print(usr); print(entry); print(rooms[usr["room"]].doors)
    entry = str(msvcrt.getch())[2]
    
    # WSAD Controls
    if entry in ["w", "s", "a", "d"]:
        changes = change(entry, rooms[usr["room"]].room, usr["x"], usr["y"], usr["last"])
        rooms[usr["room"]].room = changes[0]; usr["x"] = changes[1]; usr["y"] = changes[2]; usr["last"] = changes[3]

    # Interact Control
    elif entry == "e":
        for i in range (len(rooms[usr["room"]].doors)):
            if usr["x"] == rooms[usr["room"]].doors[i]["x"] and usr["y"] == rooms[usr["room"]].doors[i]["y"]:
                # Door object, contains x, y, request & data
                door = rooms[usr["room"]].doors[i] 

                # Door Request
                if door["request"] == "door":
                    if int(len(rooms)) <= door["data"]:        
                        rooms.append(Room([door["y"],door["x"]],[[18, 7, "door", 0]]))
                    usr["room"] = door["data"]

    # Quit Control
    elif entry == "q":
        break
