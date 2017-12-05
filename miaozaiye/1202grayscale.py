import sys
from stdpackage import stddraw,stdio
from stdpackage.color import Color
from stdpackage.picture import Picture


def luminance(c):
    red = c.getRed()
    green = c.getGreen()
    blue = c.getBlue()

    return .299*red + .587*green + .144*blue

def toGray(c):
    y = int(round(luminance(c)))
    return Color(y,y,y)

def areCompatible(c1,c2):
    return abs(luminance(c1) - luminance(c2))>=128.0


pic = Picture(sys.argv[1])
for col in range(pic.width()):
    for row in range(pic.height()):
        pixcel = pic.get(col,row)
        gray = toGray(pixcel)
        pic.set(col,row,gray)

stddraw.setCanvasSize(pic.width(),pic.height())
stddraw.picture(pic)
stddraw.show()