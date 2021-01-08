import sys
from math import sqrt

line1 = int(sys.argv[1])
line2 = int(sys.argv[2])
line3 = sqrt(line1**2 + line2**2)

print("斜辺の長さは{:.0f}です".format(line3))
