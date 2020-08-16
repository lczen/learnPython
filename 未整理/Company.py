class Company:
    companyNum = 0
    companyList = []
    def __init__(self,companyName,desc):
        self.companyName = companyName
        self.desc = desc
        self.employeeList = []

        Company.companyNum += 1
        Company.companyList.append(companyName)

    def recruit(self,name,age,cost):
        self.employeeList.append([[name,age,cost]])
    def dismiss(self,name):
        for item in self.employeeList:
            if item[0] == name:
                self.employeeList.remove(item)

    def ggetEmployeeList(self):
        return self.CompanyNameList

#功能验证
c0 = Company('小象学院','大数据AI在线教育')
c0.recruit('HanXiaoyang',18, cost=20000)
c0.recruit('Eric',20, cost=10000)
print('{}公司员工详细信息列表:{}'.format(c0.companyName,c0.getEmployeeList()))

c0.dismiss('Eric')

c0.adPromotion(5000)
c0.payInsurance()
c0.payTax()
c0.sale(50,100)
print('{}公司员工详细信息列表:{}'.format(c0.companyName,c0.getEmployeeList()))
print('{}公司当前利润：{}'.format(c0.companyName,c0.getProfit()))

c1 = Company('百度','搜索引擎')
c1.recruit('liyanhong',30, cost=50000)
c1.recruit('likaifu',50, cost=40000)
print('{}公司员工详细信息列表:{}'.format(c1.companyName,c1.getEmployeeList()))

print('公司名列表：',Company.companyList)
print('公司总个数：',Company.companyNum)