s = "abccaddbeffe"
zidian = {c : i for i, c in enumerate(s)}
print(zidian)
ans = []
start = 0
end = 0
for i, c in enumerate(s):
    end = max(end, zidian[c])
    #end = zidian[c] 为什么不是这个，原因是每出现一个新的字母，最大位置可能都会发生改变。
    # 比如abccaddbeffe，zidain[a]=4,如果你到4了，就可以截取了。但是在到四之前出现了新的zidian[b]=7这是一个扩展的过程
    if i == end:
        ans.append(end-start+1)
        start = i + 1
print(ans)
