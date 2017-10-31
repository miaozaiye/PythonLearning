#从命令行获取整数m, 从标准输入获取最近m个浮点数，并用动画展示出来

from stdpackage import stdarray,stddraw,stdio,stdstats
import sys

m = int(sys.argv[1])
list =[]

stddraw.setCanvasSize(500,500)
stddraw.setYscale(-1,1)
for i in range(m):

    stddraw.clear()
    list.append([stdio.readFloat(),str(i)])
    print(list)
    stdstats.plotBars(list,text = True)
    stddraw.show(200)

stddraw.show()
