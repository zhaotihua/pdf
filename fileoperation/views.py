from django.shortcuts import render


from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST
from django.http import HttpResponse
from django.core.files import File
import os

from fileoperation.labeladdnumber.getimage import pyMuPDF2_fitz
from fileoperation.labeladdnumber.readtiaoxingma import decode
from fileoperation.labeladdnumber.excelline1 import readExceline1
from fileoperation.labeladdnumber.excelline2 import readExceline2
from fileoperation.labeladdnumber.excelline3 import readExceline3
from fileoperation.labeladdnumber.textmark import create_watermark
from fileoperation.labeladdnumber.addwatermarrk import addwatermarrk
from fileoperation.labeladdnumber.main1 import main
from fileoperation.labeladdnumber.zipfiles import zipfiles

import zipfile


#import os
#import cv2
from pyzbar import pyzbar
import sys, fitz


 
SAVED_FILES_DIR = r'files/'    
excel = 'a'
pdf  = 'b'

def render_home_template(request):
    files = os.listdir(SAVED_FILES_DIR)
    return render(request, 'home.html', {'files': files})


@require_GET
def home(request):
    if not os.path.exists(SAVED_FILES_DIR):
        os.makedirs(SAVED_FILES_DIR)
 
    return render_home_template(request)


@require_GET
def download(request, filename):
    file_pathname = os.path.join(SAVED_FILES_DIR, filename)
 
    with open(file_pathname, 'rb') as f:
        file = File(f)
 
        response = HttpResponse(file.chunks(),
                                content_type='APPLICATION/OCTET-STREAM')
        response['Content-Disposition'] = 'attachment; filename=' + filename
        response['Content-Length'] = os.path.getsize(file_pathname)
 
    return response

@require_GET
def wirtxtt(request):
    #
    excel ="a"
    pdf = "a"
    a = os.listdir(SAVED_FILES_DIR)
    
    for i in a:
        x = os.path.splitext(i)[-1][1:]
        if x == "xlsx":
            excel = i
        elif x == "pdf":
            pdf = i
   
    if excel != "a" and pdf !="a":
        pdfname = SAVED_FILES_DIR + pdf
        excelfilename = SAVED_FILES_DIR + excel
        imagePath =  "image"
        output_path = SAVED_FILES_DIR
        main1 (pdfname,excelfilename,imagePath,output_path)
        
            
    return render_home_template(request)
    

@require_POST
def upload(request):
    assert1 = "c"
    

    file = request.FILES.get("filename", None)
    
    
    if not file:
        return render_home_template(request)
 
    pathname = os.path.join(SAVED_FILES_DIR, file.name)
 
    with open(pathname, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    
    
    
    return render_home_template(request)





@require_GET
def delete(request):
    x = request.GET.get("nid")
    os.remove(SAVED_FILES_DIR + x)
    #y = str(x)
    #if x == "lnc.xlsx":
      #  with open(SAVED_FILES_DIR + "tt.txt", 'w') as destination:
       #     destination.write("yyyyyy")
    return render_home_template(request)




