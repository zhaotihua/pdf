


from fileoperation.labeladdnumber.getimage import pyMuPDF2_fitz
from fileoperation.labeladdnumber.readtiaoxingma import decode
from fileoperation.labeladdnumber.excelline1 import readExceline1
from fileoperation.labeladdnumber.excelline2 import readExceline2
from fileoperation.labeladdnumber.excelline3 import readExceline3
from fileoperation.labeladdnumber.textmark import create_watermark
from fileoperation.labeladdnumber.addwatermarrk import addwatermarrk
from fileoperation.labeladdnumber.addwatermarrk import addwatermarrk
from fileoperation.labeladdnumber.zipfiles import zipfiles



import zipfile


import os

from pyzbar import pyzbar
#转换图片

def main1 (pdfname,excelfilename,imagePath,output_path):
    #pdfname = 'WF0428.pdf'
    #imagePath = 'image1'
    #pyMuPDF_fitz(pdfPath, imagePath)#只是转换图片
    pyMuPDF2_fitz(pdfname, imagePath)
    
    
    #进行解码
    list4 = []
    #path = 'image1'
    for i in range(len([lists for lists in os.listdir(imagePath) if os.path.isfile(os.path.join(imagePath, lists))])):
        f = "psReport_" + str(i) + ".png"
        e = imagePath + "/" + f
        print (f)
        print (e)
        #image = cv2.imread('psReport_0.png')
        image = cv2.imread(e)
        # 找到图像中的条形码并进行解码
        barcodes = pyzbar.decode(image)
        decode(image,barcodes)
        list4.append(decode(image, barcodes))
        print (list4)
    d= list4
    #找对应产品号
    print (d)
    #excelfilename = 'lnc.xlsx'
    a = readExceline1(excelfilename)
    b = readExceline2(excelfilename)
    c = readExceline3(excelfilename)


  

    n=-1
    for i in d:
        print (i)
        n=n+1
        if i in c:
            q = c.index(i)
            print (q)
            f = a[q] + "X" + str(b[q])
            #create_watermark(f)
            j=a[q] + "-" + str(n) + ".pdf"
            addwatermarrk(pdfname,j,n,f)
        else:
            f = "wrong"
            #create_watermark(f)
            j="wrong" + "-" + str(n) + ".pdf"
            addwatermarrk(pdfname,j,n,f)
        if len(d) == n+1:
            zipfiles (output_path)

           
