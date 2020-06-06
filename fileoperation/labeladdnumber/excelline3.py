
import json
import xlrd

def readExceline3(excelfilename):
    #filename = 'lnc.xlsx'
    excel = xlrd.open_workbook(excelfilename)
    # 得到第一张表单
    sheet1 = excel.sheets()[0]
    #找到有几列几列
    nrows = sheet1.nrows #行数
    ncols = sheet1.ncols #列数
    line=[]
    line1=[]
    line2=[]
    totalArray=[]
    #title=[]
    # 标题
    #for i in range(0,ncols):
    # title.append(sheet1.cell(0,i).value);
    #数据
    for rowindex in range(0,nrows):
        s=sheet1.cell(rowindex,2).value
        print (s)
        line.append(s)
        print (line)
    return line
#a=(readExcel())
#print (a)
#x=3
#d=a[x]
#print (d)
