from collections import OrderedDict
T = input()

for t in range(int(T)):
    d = {}
    for i in range(12):
        s = input()
        s_array = s.split()
        team_1 = s_array[0]
        team_2 = s_array[-1]
        score_1 = int(s_array[1])
        score_2 = int(s_array[-2])
        if team_1 not in d:
            if score_1>score_2:
                d[team_1] = [3,score_1-score_2]
            elif score_1<score_2:
                d[team_1] = [0,score_1-score_2]
            else:
                d[team_1] = [1,score_1-score_2]
        else:
            if score_1>score_2:
                d[team_1] = [d[team_1][0]+3,d[team_1][1]+score_1-score_2]
            elif score_1<score_2:
                d[team_1] = [d[team_1][0]+0,d[team_1][1]+score_1-score_2]
            else:
                d[team_1] = [d[team_1][0]+1,d[team_1][1]+score_1-score_2]

        if team_2 not in d:
            if score_2>score_1:
                d[team_2] = [3,score_2-score_1]
            elif score_2<score_1:
                d[team_2] = [0,score_2-score_1]
            else:
                d[team_2] = [1,score_2-score_1]
        else:
            if score_2>score_1:
                d[team_2] = [d[team_2][0]+3,d[team_2][1]+score_2-score_1]
            elif score_2<score_1:
                d[team_2] = [d[team_2][0]+0,d[team_2][1]+score_2-score_1]
            else:
                d[team_2] = [d[team_2][0]+1,d[team_2][1]+score_2-score_1]
    print(d)
    d = sorted( d.items(), key=lambda e: (e[1][0], e[1][1]), reverse=True )
    print(d)
    print(str(d[0][0]) + " " + str(d[1][0]))
