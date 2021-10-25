# 1 打开文件
file = open(r"../笔记.txt", encoding='utf8')

# 2 读写文件
content = file.read()
print(content)

# 3 关闭文件
file.close()