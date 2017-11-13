#用递归的方式将10进制转换为2进制。

'''

1. 输入十进制 n
2。 将n除以2，得到倍数和余数。
3. 如果结果为1 或者0，则记录。如果倍数为1，则上进1位记录1；在本位上记录余数（0，1）
'''


n = 19
binarylist = []

def transfer(n):
    if n == 1:
        binarylist.insert(0,1)
        return
    lower_result = n//2
    lower_left = n%2

    binarylist.insert(0,lower_left)
    if lower_result == 1:
        binarylist.insert(0,1)
        return
    transfer(lower_result)

m = 22
transfer(m)
print(binarylist)