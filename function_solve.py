from globals import grid, rnds, rinks
from function_possible import possible
import numpy as np
from shaping import games

my_count = 0
global draft_draw
# draft_draw = []


def solve(level=0):

    global my_count
    my_count = my_count + 1

    if my_count > 1000000:
        print("There appears to be no solution, try a smaller number of rounds")
        # print(np.array(grid))
        return
    # print(my_count)
    for y in range(0, rnds):  # cycle through the number of rounds
        # print("Thinking!!!!")
        # print(games)
        for x in range(0, (rinks*2), 2):  # cycle through the number of rinks
            # print(grid)
            if grid[y][x] == 0 and grid[y][x+1] == 0:
                # print("This is y",y,"This is x",x)
                for n in range(0, len(games[y]), 2):    # cycle through every game in the draw in that round
                    # print("This is n", n)
                    if possible(y, x, games[y][n], games[y][n+1]):
                        grid[y][x] = games[y][n]
                        grid[y][x+1] = games[y][n+1]
                        # print(level)  # print levels of recursion
                        solve(level=level+1)
                        grid[y][x] = 0
                        grid[y][x + 1] = 0
                        # print(level)

                return

    # print(np.array(grid))
    cv = np.array(grid)
    my_file = open('my_new_draw', 'wb')
    np.save(my_file, cv)
    my_file.close()
    # print(np.array(grid), file=filename)
    print(cv)
    # print(draft_draw)
    # input("More?")
    exit()
