# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution:
#     def nextLargerNodes(self, head: ListNode):
#         nums = []
#         node = head
#         while node != None :
#             nums.append(node.val)
#             node = node.next
#         stack = []
#         stack_loc = []
#         res = [0] * len(nums)
#
#         for i in range(len(nums)):
#             while stack and stack[-1] < nums[i]:
#                 res[stack_loc[-1]] = nums[i]
#                 stack.pop()
#                 stack_loc.pop()
#             stack.append(nums[i])
#             stack_loc.append(i)
#
#         return res
# print(Solution().nextLargerNodes(head=0))
# """遍历2，由于2是第一个数，直接入栈。2比一小吗？否，1入栈。1比5小吗？是。1的下一个大数是5.弹出1；2比5小吗，是，2的下一个最大值是5.弹出2.
# 栈空了。5入栈，5比7小吗，是，5的下一个最大数是7，弹出5，7入栈。7是最后一个元素。for循环结束。"""
# def max_next():
#     nums = [2, 1, 5 ,7]
#     stack = []
#     stack_loc = []
#     res = [0] * len(nums)
#     for i in range(len(nums)):
#         while stack and stack[-1] < nums[i]:
#             res[stack_loc[-1]] = nums[i]
#             stack.pop()
#             stack_loc.pop()
#         stack.append(nums[i])
#         stack_loc.append(i)
#     return res
# print(max_next())
print('需要面额为{} 的 {} 张'.format(20, 12))