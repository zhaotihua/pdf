import PyPDF2
import os
#from textmark import create_watermark
from fileoperation.labeladdnumber.textmark import create_watermark

def addwatermarrk(pdfname,output_pdf,n,content):
#打开PDF文件
    with open(pdfname,'rb') as pdffile:
    #读取文件到对象里
        PdfReader = PyPDF2.PdfFileReader(pdffile)
    #读取一页到第一页对象里
        minutesFirstPage = PdfReader.getPage(n)
        #判断页面方向
#input1 = PdfFileReader(open('example.pdf', 'rb'))
        RectangleObject = minutesFirstPage.mediaBox
#RectangleObject([0, 0, 612, 792])

    
    #对比高宽值进行判断
        if (RectangleObject[2] > RectangleObject[3]):
            y = 2
            degree = 90
        else:
            y = 11
            degree = 0
        create_watermark(content,y,degree)


    #打开水印PDF文件
        with open('mark1.pdf','rb') as markfile:
        #读取文件到对象里
            pdfwatermarkreader = PyPDF2.PdfFileReader(markfile)
        #合并水印PDF对象到原PDF对象里
            minutesFirstPage.mergePage(pdfwatermarkreader.getPage(0))
        #建个写的对象
            pdfwriter = PyPDF2.PdfFileWriter()
        #将合并的对象写到新对象里
            pdfwriter.addPage(minutesFirstPage)
            if not os.path.exists("finish"):
                os.makedirs("finish")

        #建一个新的PDF文件，将合并后的对象写到文件里
            with open("finish/" + output_pdf,'wb') as resultpdffile:
                pdfwriter.write(resultpdffile)
            #pdf_writer = PdfFileWriter()
            #pdfOutputFile = open(output_pdf,'wb')
            #pdf_writer.write(pdfOutputFile)
            #pdfOutputFile.close()

