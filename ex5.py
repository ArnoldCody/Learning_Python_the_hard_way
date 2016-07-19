# coding: utf-8
# 更多的变量和打印
my_name = 'Arnold Y.'
my_age = 35
my_height = 190 # cm
my_weight = 90 # kg
my_eyes = 'Black'
my_teeth = 'white'
my_hair = 'black'

print "Let's talk about %s." % my_name
print "He's %d cm tall." % my_height
print "He's %d kg heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hari." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is triky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." %(my_age, my_height, my_weight, my_age + my_height + my_weight)