dic = {}

for _ in range(8):
    line = input()
    team = line.split(",")[0]
    wins = len(line.split(",")) - 1
    dic[team] = wins

dic = dict(sorted(dic.items(), key=lambda item: (-item[1], item[0])))

for team, wins in dic.items():
    print(f"{team}:{wins}")
    