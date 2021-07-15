import numpy as np
import random

desired_width = 320
np.set_printoptions(linewidth=desired_width)

team_num = 30
rinks = int(team_num/2)  #

rnds = 8


teams_r = range(0, team_num)

teams = []

for t in teams_r:
    teams.append(teams_r[t]+1)  # auto generate teams list from the number of teams


# random.shuffle(teams)


def my_fixture(no_of_teams):

    if len(teams) % 2 != 0:
        teams.append(0)  # if team number is odd - use 'day off' as fake team

    rotation = list(no_of_teams)       # copy the list
    fixtures = []
    full_draw = []

    for i in range(0, len(teams)-1):
        fixtures.append(rotation)
        rotation = [rotation[0]] + [rotation[-1]] + rotation[1:-1]

    for f in fixtures:
        n = len(f)
        full_draw.append(list(zip(f[0:int(n / 2)], reversed(f[int(n / 2):n]))))

    return full_draw


matches = my_fixture(teams)


# print(matches)


games = np.reshape(matches, (team_num-1, team_num))

grid = np.zeros((rnds, (rinks * 2)), dtype=np.int64)


def possible(y, x, n, m):
    global grid
    # print(y,x,n,m)

    for k in range(0, (rinks * 2)):  # 0 to 16
        if grid[y][k] == n or grid[y][k] == m:
            return False  # check in the row for n or m
    for i in range(0, rnds):  # 0 to 5
        if grid[i][x] == n or grid[i][x] == m:
            return False  # check in the column for m or n (has either team played on that rink)
        if grid[i][x+1] == n or grid[i][x+1] == m:
            return False  # check in the column for m or n (has either team played on that rink)
    return True
# y is the round number from the number of rounds set
# x = rink number from the number of rinks available (starts at 0 and counts by 2 - so 0 to 15 for 8 rinks


my_count = 0


def solve(level=0):

    global grid
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

    print(np.array(grid))
    # print(y0)
    input("More?")


solve()
