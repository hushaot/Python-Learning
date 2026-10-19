# 第一题：两数计算器

a = float(input("请输入第一个数字:"))
b = float(input("请输入第二个数字:"))

print("加法结果:", a + b)
print("减法结果:", a - b)
print("乘法结果:", a * b)

if b != 0:
    print("除法结果:", a / b)
else:
    print("除数不能为 0,无法进行除法运算")

print("a 的 b 次方结果:", a ** b)