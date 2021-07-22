import numpy as np
from globals import teams, team_num
from function_fixture import my_fixture


# matches = my_fixture(teams)

# games is every possible combination for a full round robin draw.

games = np.reshape(my_fixture(teams), (team_num-1, team_num))
