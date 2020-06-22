# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def add_to_vector(head, vector):
    if not head:
        return
    vector.append(head.val)
    add_to_vector(head.next, vector)

a = ListNode(4)
b = ListNode(2)
c = ListNode(1)
a.next = b
b.next = c
vector = []
add_to_vector(a, vector)
print(vector)


#使用循环把[1,2,3]中的[1],[1,2],[1,2,3]放入列表中
# nums = [1,2,3]
#
# result = []
# item = []
# for i in range(0,len(nums)):
#     item.append(nums[i])
#     new_item = []##python里面的指针与赋值操作
#     new_item = item[0:]
#     result.append(new_item)
# print(result)

#使用递归把[1,2,3]中的[1],[1,2],[1,2,3]放入列表中
def generate(i, nums, item, result):
    if i>=len(nums):
        return
    item.append(nums[i])
    result.append(item[0:])#只加入值
    generate(i+1,nums,item,result)
result = []
item = []
generate(0,[1,2,3],item,result)
print(result)
