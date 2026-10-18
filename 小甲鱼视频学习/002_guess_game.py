secret = 8
guess = int(input("猜猜小甲鱼现在心里想的是哪个数字:"))

if guess == secret:
    print("你猜的太准了！")
    print("猜对了也没有奖励！")
else:
    if guess > secret:
        print("哥，大了大了~~~")
    else:
        print("嘿嘿，小了~~~")
