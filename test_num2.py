# coding: utf-8
# 这个代码用于检验 input 是否为数字(int)

def num_or_not(input):
	count = 0
	num = []

	for i in input:
		while count < 10:
			if i is not str(count):
				count += 1
			else:
				num.append(True)
				break	
		count = 0
			
	if len(num) == len(input):
		print "It is a number", int(input)
	else:
		print "it is not a number"
	
input = raw_input("> ")
num_or_not(input)

			