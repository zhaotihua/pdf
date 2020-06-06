
#encoding=utf-8
#author: walker
#date: 2014-03-17
#function: 创建文字水印pdf



from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
def create_watermark(content,y,degree):
    #默认大小为21cm*29.7cm
    c = canvas.Canvas("mark1.pdf", pagesize = (10*cm, 15*cm))
    #移动坐标原点(坐标系左下为(0,0))
    c.translate(4*cm, y*cm)
 
    #设置字体
    c.setFont("Helvetica", 20)
    #指定描边的颜色
    c.setStrokeColorRGB(0, 0, 1)
    #指定填充颜色
    c.setFillColorRGB(0, 1, 0)
    #画一个矩形
    #c.rect(cm, cm, 7*cm, 17*cm, fill=1)
 
    #旋转45度,坐标系被旋转
    c.rotate(degree)
    #指定填充颜色
    c.setFillColorRGB(0.6, 0, 0)
    #设置透明度,1为不透明
    c.setFillAlpha(0.5)
    #画几个文本,注意坐标系旋转的影响
    c.drawString(1*cm, 0*cm, content)
    #c.setFillAlpha(0.6)
    #c.drawString(4*cm, 2*cm, content)
    #c.setFillAlpha(1)
    #c.drawString(6*cm, 4*cm, content)
 
    #关闭并保存pdf文件
    c.save()
#create_watermark("A03568h",2,90)
