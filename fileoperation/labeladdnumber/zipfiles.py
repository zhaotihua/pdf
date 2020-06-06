import zipfile
import os
def zipfiles (output_path):
    input_path =  "finish"
    #output_path = "d:"
    output_name = "123.zip"
    files = os.listdir(input_path)
    f = zipfile.ZipFile(output_path + '/' + output_name, 'w', zipfile.ZIP_DEFLATED)
    print (files)
    
    for file in files:
       
        f.write(input_path + '/' + file)
    f.close()
        
