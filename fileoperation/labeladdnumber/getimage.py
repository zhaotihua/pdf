
import sys, fitz
import os
#import datetime
 
def pyMuPDF2_fitz(pdfPath, imagePath):
    pdfDoc = fitz.open(pdfPath) # open document
    for pg in range(pdfDoc.pageCount): # iterate through the pages
        page = pdfDoc[pg]
        rotate = int(0)
        # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像
        # 此处若是不做设置，默认图片大小为：792X612, dpi=96
        #zoom_x = 1.33333333 #(1.33333333-->1056x816)   (2-->1584x1224)
        #zoom_y = 1.33333333
        zoom_x = 2 #(1.33333333-->1056x816)   (2-->1584x1224)
        zoom_y = 2
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate) # 缩放系数1.3在每个维度  .preRotate(rotate)是执行一个旋转
        rect = page.rect                         # 页面大小
        mp = rect.tl + (rect.bl - (0,330/zoom_x)) # 矩形区域    56=75/1.3333
        clip = fitz.Rect(mp, rect.br)            # 想要截取的区域
        pix = page.getPixmap(matrix=mat, alpha=False, clip=clip) # 将页面转换为图像
        if not os.path.exists(imagePath):
            os.makedirs(imagePath)
        print (pix)
        pix.writePNG(imagePath + '/' + 'psReport_%s.png' % pg)# store image as a PNG
 

