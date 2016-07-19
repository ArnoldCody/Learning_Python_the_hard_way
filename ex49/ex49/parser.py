# coding: utf:8
# 以下代码为 ex48 的进一步拓展，将 lexicon.py 产生的列表转化成一个 sentence 类

# 从处理异常情况开始
class ParserError(Exception):
	pass
	
# 创建 sentence 类
class Sentence(object):
	def __init__(self, subject, verb, object):
		self.subject = subject[1]
		self.verb = verb[1]
		self.object = object[1]
		
# 用 peek 看到列表中的单词，并返回单词的类（’type‘）		
def peek(word_list):
	if word_list:
		word = word_list[0]
		return word[0]
	else:
		return None
		
# 用 match 处理列表中单词，如单词的类符合预期，那么，返回该元组（‘type’， ‘word'），同时在单词列表中
# 去除该元组
def match(word_list, expecting):
	word = word_list.pop(0)
	
# 访问列表用［］，不是（）
	if word[0] == expecting:
		return word
	else:
		return None	
		
# 用 skip 来过滤掉我们不关心的单词（prep）
def skip(word_list, word_type):
	while peek(word_list) == word_type:
		match(word_list, word_type)
		
# 解析动词部分，跳过 prep 词。获得列表里的第一个元组，如果是动词，那么将此元组从列表里剔除。
def parse_verb(word_list):
	skip(word_list, 'prep')
	
	if peek(word_list) == 'verb':
		return match(word_list, 'verb')
	else:
		raise ParserError("Expected a verb next")
	
# 跳过 prep 词。获得列表里的第一个元组，如果是object, 或direction，那么将此元组从列表里剔除。
def parse_object(word_list):
	skip(word_list, 'prep')
	next_word = peek(word_list)
	
	if next_word == 'noun':
		return match(word_list, 'noun')
	elif next_word == 'direction':
		return match(next_word, 'direction')	
	else:
		raise ParserError("Expected a object or direction next")
		
# 用 peek 处理主语
def parse_subject(word_list):
	skip(word_list, 'prep')
	next_word = peek(word_list)
	
	if next_word == 'noun':
		return match(word_list, 'noun')
	elif next_word == 'verb':
		return ('noun', 'player')
	else:
		raise ParserError("Expected a verb next")	

# 最后一个函数
def parse_sentence(word_list):
	sub = parse_subject(word_list)
	verb = parse_verb(word_list)
	obj = parse_object(word_list)
	print sub
	print verb
	print obj
	return Sentence(sub, verb, obj)

	
start = parse_sentence([('noun', 'I'), ('prep', 'very'), ('verb', 'love'), ('noun', 'you')])

		




		