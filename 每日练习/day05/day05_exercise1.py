# 第一题：学生信息管理

student = {
    "name" : "小明",
    "major" : "电子科学与技术",
    "grade" : "研一",
    "score" : "92"
}

print("姓名:",student["name"])
print("专业:",student["major"])

student["score"] = 95
student["class"] = "一班"

print("修改后的学生信息:")
print(student)