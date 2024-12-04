def printmaze(maze, path):
    for i, j in path:
        maze[i][j] = "X"

    for i in maze:
        for j in i:
            print(j, end = " ")
        print()