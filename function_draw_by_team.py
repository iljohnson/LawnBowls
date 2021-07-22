import numpy as np
import pandas as pd
from globals import rnds, team_num

desired_width = 320
np.set_printoptions(linewidth=desired_width)


def create_draw(number_of_rounds, number_of_teams):
    z = []
    for t in range(1, team_num+1):
        z.append(t)

    t_arr = np.array(z)
    new_t = t_arr.reshape((team_num, 1))

    draw_grid = np.zeros((team_num, (rnds * 2)), dtype=np.int64)

    draw_grid = np.append(new_t, draw_grid, 1)

    return draw_grid

    # ----------------------------LOAD DRAW AND CREATE TOURNAMENT DRAW ------------------------------------------ #


def create_tournament_draw (number_of_rounds,number_of_teams, my_init_draw ):

    my_file = open('my_new_draw', 'rb')
    t_draw = np.load(my_file)
    t_d = 0
    l_r = 0
    for r in range(0, rnds):  # loop through each round

        for q1 in range(0, team_num):  # loop through each team in init_draw
            for p1 in range(0, team_num, 2): # loop through the teams in t_draw starting at 0 in steps of 2
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


def make_header(number_of_rounds):
    header = np.full([1, (rnds*2)+1], "", dtype="<U10")

    header[0,0] = "Team No"
    rnd_count = 1
    for x in range(1, rnds*2, 2):

        header[0, x] = "Rink"
        header[0, x+1] = "Rnd " + str(rnd_count)
        rnd_count += 1
    return header

    # ----------------------------ADD HEADER TO DRAW AND EXPORT---------------------------------------------------- #


def add_header_export_draw(number_of_rnds, number_of_teams, initial_draw_update, the_header):
    final_draw = np.append(header, init_update, axis=0)
    my_name = 'No of Teams ' + str(team_num) + ' No of Rnds ' + str(rnds)
    df = pd.DataFrame(final_draw)
    df.to_excel('output_data.xlsx', sheet_name=my_name, index=False, header=False)
    return final_draw
    # ------------------------------------------------------------------------------------------------------------- #


def arrange_export(number_of_rnds, number_of_teams):
    global init_draw
    global init_update
    global header
    init_draw = (create_draw(rnds, team_num))
    init_update = create_tournament_draw(rnds, team_num, init_draw)
    header = make_header(rnds)
    add_header_export_draw(rnds, team_num, init_update, header)
    return
    # -------------------------------------------------------------------------------------------------------------- #

arrange_export(rnds, team_num)

