f1 = open('../笔记.txt', 'r', encoding='utf8')
f2 = open('../笔记副本.txt', 'w', encoding='utf8')

content1 = f1.read()
f2.write(content1)

f1.close()
f2.close()
