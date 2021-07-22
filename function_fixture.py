
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
