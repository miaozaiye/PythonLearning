import sys
from stdpackage import stdio

# from miaozaiye.redirection import __redirection__
def main():

    # r_obj = __redirection__()
    # sys.stdout = r_obj
    n = int(sys.argv[1])
    total = 0
    for i in range(n):
        total +=stdio.readInt()
    stdio.writeln('in {0} sum is'.format(sys.argv[0]) + str(total))
    # r_obj.to_console()
    # r_obj.to_file('test.log')



main()