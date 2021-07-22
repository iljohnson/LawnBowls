import numpy as np
import random


team_num = 16
rinks = int(team_num/2)
teams_r = range(0, team_num)
teams = []
rnds = 5
grid = np.zeros((rnds, (rinks * 2)), dtype=np.int64)
# my_count = 0
for t in teams_r:
    teams.append(teams_r[t]+1)
# auto generate teams list from the number of teams

random.shuffle(teams)
