# 第三题：输出1 到n 之间能被3 和5 整除的整数

n = int(input("请输入正整数:"))
for i in range(1,n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
        
