#二叉树定义
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#二叉树前序遍历，递归
def preorder(root):
    if root == None:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)

#二叉树前序遍历，非递归
def preorder_non_recursion(root):
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            print(node.val)
            stack.append(node.left)
            stack.append(node.right)

#二叉树中序遍历，递归
def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

#二叉树中序遍历，非递归
#中序遍历非递归
#idea:访问一个节点看是否为空，不为空加入队列，继续加入左孩子
#如果左孩子为空了，取出节点，打印节点，指向右孩子
def inorder_non_recursion(root):
    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            print(node.val)
            node = node.right


#二叉树后序遍历，递归
def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)

#后序遍历非递归
#这里是把遍历转成  左右根，
def postorder_non_recursion(root):
    stack1 = [root]
    stack2 = []
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    while stack2:
        print(stack2.pop().val)

#二叉树的层次遍历
# 这其实就是bfs
def levelorder(root):
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


