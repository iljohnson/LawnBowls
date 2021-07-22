from globals import rinks, grid, rnds


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
