"""
Need to check that:
1) Each golfer plays exactly once per day
2) The number/size of the groups is the same every day
3) Each player plays with every other player at most once


Proposed solutions:
3) Keep a dictionary of all possible pairs and increment for each pair seen. The dict key would need to be unordered.

2) Keep a tally of the group size and number of groups for every row, check if all are same, possibly as
length({(group size, number of groups)}) <= 1

1) For every row, keep a tally of the elements, a[0][0][x] in the row and add to a set, then check that the set sizes
are equal over all rows

"""
import itertools


def valid(a):
    no_of_days = len(a)
    group_sizes_and_no = set([])
    players_on_first_day = set(itertools.chain.from_iterable(a[0]))
    is_valid = True
    combinations_of_players = [set(x) for x in itertools.combinations(players_on_first_day,2)]

    for day in range(no_of_days):
        no_of_groups = len(a[day])  # for (2)

        for group in range(no_of_groups):
            group_size = len(a[day][group])  # for (2)
            group_sizes_and_no.add((no_of_groups, group_size))  # for (2)

            for x in itertools.combinations(a[day][group], 2):  # for (3)
                pair = set(x)
                if pair in combinations_of_players:
                    combinations_of_players.remove(pair)
                else:
                    is_valid = False

        if set(itertools.chain.from_iterable(a[day])) != players_on_first_day:  # for (1)
            is_valid = False

    if len(group_sizes_and_no) != 1:  # for (2)
        is_valid = False

    return is_valid


print(valid([
    ["AB", "CD", "EF", "GH"],
    ["AC", "BD", "EG", "FH"],
    ["AD", "CE"],
    ["AE", "BG", "CH", "FD"]]))
