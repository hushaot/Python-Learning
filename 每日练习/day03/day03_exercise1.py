# 第一题：计算 1 到 n 的总和
n = int(input("请输入一个正整数:"))
total = 0
for i in range(1,n + 1):
    total = total + i
print(f"累加和为{total}")