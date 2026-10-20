# 第一题：列表基本操作

numbers = [10,20,30,40,50]

print("原始列表:",numbers)
print("第一个元素:",numbers[0])
print("最后一个元素:",numbers[-1])

numbers[1] = 25
print("修改后:",numbers)

numbers.append(60)
print("添加后:",numbers)

numbers.remove(30)
print("删除后:",numbers)

print("列表长度:",len(numbers))