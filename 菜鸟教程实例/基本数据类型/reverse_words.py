def reverseWords(input):

    # 通过空格将字符串分隔，把各个单词分隔为列表
    inputWords = input.split(" ")

    # inputWords[-1::-1]三个参数说明：
    # 第一个参数 -1 表示从最后一个元素开始
    # 第二个元素为空，表示移动到列表开头
    # 第三个元素 -1 表示逆向步进 （每次向左移动一个位置）
    inputWords = inputWords[-1::-1]

    # 重新用空格拼接单词
    output = ' '.join(inputWords)

    return output

if __name__ == "__main__":
    input = 'I like runoob'
    rw = reverseWords(input)
    print(rw)