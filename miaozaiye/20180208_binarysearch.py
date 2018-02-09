import sys


sys.path.insert(0,'/Users/Jane/Library/Python/3.5/lib/python/site-packages/')
from stdpackage import stdio
from stdpackage.instream import InStream

def _search(key,a,lo,hi):
    if hi <=lo:return -1
    mid = (lo+hi)//2
    if a[mid] > key:
        return _search(key,a,lo,mid)
    elif a[mid]<key:
        return _search(key,a ,mid+1,hi)
    else:
        return mid

def search(key,a):
    return _search(key,a,0,len(a))

def main():
    instream = InStream(sys.argv[1])
    a = instream.readAllStrings()
    while not stdio.isEmpty():
        key = stdio.readString()
        if search(key,a)<0:stdio.writeln(key)


main()
if __name__ == '__main__' :main()