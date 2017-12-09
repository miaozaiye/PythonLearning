#从命令行读取2个或者更多图片文件名，然后用淡入淡出的方式来展示

'''
1. get list of filename from sys.argv[1:]
2. while not end, use fade(a,b) to show slide
3. fade(a,b), transfer a to b via n steps, and for i step, the pixel shows the value of average(a+b)
'''

import sys,pygame,PIL
from stdpackage import picture,stddraw
from stdpackage.picture import Picture
from stdpackage.color import Color

def blend(c1,c2,alpha):
    r = (1-alpha)*c1.getRed()+alpha*c2.getRed()
    g = (1-alpha)*c1.getGreen()+alpha*c2.getGreen()
    b = (1-alpha)*c1.getBlue()+alpha*c2.getBlue()
    return Color(int(r),int(g),int(b))

def fade(file1,file2):
    print('can support extension:', pygame.image.get_extended())
    source = Picture(file1)
    target = Picture(file2)

    n = 5

    width =source.width()
    height =source.height()

    stddraw.setCanvasSize(width,height)
    pic = Picture(width,height)

    for t in range(n+1):
        for col in range(width):
            for row in range(height):
                c0 = source.get(col,row)
                cn = target.get(col,row)
                alpha = 1.0*t/n
                pic.set(col,row,blend(c0,cn,alpha))
        stddraw.picture(pic)
        stddraw.show(2)
    stddraw.show()



fade('1.bmp','2.bmp')

# def main():
#     filelist = sys.argv[1:]
#
#     for i in range(len(filelist)):
#         if i<len(filelist)-1:
#             fade(fade(filelist[i],filelist[i+1]))
#         else:
#             pass
