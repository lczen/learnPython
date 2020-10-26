#方法一所有可能出现的情况括号
def generate(item,n,result):
    if len(item)==2*n:
        result.append(item)
        return
    generate(item+'(',n,result)
    generate(item+')',n,result)

# 方法一所有可能出现的情况括号
def all_brackets():
    result = []
    generate("",2,result)
    print(result)

#方法二合法的括号
def generateParenthesis(n):
    result = []
    generate("",n,n,result)
    return result
def generate(item,left,right,result):
    if left == 0 and right == 0:
        result.append(item)
        return
    if left>0:
        generate(item+'(',left-1,right,result);
    if left<right:
        generate(item + ')', left, right-1, result);
print(generateParenthesis(2))