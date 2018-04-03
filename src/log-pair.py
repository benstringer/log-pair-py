
#
# log-pair.py - process a logfile looking for BEGIN/END pairs and correlate, reporting timestamp intervals
#

import sys

# Check for args

if len(sys.argv) < 3:
   sys.exit('Usage: %s file1 file2' % sys.argv[0])

print "File1 : ", sys.argv[1]
print "File2 : ", sys.argv[2]

