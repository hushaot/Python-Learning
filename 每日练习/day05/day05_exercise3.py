# 第三题：成绩报告

scores = [78, 92, 61, 45, 88, 56, 95]
average = sum(scores) / len(scores)
highest = max(scores)
lowest = min(scores)

print("==== 成绩统计报告 ====")
print(f"本次统计共有{len(scores)}个学生")
print(f"平均分为{average:.2f}分")
print(f"最高分为{highest}分")
print(f"最低分为{lowest}分")