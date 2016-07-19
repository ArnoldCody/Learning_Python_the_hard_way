# coding: utf-8

ten_things = "Apple Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ') # 创建 stuff 列表, 将 ten_things 中的字符串用"空格"隔开, 并加入此列表
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop() # 删除 more_stuff 列表中的最后一项, 并返回该项
	print "Adding: ", next_one 
	stuff.append(next_one) # 在 stuff 列表中加入 next_one 返回的项目
	print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]  
print stuff[-1] 
print stuff.pop()
print ' '.join(stuff) # 用"空格"将列表 stuff 中的元素连接成一个字符串
print '#'.join(stuff[3:5]) # 与上同理
