import random
#Generate a room
class Room:
    def __init__(self, spawn, doors):
        self.room = self.__generate(spawn)
        self.doors = []
        for i in range (len(doors)):
            self.doors.append([])
            self.doors[i] = {"x": doors[i][0],
                             "y": doors[i][1],
                             "request": doors[i][2],
                             "data": doors[i][3]}

    def __generate(self, spawn):
        room = [[" "]*36 for _ in range(8)]
        for y in range(8):
            room[y][0] = "/"
            room[y][35] = "/"
        for x in range(36):
            room[0][x] = "/"
            room[7][x] = "/"
        for z in range(50):
            room[random.randint(0,5)][random.randint(0,35)] = "/"

        room[7][17] = "["; room[7][18] = " "; room[7][19] = "]" 
        # Spawn Hero

        room[spawn[0]][spawn[1]] = "8"
        return(room)
