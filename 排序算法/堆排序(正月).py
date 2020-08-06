'''
parent = (i-1)/2
c1 = 2i+1
c2 = 2i+2
'''
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
def heapify(tree, n, i):
    if i >= n:
        return
    c1 = 2 * i + 1
    c2 = 2 * i + 2
    max = i
    if c1 < n and tree[c1] > tree[max]:
        max = c1
    if c2 < n and tree[c2] > tree[max]:
        max = c2
    if max != i:
        swap(tree, max, i)
        heapify(tree, n, max)
def build_heap(tree, n):
    last_node = n-1
    parent = int((last_node-1)/2)
    for i in range(parent, -1, -1):
        heapify(tree, n, i)
def heap_sort(tree, n):
    build_heap(tree, n)
    for i in range(n-1, -1, -1):
        swap(tree, i, 0)
        heapify(tree, i, 0)
#tree = [4, 10, 3, 5, 1, 2]
tree = [2, 5, 3, 1, 10, 4]
n = 6
#build_heap(tree, n)
heap_sort(tree, n)
print(tree)
"""
我有提到过一个前提：对一个节点做heapify的时候，必须保证它的所有子树都已经是堆。
所以，在这个前提下，如果要做heapify的节点已经符合“父节点 > 子节点”的性质，那么这就已经是一个堆了；就没有必要往下走了。
另外，我们的build_heap函数是从最后一个不是叶节点的点开始往前做heapify操作的，所以最后是可以形成一个堆。
"""