import csv
with open('WorldCupMatches.csv','r',encoding='UTF-8') as f:
    reader = csv.DictReader(f)
    home_team_goals = []
    away_team_goals = []
    for row in reader :
        home_team_goals.append(int(row['Home Team Goals']))
        away_team_goals.append(int(row['Away Team Goals']))
#print(home_team_goals,away_team_goals)

def quartile_value(list,num):
    list.sort()
    location = num*(len(list)+1)/4
    location_int = int(location)
    quartile = list[location_int-1]*(location_int+1-location) + list[location_int] * (location - location_int)
    return quartile
Q1 = quartile_value(home_team_goals,1)
Q2 = quartile_value(home_team_goals,2)
Q3 = quartile_value(home_team_goals,3)

print(Q1)
print(Q2)
print(Q3)

mean = sum(home_team_goals)/len(home_team_goals)
print(mean)

IQR = Q3 - Q1

#内限
inner_outlier_low = Q1 - 1.5*IQR
inner_outlier_high = Q3 +1.5*IQR
#外限
outer_outlier_low = Q1 - 3*IQR
outer_outlier_high = Q3 + 3*IQR

for score in home_team_goals:
    if outer_outlier_low < score <inner_outlier_low or inner_outlier_high < score < outer_outlier_high:
        print(score)
for score in home_team_goals:
    if score <outer_outlier_low or score > outer_outlier_high:
        print(score)
print('第一四分位数：{}'.format(Q1))
print('第二四分位数：{}'.format(Q2))
print('第三四分位数：{}'.format(Q3))
print('均值：{}'.format(mean))
print('内限：{}和{}'.format(inner_outlier_low,inner_outlier_high))
print('外限：{}和{}'.format(outer_outlier_low,outer_outlier_high))

from matplotlib import pyplot as plt
plt.boxplot(home_team_goals,labels=['Home Teams'])
plt.title('Goals for Home Teams in all FIFA World Cups')
plt.show()

plt.boxplot((home_team_goals,away_team_goals),labels= ['Home Teams','Away Teams'])
plt.title('Goals for Home Teams and Away Teams in all FIFA World Cups')
plt.show()