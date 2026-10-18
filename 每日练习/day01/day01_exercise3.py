# 第三题：电功率计算器

# 接收用户输入的电压和电流
voltage = float(input("请输入电压 (V): "))
current = float(input("请输入电流 (A): "))

# 计算电功率
power = voltage * current

# 输出结果
print("\n==== 电功率计算结果 ====")
print(f"电压: {voltage} V")
print(f"电流: {current} A")
print(f"电功率: {power} W")
