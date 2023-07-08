from random import shuffle

def _get_weight_and_name(line):
    line = line.strip()
    first_space_index = line.find(" ")
    last_space_index = line.rfind(" ")
    if first_space_index == -1:
        raise Exception(f"'{line}' must have a space after the number.")

    weight = line[last_space_index + 1:]
    if weight.isdigit():
        last_index = last_space_index
    else:
        last_index, weight = None, None
    try:
        int(line[:first_space_index - 1])
    except ValueError:  # line don't start in numeric
        return None, None
    name = line[first_space_index + 1 : last_index]

    return weight, name


def _get_teams(team_1, team_2, sub_team_1, sub_team_2):
    len_1, len_2 = len(team_1), len(team_2)
    sub_len_1, sub_len_2 = len(sub_team_1), len(sub_team_2)

    # try to make equal the len(team_1) and len(team_2)
    if len_1 == len_2:
        return team_1 + sub_team_1, team_2 + sub_team_2
    elif len_1 < len_2:
        if sub_len_1 < sub_len_2:
            return team_1 + sub_team_2, team_2 + sub_team_1
        else:
            return team_1 + sub_team_1, team_2 + sub_team_2
    else:
        if sub_len_1 < sub_len_2:
            return team_1 + sub_team_1, team_2 + sub_team_2
        else:
            return team_1 + sub_team_2, team_2 + sub_team_1


def print_2_random_soccer_teams(string):
    """
    When "player name" ends with " number", then number is the player "weight"

    string = '''
        Futbol Jueves 19 hs Juniros
        1. Player Name A 1
        2. Player Name B
        3. Player Name C 1
        4. Player Name D
    '''
    print_2_random_soccer_teams(string)
    """
    splitted = string.split("\n")

    names = dict()
    for line in splitted:
        if not line or line == "\n":
            continue
        weight, name = _get_weight_and_name(line)
        if weight is None and name is None:
            continue  # name don't start in numeric
        if not names.get(weight):
            names[weight] = list()
        names[weight].append(name)

    for lis7 in names.values():
        shuffle(lis7)

    team_1, team_2 = list(), list()
    for weight, lis7 in names.items():
        index = divmod(len(lis7), 2)[0]
        sub_team_1, sub_team_2 = lis7[:index], lis7[index:]
        team_1, team_2 = _get_teams(team_1, team_2, sub_team_1, sub_team_2)

    shuffle(team_1)
    shuffle(team_2)

    result = "*Equipo 1:*\n"
    for index, name in enumerate(team_1, 1):
        result += f"{index}. {name}\n"

    result += "\n*Equipo 2:*\n"
    for index, name in enumerate(team_2, 1):
        result += f"{index}. {name}\n"
    return result