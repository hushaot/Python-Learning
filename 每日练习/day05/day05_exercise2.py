# 第二题：字符串转数字列表

text = input("请输入多个数字，用空格分隔：")
parts = text.split()
numbers = []

for part in parts:
    number =float(part)
    numbers.append(number)

print("数字列表:",numbers)
print("数据个数:",len(numbers))
print("平均值:",sum(numbers) / len(numbers))
print("最大值:",max(numbers))
print("最小值:",min(numbers))