def solution(r1, r2):
    count = {'R':0, 'W':0}
    l = len(r1)
    blank = 0
    replacements = 0
    for i in range(l):

        if r1[i] == '?' and r2[i] =='?':
            blank += 1
            continue

        if r1[i] == r2[i]:
            return -1

        if r1[i] + r2[i] == 'WR':
            count['W'] += 1
            count['R'] -= 1
            continue

        if r1[i] + r2[i] == 'RW':
            count['R'] += 1
            count['W'] -= 1
            continue

        if r1[i] == 'R' or r2[i] == 'W':
            count['R'] += 1
            count['W'] -= 1
        elif r1[i] == 'W' or r2[i] == 'R':
            count['W'] += 1
            count['R'] -= 1
        replacements += 1
    
    diff = abs(count['R']-count['W'])

    if diff > blank*2:
        return -1

    return replacements + diff

print(solution('?RW?WR', '?WR?RW')) # 0
print(solution('W?WR?','R??W?')) # 3
print(solution('R?R??','??W??')) # 5
print(solution('RRR??','WWW??')) # -1