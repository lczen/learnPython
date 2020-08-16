import csv

# dadas = [['name','age'],
#          ['张三', 29],
#          ['李四',43],
#          ['王五','18']]
#
# with open('test.csv','w',newline='') as f:
#     writer = csv.writer(f)
#     for row in dadas:
#         writer.writerow(row)

headers = ['name','age']

datas = [{'name':'张三','age':29},
         {'name': '李四', 'age': 43},
         {'name': '王五', 'age': 18}
         ]
with open('test.csv','w',newline='') as f:
    writer = csv.DictWriter(f, headers)
    writer.writeheader()
    writer.writerows(datas)