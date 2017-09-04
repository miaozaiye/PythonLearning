import sys
from stdpackage import stdio


def main():
    n = int(sys.argv[1])
    total = 0
    for i in range(n):
        total +=stdio.readInt()
    stdio.writeln('sum is' + str(total))


main()