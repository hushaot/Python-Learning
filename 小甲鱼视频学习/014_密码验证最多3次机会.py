count = 3
password = "FishC"
while count > 0:
    pwd = input("请输入密码:")
    if pwd == password:
        print("密码正确！")
        break
    else:
        count -= 1
        print(f"密码错误，还剩{count}次机会")
else:
        print("机会用完，账号锁定！")
