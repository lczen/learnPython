weight = float(input('请输入您的体重：'))
high = float(input('请输入您的身高：'))
# 完成BMI计算并返回结果提示信息
# your code here
BMI = weight/(high*high)
print(BMI)
if BMI < 18 :
    print('偏瘦')
elif 18<= BMI <25:
    print('标准')
else:
    print('超重')