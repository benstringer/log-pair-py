
#
# log-pair.py - process a logfile looking for BEGIN/END pairs and correlate, reporting timestamp intervals
#

import sys

#debug = 0
debug = 1

# Check for args

if len(sys.argv) < 3:
   sys.exit('Usage: %s file1 file2' % sys.argv[0])

if debug:
   print "File1 : ", sys.argv[1]
   print "File2 : ", sys.argv[2]

# Open the input files

file1 = open(sys.argv[1], 'r')
file2 = open(sys.argv[2], 'r')

# Read input into dict

# 

