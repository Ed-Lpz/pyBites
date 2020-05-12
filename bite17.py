import itertools 

friends = 'Amndrew Mary Susan Anna Luis Joseph Muhhammad Wong Christiano'.split()


def friends_teams(friends=friends, team_size=2, order_does_matter=False):
    if order_does_matter:
        return itertools.combinations(friends, team_size)
    else:
        return itertools.permutations(friends, team_size)
    

teams = friends_teams(friends, 2, True)
[print(team) for team in teams]