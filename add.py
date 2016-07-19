# coding: utf-8
# 这个代码将替换文件中的指定字符，可以是空格( )，回车(\n)，或者TAB(\t)
# 可以 markdown 建造表格（添加|)

from_file = raw_input("读取文件名: ")
to_file = raw_input("写入文件名(如无此文件将于同目录下创建): ")
old_str = raw_input("被替换的字符: ")
new_str = raw_input("新字符: ")

f1 = open(from_file, 'r+')
f2 = open(to_file, 'w+')

first_or_not = raw_input("是否要在最头位置加入, 如不需要请输入n, 如需要请正常输入: ")
if first_or_not != "n":
	for s in f1.readlines():
		s = first_or_not + s
		f2.write(s.replace(old_str, new_str)) 
else:
	for s in f1.readlines():
		f2.write(s.replace(old_str, new_str)) 

print "写入完成"
	
f1.close()
f2.close()
	




