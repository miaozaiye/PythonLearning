import sys
from stdpackage import stdio
from stdpackage.color import Color

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

def main():
    r1 = int(sys.argv[1])
    g1 = int(sys.argv[2])
    b1 = int(sys.argv[3])
    r2 = int(sys.argv[4])
    g2 = int(sys.argv[5])
    b2 = int(sys.argv[6])
    c1 = Color(r1,g1,b1)
    c2 = Color(r2,g2,b2)

    stdio.writeln(areCompatible(c1,c2))

if __name__ =='__main__':main()
