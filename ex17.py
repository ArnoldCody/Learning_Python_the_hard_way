from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Coping from %s to %s" % (from_file, to_file)

# we could do these two on one line, hows
# in_file = open(from_file)
# indate = in_file.read
indate = open(from_file).read()

print "The input file is %d bytes long" % len(indate)

print "Does the output file exist? %r?" % exists(to_file)
print "Ready, hit return to continue, CTRL-C to abort."
raw_input()

# out_file = open(to_file, 'w')
# out_file.write(indata)
open(to_file, 'w').write(indate)

print "Alright, all done."

# out_file.close()
# in_flie.close()