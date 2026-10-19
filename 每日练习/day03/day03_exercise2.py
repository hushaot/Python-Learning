# 第二题：计算偶数之和
n = int(input("请输入一个正整数:"))
total = 0
for i in range(1,n + 1):
    if i % 2 == 0:
        total = total + i
print(f"偶数之和为{total}")