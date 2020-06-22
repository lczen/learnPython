def grade_mode(list):
    list_set = set(list)
    frequency_dic = {}
    for i in list_set:
        frequency_dic[i] = list.count(i)
    grade_mode = []
    for key, value in frequency_dic.items():
        if value == max(frequency_dic.values()):
            grade_mode.append(key)
    return grade_mode

list = [0,1,2,3,4,5,5,5,6,6,6,7,9]

print(grade_mode(list))