class Solution:
    def restoreIpAddresses(self,s):
        ret = []
        ip = []
        for a in range(1,4):
            for b in range(1, 4):
                for c in range(1, 4):
                    for d in range(1, 4):
                        if a + b + c + d == len(s):
                            n1 = int(s[0:a])
                            n2 = int(s[a:a+b])
                            n3 = int(s[a+b:a+b+c])
                            n4 = int(s[a+b+c:])
                            if n1 <= 255 and n2 <= 255 and n3 <= 255 and n4 <= 255:
                                ip.append(str(n1))
                                ip.append('.')
                                ip.append(str(n2))
                                ip.append('.')
                                ip.append(str(n3))
                                ip.append('.')
                                ip.append(str(n4))
                                vip = "".join(ip)
                                if len(vip) == len(s) + 3:
                                    ret.append(vip)
                                ip.clear()


        return ret
print(Solution().restoreIpAddresses("25525511135"))