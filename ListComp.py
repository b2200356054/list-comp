import sys
repeat = 21
stars = ["*"*(x*2-1) for x in range(0,repeat+1)]
reversestars = ["*"*(2*x-1) for x in range(repeat,0, -1)]
[print(" "*(repeat-x), stars[x], " "*(repeat-x),"\n", end="") for x in range(0,repeat)]
[print(" "*(repeat-x), stars[x], " "*(repeat-x),"\n", end="") for x in range(repeat,-1, -1)]