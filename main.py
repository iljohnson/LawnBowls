import numpy as np
import funtools as ft

desired_width = 320
np.set_printoptions(linewidth=desired_width)


# To generate a tournament draw in excel in your python directory end the number of rounds and the number of teams #
# , if you enter an odd number of teams the program will add an additional team to ensure there is an even number  #
# Example ft.make_my_draw(4, 28) will produce a draw of four rounds between 28 teams using 14 rinks. If you don't   #
# enter any parameters for Example ft.make_my_draw() the program will produce a draw of 4 rounds between 32 teams  #
# using 16 rinks. The final and third input variable creates a standard sequential draw (0) and if 1 is entered    #
# the round robin fixture is randomly shuffled. If you don't enter the third variable it will default to the          #
# standard sequential draw. #

# ft.make_my_draw(rounds, number of teams, random draw)

ft.make_my_draw(6, 64, 1)



