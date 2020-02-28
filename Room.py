import random
#Generate a room
class Room:
    def __init__(self, spawn, doors):
        self.spawn = spawn
        self.doors = []
        for i in range (len(doors)):
            self.doors.append([])
            self.doors[i] = {"x": doors[i][0],
                             "y": doors[i][1],
                             "request": doors[i][2],
                             "data": doors[i][3]}
        print(self.doors)
        self.room = self.__generate(doors)

    def __generate(self, doors):
        # Create Basic Square
        room = [[" "]*36 for _ in range(8)]
        for y in range(8):
            room[y][0] = "/"
            room[y][35] = "/"
        for x in range(36):
            room[0][x] = "/"
            room[7][x] = "/"
        
        # Add doors (interactive space's look)
        for door in doors:
            # Door properties become array value, so x = 0, y=1, requet=2, data=3
            print(door)
            if door[2] == "door":
                change = ["["," ","]"]
                pos = [door[0] - 1, door[0], door[0] + 1]
                for x,y in zip(pos, change):
                    room[door[1]][x] = y
        
        #room[7][17] = "["; room[7][18] = " "; room[7][19] = "]" 
        return(room)