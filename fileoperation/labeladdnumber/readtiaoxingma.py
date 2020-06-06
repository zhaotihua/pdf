# 导入模块

from pyzbar import pyzbar



#import cv2

# 读取图片

#image = cv2.imread('psReport_0.png')
#image = cv2.imread(f)

# 找到图像中的条形码并进行解码

#barcodes = pyzbar.decode(image)

def decode(image,barcodes):
    

    # 循环检测到的条形码

    for barcode in barcodes:
        

        # 提取条形码的边界框的位置

         # 画出图像中条形码的边界框

        #(x, y, w, h) = barcode.rect

        #cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 5)

        # 条形码数据为字节对象，所以如果我们想在输出图像上

        # 画出来，就需要先将它转换成字符串
        barcodeData = barcode.data.decode("utf-8")
        print (barcodeData)
        if len(barcodeData) == 34:
            text = barcodeData[22:34]
        else:
            text = barcodeData

        #barcodeType = barcode.type

        # 绘出图像上条形码的数据和条形码类型

        #text = "{} ({})".format(barcodeData, barcodeType)
        #text1 = "{} ({})".format(barcodeData)
        print (text)
        #print (text1)

        #cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,.8, (255, 0, 0), 2)

        # 向终端打印条形码数据和条形码类型
        print (text)
        
        

        #print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
        return text

    

#plt.show()

#. 识别二维码

#decode(image, barcodes)

# 读取图片

#image = cv2.imread('image2.png')

# 找到图像中的条形码并进行解码

#barcodes = pyzbar.decode(image)

# 识别条形码

#path = 'C:/Users/Dell/Desktop/test'
#len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])
