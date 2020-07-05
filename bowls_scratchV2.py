
import random
import numpy as np
import pandas as pd
import os.path
import time

desired_width = 320
np.set_printoptions(linewidth=desired_width)


# ROUND ROBIN CODE


def my_fixture(no_of_teams):

    if len(teams) % 2 != 0:
        a = 'Bye -' + str(len(teams)+1)
        teams.append(a)  # if team number is odd - use 'day off' as fake team

    rotation = list(no_of_teams)       # copy the list
    fixtures = []
    func_full_draw = []

    for i in range(0, len(teams)-1):
        fixtures.append(rotation)
        rotation = [rotation[0]] + [rotation[-1]] + rotation[1:-1]

    for f in fixtures:
        n = len(f)
        func_full_draw.append(list(zip(f[0:int(n / 2)], reversed(f[int(n / 2):n]))))

    return func_full_draw

# -------------------------------------------------------------------------------------------------------------------


def ditch_rinks(green_1=1, green_2=1, green_3=1, green_4=1):

    dr = [0]

    if green_1 == 8 or green_1 == 7:
        dr = [dr[-1]+1] + [dr[-1]+green_1]
    else:
        dr = print('You must enter at least one rink and the rink size must be 7 or 8')
    if green_2 == 8 or green_2 == 7:
        dr = dr + [dr[-1]+1] + [dr[-1]+green_2]
    if green_3 == 7 or green_3 == 8:
        dr = dr + [dr[-1]+1] + [dr[-1]+green_3]
    if green_4 == 7 or green_4 == 8:
        dr = dr + [dr[-1]+1] + [dr[-1]+green_4]
    return dr


# ------------------------------------------------------------------------------------------------------------------

def rink_use_array(teams):

    import numpy as np
    a = np.array(range(1, teams + 1))
    b = np.array([0 for x in range(0, teams * 4)])
    c = np.append(a, b).reshape(5, teams).transpose()
    return c

# ------------------------------------------------------------------------------------------------------------------


homepath = os.path.expanduser("~\\Desktop")

# User Inputs


ip1 = int(input('Enter the number of teams (must be greater than  2)......default value is 32  ') or '32')
ip2 = int(input('Enter the number of available rinks (must be greater than 2)......default value is 16  ') or '16')
ip3 = int(input('Enter the number of rounds to be played (must be greater than 1......default value is 4  ') or '4')
ip4 = int(input('Enter the number of rinks for green One (must be 7 or 8)......default value is 8  ') or '8')
ip5 = int(input('Enter the number of rinks for green Two (can be any number).....default value is 8  ') or '8')
ip6 = int(input('Enter the number of rinks for green Three (can be any number)......default value is 8  ') or '8')
ip7 = int(input('Enter the number of rinks for green Four (can be any number)......default value is 8  ') or '8')
print('The output file will be saved in the users Desktop')



def do_draw(a, b, c):

    team_num = a
    avail_rinks = b
    rnds = c

    greens_dim = ditch_rinks(ip4, ip5, ip6, ip7)

    teams_r = range(0, team_num)

    global teams
    teams = []

    # rink_array = rink_use_array(team_num)

    if team_num % 2 != 0:
        rink_array = rink_use_array(team_num+1)
    else:
        rink_array = rink_use_array(team_num)

    # rink_array_usage = rink_use_array(team_num)

    if team_num % 2 != 0:
        rink_array_usage = rink_use_array(team_num+1)
    else:
        rink_array_usage = rink_use_array(team_num)

    for t1 in teams_r:
        teams.append(f"Team {teams_r[t1]+1}")  # auto generate teams list from the number of teams

    full_draw = my_fixture(teams)

    check = []  # place each team and rink allocation in here

    draw = []   # output - shows fixture and rink allocation per

    con_games = list(range(0, team_num % 2 + int(team_num/2), 1))
    # The number of concurrent games that can be played which is N/2 if MOD %2
    rinks = list(range(1, avail_rinks+1, 1))
    random.shuffle(rinks)

    global wm
    global op
    global t

    r = 0         # set rnd loop counter to 0
    t = 0         # loop try counter
    wm = []
    op = []

    while r != rnds:
        rc = []  # reset rc to empty

        for m in con_games:

            a = f"{full_draw[r][m][0]} Rink {rinks[0]}"
            b = f"{full_draw[r][m][1]} Rink {rinks[0]}"
            c = [a, b]
            # d = rinks[m]

            # print(full_draw)
            y = int(full_draw[r][m][0][5:])
            z = int(full_draw[r][m][1][5:])

            while any(x in c for x in check) or rinks[0] in rc:

                # keep changing the rink number until neither team has used that rink before
                rinks = rinks[1:] + [rinks[0]]  # rotate rinks anti clockwise until you find a clear rink
                a = f"{full_draw[r][m][0]} Rink {rinks[0]}"  # update "a" while in the loop
                b = f"{full_draw[r][m][1]} Rink {rinks[0]}"  # update "b" while in the loop
                c = [a, b]
                t += 1

                if t > 100:
                    break

            check.append(f"{full_draw[r][m][0]} Rink {rinks[0]}")
            check.append(f"{full_draw[r][m][1]} Rink {rinks[0]}")

    # ------------------------------- record how many games per team on a ditch rink ----------------------------------

            if len(greens_dim) >= 2 and (greens_dim[0] == rinks[0] or greens_dim[1] == rinks[0]):
                rink_array[y - 1][1] = rink_array[y - 1][1] + 1
                rink_array[z - 1][1] = rink_array[z - 1][1] + 1
            if len(greens_dim) >= 4 and (greens_dim[2] == rinks[0] or greens_dim[3] == rinks[0]):
                rink_array[y - 1][2] = rink_array[y - 1][2] + 1
                rink_array[z - 1][2] = rink_array[z - 1][2] + 1
            if len(greens_dim) >= 6 and (greens_dim[4] == rinks[0] or greens_dim[5] == rinks[0]):
                rink_array[y - 1][3] = rink_array[y - 1][3] + 1
                rink_array[z - 1][3] = rink_array[z - 1][3] + 1
            if len(greens_dim) == 8 and (greens_dim[6] == rinks[0] or greens_dim[7] == rinks[0]):
                rink_array[y - 1][4] = rink_array[y - 1][4] + 1
                rink_array[z - 1][4] = rink_array[z - 1][4] + 1

    # ----------------------------- record how many games per team on each green --------------------------------------
            if len(greens_dim) >= 2 and (greens_dim[0] <= rinks[0] <= greens_dim[1]):
                rink_array_usage[y - 1][1] = rink_array_usage[y - 1][1] + 1  # --- first team of pair on A green
                rink_array_usage[z - 1][1] = rink_array_usage[z - 1][1] + 1  # --- second team of pair on A green

            if len(greens_dim) >= 4 and (greens_dim[2] <= rinks[0] <= greens_dim[3]):
                rink_array_usage[y - 1][2] = rink_array_usage[y - 1][2] + 1
                rink_array_usage[z - 1][2] = rink_array_usage[z - 1][2] + 1

            if len(greens_dim) >= 6 and (greens_dim[4] <= rinks[0] <= greens_dim[5]):
                rink_array_usage[y - 1][3] = rink_array_usage[y - 1][3] + 1
                rink_array_usage[z - 1][3] = rink_array_usage[z - 1][3] + 1

            if len(greens_dim) == 8 and (greens_dim[6] <= rinks[0] <= greens_dim[7]):
                rink_array_usage[y - 1][4] = rink_array_usage[y - 1][4] + 1
                rink_array_usage[z - 1][4] = rink_array_usage[z - 1][4] + 1

    # --------------------------------------------------------------------------------------------------------------

            draw.append(f"Rnd {r + 1} {full_draw[r][m][0]}  {full_draw[r][m][1]} Rink {rinks[0]}")
            rc.append(rinks[0])
            rinks = rinks[1:] + [rinks[0]]  # rotate rinks anti clockwise once
            if t > 100:
                break

            if m == len(con_games)-1:
                r = r + 1
                # probably want to rotate the rinks 5 rinks between rounds
                rinks = rinks[4:] + rinks[:4]
                #random.shuffle(rinks)
        if t > 100:

            break

    if len(wm) == 0 and t < 100 and team_num % 2 == 0:
        op = np.transpose(np.array(draw).reshape(rnds, int(team_num / 2)))
        return op, rink_array, rink_array_usage
    elif len(wm) == 0 and t < 100 and team_num % 2 != 0:
        op = np.transpose(np.array(draw).reshape(rnds, int((team_num+1) / 2)))
        return op, rink_array, rink_array_usage
    else:
        print('Error - Too may rounds for the number of rinks available....try again')


try:

    xy = (do_draw(ip1, ip2, ip3))

    if len(wm) == 0 and t < 100:
        xy0 = pd.DataFrame(xy[0])
        xy1 = pd.DataFrame(xy[1])
        xy2 = pd.DataFrame(xy[2])
        writer = pd.ExcelWriter(os.path.join(homepath, 'My_Bowls_Draw.xls'))

        xy0.to_excel(writer, sheet_name='Draw', index=False)
        xy1.to_excel(writer, sheet_name='Ditch Rinks Usage', index=False)
        xy2.to_excel(writer, sheet_name='Green Usage', index=False)
        writer.save()
        print('your output file has been saved to ', os.path.join(homepath, 'My_Bowls_Draw.xls'))
        time.sleep(10)
except:

    print('There was an error adjust your values and try again')
    time.sleep(10)


















