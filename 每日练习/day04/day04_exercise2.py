# 第二题：成绩统计程序

scores = [78,92,61,45,88,56,95]
average =sum(scores) / len(scores)

pass_count = 0
fail_count = 0
for score in scores:
    if score >= 60:
        pass_count += 1
    else:
        fail_count += 1

print("总人数:",len(scores))
print("平均分:",average)
print("最高分:",max(scores))
print("最低分:",min(scores))
print("及格人数:",pass_count)
print("不及格人数:",fail_count)