'''
Created on Mar 30, 2020

@author: zen
'''

#if __name__ == '__main__':
RMB = [200, 100, 20, 10, 5, 1]
NUM = 6
X = 628
count = 0
for i in range(NUM):
    use = X // RMB[i]
    count += use
    X = X - RMB[i] * use
    print('需要面额为{} 的 {} 张'.format(RMB[i],use))
    print('剩余需要支付金额{}'.format(X))

print(count)