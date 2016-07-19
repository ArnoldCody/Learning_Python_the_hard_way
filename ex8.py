# coding: utf-8
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % ("我", "是", "中", "文")
print "这行字会出现代码, 不要用%r, 要用%s来正常打印"
print "%s %s %s %s" % ("我", "是", "中", "文")
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnighht."
)