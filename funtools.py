import numpy as np
import random
import pandas as pd

desired_width = 320
np.set_printoptions(linewidth=desired_width)

# -------------------------------- Module Variables Global Variables ----------------------------- #

team_num = 32
rnds = 6
rinks = 0
teams = []
games = []
grid = []
my_count = 0
init_draw = []
init_update = []
header = []
final_draw = []


# -------------------------------- Module Functions ---------------------------------- #


def my_fixture(no_of_teams):

    if len(no_of_teams) % 2 != 0:
        no_of_teams.append(0)  # if team number is odd - use 'day off' as fake team

    rotation = list(no_of_teams)       # copy the list
    fixtures = []
    full_draw = []

    for i in range(0, len(no_of_teams)-1):
        fixtures.append(rotation)
        rotation = [rotation[0]] + [rotation[-1]] + rotation[1:-1]

    for f in fixtures:
        n = len(f)
        full_draw.append(list(zip(f[0:int(n / 2)], reversed(f[int(n / 2):n]))))

    return full_draw

# --------------------------------------------------------------------------------------------------- #


def reshape():
    global games
    teams_r = range(0, team_num)
    for t in teams_r:
        teams.append(teams_r[t]+1)
    random.shuffle(teams)
    games = np.reshape(my_fixture(teams), (team_num-1, team_num))
    return


# ---------------------------------------------------------------------------------------------- #

def possible(y, x, n, m):

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


# ----------------------------------------------------------------------------------------------- #


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
                        #  print(level)

                return

    # print(np.array(grid))
    cv = np.array(grid)
    my_file = open('my_new_draw', 'wb')
    np.save(my_file, cv)
    my_file.close()
    # print(np.array(grid), file=filename)
    print(cv)
    # input("More?")
    arrange_export()
    exit()


# ---------------------------------------------------------------------------------------------- #

def create_draw():  # Used to create init_draw
    z = []
    for t in range(1, team_num+1):
        z.append(t)

    t_arr = np.array(z)
    new_t = t_arr.reshape((team_num, 1))

    draw_grid = np.zeros((team_num, (rnds * 2)), dtype=np.int64)

    draw_grid = np.append(new_t, draw_grid, 1)

    return draw_grid

# ----------------------------LOAD DRAW AND CREATE TOURNAMENT DRAW ------------------------------------------ #


def create_tournament_draw():
    my_file = open('my_new_draw', 'rb')
    t_draw = np.load(my_file)
    global init_draw

    for r in range(0, rnds):  # loop through each round

        for q1 in range(0, team_num):  # loop through each team in init_draw
            for p1 in range(0, team_num, 2):  # loop through the teams in t_draw starting at 0 in steps of 2
                if init_draw[q1][0] == t_draw[r][p1]:  # compare teams numbers to left team number of game
                    rink = divmod(p1, 2)
                    init_draw[q1][1 + 2*r] = rink[0]+1  # calculate and insert rink for game into init_draw
                    init_draw[q1][2 + 2*r] = t_draw[r][p1+1]
                    # when there is a match take the Vs team and insert into init_draw

        for q2 in range(0, team_num):  # loop through each team in init_draw
            for p2 in range(1, team_num, 2):  # loop through the teams in t_draw starting at 1 in steps of 2
                if init_draw[q2][0] == t_draw[r][p2]:  # compare teams numbers to right team number of game
                    rink = divmod(p2, 2)
                    init_draw[q2][1 + 2*r] = rink[0]+1  # calculate and insert rink for game into init_draw
                    init_draw[q2][2 + 2*r] = t_draw[r][p2-1]
                    # when there is a match take the Vs team and insert into init_draw
    return init_draw


# ------------------------------------CREATE HEADER ---------------------------------------------------------- #

def make_header():
    global header
    header = np.full([1, (rnds*2)+1], "", dtype="<U10")

    header[0, 0] = "Team No"
    rnd_count = 1
    for x in range(1, rnds*2, 2):

        header[0, x] = "Rink"
        header[0, x+1] = "Rnd " + str(rnd_count)
        rnd_count += 1
    return header

# ----------------------------ADD HEADER TO DRAW AND EXPORT---------------------------------------------------- #


def add_header_export_draw():
    global final_draw
    final_draw = np.append(header, init_update, axis=0)
    my_name = 'No of Teams ' + str(team_num) + ' No of Rnds ' + str(rnds)
    df = pd.DataFrame(final_draw)
    df.to_excel('output_data.xlsx', sheet_name=my_name, index=False, header=False)
    return final_draw

# ------------------------------------------------------------------------------------------------------------- #


def arrange_export():
    global init_draw
    global init_update
    global header
    init_draw = (create_draw())
    init_update = create_tournament_draw()
    header = make_header()
    add_header_export_draw()
    return
# -------------------------------------------------------------------------------------------------------------- #


def make_my_draw(num_of_rnds=4, num_of_teams=32):
    global rnds
    global team_num
    global grid
    global rinks
    global init_draw
    global init_update
    global header
    rnds = num_of_rnds
    team_num = num_of_teams
    if team_num % 2 != 0:
        team_num = team_num + 1
    rinks = int(team_num/2)
    grid = np.zeros((rnds, (rinks * 2)), dtype=np.int64)
    reshape()
    solve()
    return

# ------------------------------------------------------------------------------------------------ #
