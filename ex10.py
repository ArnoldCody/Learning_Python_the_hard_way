# coding: utf-8
# 那是什么?
# 将单引号和双引号转义
# 方法一: 
# 使用反斜杠 \ (back-slash)可以将难以打印的字符放到字符串.这就叫做"转义序列"(escape sequences)
# 例如 \\ = \
# example
print "I am 6'2\" tall." # 将双引号转义
print 'I am 6\'2" tall.' # 将单引号转义

# 方法二:
# 使用"三引号(triple-quotas)", """
print '"' * 3

# 例如
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat"

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "a\nb" 
# 打印出来为:
# a
# b
print "a\rb"
# 打印出来为: 
# b
print "abcdefg\rhigk"
# 打印出来为:
# rhigkfg
print "\a"

print "这是一个小代码,看看打印出来是什么"
print """
While True:
\tfor i in ["/", "-", "|", "\\", "\"]:\n\t\tprint "%s\\r" % i
"""
while True:
	for i in ["/", "-", "|", "\\", "|"]:
		print "%s\n" % i,