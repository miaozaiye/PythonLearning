#命令行输入字符串，由左向右漂移，飘到触碰到最右边边界，则重新从左边开始。
from stdpackage import stddraw

s= 'this is a sentence'

x = 0.0
y = 0.9

stddraw.setFontSize(35)
stddraw.setPenColor(stddraw.BOOK_RED)

while True:

    stddraw.clear()
    if x<1:
        stddraw.text(x,y,s)
        stddraw.show(100.0)
        x +=0.1
    else:
        x = 0.0
