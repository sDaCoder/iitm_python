def get_goals(filename, country):
    """
    Get the count of players and their cumulative goals for this country

    Arguments:
        filename: string
        country: string
    Return: 
        result: tuple, (integer, integer)
    """
    d = {}
    f = open(filename, 'r')

    data = f.read()
    for line in data.split("\n"):
        name, coun, goals = line.split(',')
        goals = int(goals)
        d[name] = {coun: goals}
    f.close()

    countP, countG = 0, 0
    for value in d.values():
        for coun, goals in value.items():
            if coun == country:
                countP += 1
                countG += goals

    return (-1, -1) if countP == 0 else (countP, countG)

print(get_goals("goals.csv", "Brazil"))