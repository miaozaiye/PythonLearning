from stdpackage import stddraw

stddraw.setXscale(-1.0,1.0)
stddraw.setYscale(-1.0,1.0)

DT = 20
RADIUS = 0.1
r1x = 0.480
r1y = 0.860
v1x = 0.015
v1y = 0.023
position1 = [(r1x,r1y)]
r2x = 0.080
r2y = -0.360
v2x = 0.03
v2y = 0.02
position2 = [(r2x,r2y)]
changepoint = []
while True:
    if (abs(r1x+v1x-r2x-v2x)<2*RADIUS and abs(r1y+v1y-r2y-v2y)<2*RADIUS):

        print(r1x,v1x,r2x,v2x,'change')
        a = v1x
        v1x = v2x
        v2x = a
        changepoint.append((r1x,r1y,r2x,r2y))
        # stddraw.line(r1x,r1y,r2x,r2y)
        # stddraw.show()
        a = v1y
        v1y = v2y
        v2y = a
        # break
    if abs(r1x+v1x)+RADIUS>1.0: v1x = -v1x
    if abs(r1y + v1y)+RADIUS >1.0:v1y = -v1y
    if abs(r2x+v2x)+RADIUS>1.0: v2x = -v2x
    if abs(r2y + v2y)+RADIUS >1.0:v2y = -v2y
    r1x = r1x+v1x
    r1y = r1y + v1y
    r2x = r2x+v2x
    r2y = r2y + v2y

    position1.append((r1x,r1y))

    stddraw.clear(stddraw.LIGHT_GRAY)

    stddraw.setPenColor(stddraw.GRAY)
    for x,y in position1[-50:]:
        print(x,y)
        stddraw.circle(x,y,RADIUS)
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.filledCircle(r1x,r1y,RADIUS)
    stddraw.filledCircle(r2x,r2y,RADIUS)
    stddraw.show(DT)
