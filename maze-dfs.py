import printmazesol

def solve(maze, start, goal):
    m = len(maze[0])
    n = len(maze)
    frontier = [(start, [start])]
    visited = set()

    while frontier:
        curr, path = frontier.pop()
        if curr in visited:
            continue 

        if curr == goal:
            return path

        visited.add(curr)
        for i, j in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            x, y = curr[0] + i, curr[1] + j
            if 0 <= x < m and 0 <= y < n and maze[x][y] == 0:
                p = path + [(x,y)]
                frontier.append(((x,y), p))

    return []



maze = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

s= solve(maze, (0,0), (4,4))
printmazesol.printmaze(maze, s)