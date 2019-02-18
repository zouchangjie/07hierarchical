# -*- encoding=utf-8 -*-
from hierarch import hcluster
from Clustering.HierarchicalClustering import getheight
from Clustering.HierarchicalClustering import getdepth
import numpy as np
import theano
import pylearn2
def drawdendrogram(clust,lables,jpeg='clusters.jpg'):
    #高度和宽度
    h=getheight(clust)*20
    w=1200
    depth=getdepth(clust)

    #由于宽度是固定的，对距离值做调整
    scaling=float(w-150)/depth

    #新建一个白色背景图片
    img=Image.new('RGB',(w,h),(255,255,255))
    draw=ImageDraw.Draw(img)

    draw.line((0,h/2,10,h/2),fill=(255,0,0))

    #画第一个节点
    drawnode(draw,clust,10,(h/2),scaling,lables)
    img.save(jpeg,'JPEG')

#对于每一个点进行作图
def drawnode(draw,clust,x,y,scaling,imlist,img):
    if clust.id<0:
        h1=gethight(clust.left)*20
        h2=gethight(clust.right)*20
        top=y-(h1+h2)/2
        bottom=y+(h1+h2)/2

        #线的长度
        ll=clust.distance*scaling

        #聚类到其子节点的垂直线
        draw.line((x,top+h1/2,x,bottom-h2/2),fill=(255,0,0))

        #链接左侧节点的水平线
        draw.line((x, top + h1 / 2, x+ll, top+ h1 / 2), fill=(255, 0, 0))

        # 链接右侧节点的水平线
        draw.line((x, bottom-h2 / 2, x + ll, bottom - h2 / 2), fill=(255, 0, 0))

        #递归绘制左右节点
        drawnode(draw,clust.left,x+ll,top+h1/2,scaling,imlist,img)
        drawnode(draw,clust.right,x+ll,bottom-h2/2,scaling,imlist,img)
    else:
        #绘制叶节点标签
        nodeis - Image.open(imlist(clust.id))
        nodeis.thumbnail((20,20))
        ns = nodeim.size
        print x,y,ns[1]//2
        print x+ns[0]
        print img.paste(nodeim,(int(x),int(y.ns[1]//2),int(x+ns[0]),int(y+ns[1]-ns[1]//2)))
imlist = []
folderPath = r''
for filename in os.listdi-(folderPath):
    if os.path.splitext(filename)[1]=='.jpg':
        i = list.append(os.path.join(folderPath,filename))
n = len(imlist)
print n

features = np.zeros(n,3)
for i in range(n):
    im = np.arrage(Image.open(imlist[i]))
    R = np.mean(im[;,;,0],flatten())
    G = np.mean(im[;,;,1],flatten())
    B = np.mean(im[;,;,2],flatten())
    features[i] = np.array([R,G,B])
tree = hcluster(features)
drawdendrogram(tree,imlist,jpeg=sunset.jpg)
