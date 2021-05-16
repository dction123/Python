# 这是一个单行注释
"""
这是一个多行注释1
"""
"""
多行注释2
"""
if True:
    print("真")
    print("zhen2")  # 缩进必须保持一致
else:
    print("假")
# 多行语句
item_one = "this"
item_two = "is"
item_three = "pig"
total = item_one + \
        item_two + \
        item_three
print(r"这是一行字 \n")  # r 取消 \ 的转译

"""字符串"""
name = "梁小明"
split_name = name[1:3:1]  # 字符串截取
print(split_name)


name2 = "abcdefg"
print(name2[0:-1])  # 输出第一个到倒数第二个字
print('\n')  # 输出空行
print(r"\n")  # 输出转义字符
print(name2[3:])
