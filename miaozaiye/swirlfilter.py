#旋风滤镜，将目标图片从原点到边缘，按照渐进增大的角度进行旋转
'''
1。 命令行输入图片文件名，以及最大角度
2。 根据长宽，生成新的图片对象
3。 读取当前图片每个像素，并在新图片对象对应转角的位置储存
4。 展示图片


'''


import sys,pygame,PIL
from stdpackage import picture,stddraw
from stdpackage.picture import Picture
from stdpackage.color import Color
import math

def swirl(col,row,theta):
    '''

    :param col:
    :param row:
    :return: 经过旋转后的坐标
    '''


    newcol = col+1
    newrow = row+1

    return newcol,newrow

def getangle(col,row):
    '''

    :param col:
    :param row:
    :return: 对应
    '''

    alpha = 0

    return alpha

def getratio(col,row,alpha):
    ratio = 0
    return ratio


def get_length(alpha,img):
    length = 0
    return  length

def main(filename,theta):
    #通过命令行输入图片地址，以及最大角度
    img = picture(filename)
    width = img.width()
    height = img.height()
    new_img = picture(width,height)


    #用极坐标来重新画图
    for alpha in range(2*math.pi):  #遍历从 0 到360度
        length = get_length(alpha) # 获取该图片在该角度下，极坐标对应的轴长
        for r in range(length):
            col = r*math.cos(alpha)
            row = r*math.sin(alpha)
            pix = img.get(col,row)
            beta = r/length * theta
            new_col,new_row = swirl(col,row,beta)
            new_img.set(new_col,new_row,pix)


    # for col in range(width):
    #     for row in range(height):
    #
    #         alpha = getangle(col,row) #获取该位置所对应的角度
    #         ratio = getratio(col,row,alpha) #获取该位置所对应的角度变化比例
    #         beta = theta*ratio #应该旋转的角度
    #         pix = img.get(col,row) #原始图片该位置的像素值
    #
    #         new_col,new_row = swirl(col,row,beta) #给新图片该位置对应旋转后新位置
    #         new_img.set(new_col,new_row,pix) #给新图片新位置赋上像素值

    stddraw.picture(new_img) #画出新图片
    stddraw.show() #展示新图片

main()