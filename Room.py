import random
#Generate a room
class Room:
    def __init__(self, spawn, walls, doors):
        self.spawn = spawn
        self.doors = []
        for i in range (len(doors)):
            self.doors.append([])
            self.doors[i] = {"x": doors[i]["x"],
                             "y": doors[i]["y"],
                             "request": doors[i]["request"],
                             "data": doors[i]["data"]}
        print(self.doors)

        self.room = self.__generate(walls, doors)

    def __generate(self, walls, doors):
        # Create Basic Square
        room = [[" "]*36 for _ in range(8)]
        for y in range(8):
            room[y][0] = "/"
            room[y][35] = "/"
        for x in range(36):
            room[0][x] = "/"
            room[7][x] = "/"
        if len(walls) != 0:
            for wall in walls:
                room[wall[0]][wall[1]] = "/"
            
        # Add doors (interactive space's look)
        for door in doors:
            # Door properties become array value, so x = 0, y=1, requet=2, data=3
            print(door)
            if door["request"] == "door":
                change = ["["," ","]"]
                pos = [door["x"] - 1, door["x"], door["x"] + 1]
                for x,y in zip(pos, change):
                    room[door["y"]][x] = y
            if door["request"] == "battle":
                room[door["y"]][door["x"]] = "@"
            if door["request"] == "text":
                room[door["y"]][door["x"]] = "?" 
        
        #room[7][17] = "["; room[7][18] = " "; room[7][19] = "]" 
        return(room)