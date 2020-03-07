def output_grid(grid):
    print("X"*55)
    for y in range (8):
        print(" " * 9 + "X", end="")
        for x in range(35):
            print(grid[y][x], end="")   
        print("X")
    print("X"*55)