def last_weight_stone(stone):
    if len(stone)==1:
        return stone[0]
    stone.sort()

    while stone[-2]!=0:
        if stone[-1] == stone[-2]:
            stone[-1] = 0
            stone[-2] = 0
        else:
            stone[-1] = stone[-1] - stone[-2]
            stone[-2] = 0
        stone.sort()
    return stone[-1]