# Codigo para organizar los archivos de una carpeta de acuerdo a su tipo

import os
import shutil


Ruta='C:/Users/Fernando/Downloads'


# Crear carpetas para organizar archivos

Tipos=['Word','Datos','Presentaciones','Ejecutables','Comprimidos','PDFs','Imagenes','txt','TEX','Codigos','FITS','Otros']

for carpeta in Tipos:
    ruta_carpeta=os.path.join(Ruta,carpeta)
    if  not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)

# Mover los archivos a las carpetas creadas

for  archivo in os.listdir(Ruta):

    if archivo.endswith('.jpeg') or archivo.endswith('.png') or archivo.endswith('.jpg'):
        shutil.move(os.path.join(Ruta,archivo),os.path.join(Ruta,'Imagenes',archivo))

    elif archivo.endswith('.pdf'):
        shutil.move(os.path.join(Ruta,archivo),os.path.join(Ruta,'PDFs',archivo))
    
    elif archivo.endswith('.txt'):
        shutil.move(os.path.join(Ruta,archivo),os.path.join(Ruta,'txt',archivo))

    elif archivo.endswith('.tex') or archivo.endswith('.sty'):
        shutil.move(os.path.join(Ruta,archivo),os.path.join(Ruta,'TEX',archivo))


    elif archivo.endswith('.docx') or archivo.endswith('.doc'):
        shutil.move(os.path.join(Ruta,archivo),os.path.join(Ruta,'Word',archivo))
    
    elif archivo.endswith('.pptx') or archivo.endswith('.ppt'):
        shutil.move(os.path.join(Ruta,archivo),os.path.join(Ruta,'Presentaciones',archivo))
    
    elif archivo.endswith('.xlsx') or archivo.endswith('.xls') or archivo.endswith('.csv') or archivo.endswith('.XLS') or archivo.endswith('.sav') or archivo.endswith('.accdb') or archivo.endswith('.xlsm') or archivo.endswith('.pbix'):
        shutil.move(os.path.join(Ruta,archivo),os.path.join(Ruta,'Excel',archivo))
    
    elif archivo.endswith('.py') or archivo.endswith('.ipynb') or archivo.endswith('.R') or archivo.endswith('.Rmd') or archivo.endswith('.md'):
        shutil.move(os.path.join(Ruta,archivo),os.path.join(Ruta,'Codigos',archivo))
    
    elif archivo.endswith('.zip') or archivo.endswith('.rar'):
        shutil.move(os.path.join(Ruta,archivo),os.path.join(Ruta,'Comprimidos',archivo))
    
    elif archivo.endswith('.exe') or archivo.endswith('.msi'):
        shutil.move(os.path.join(Ruta,archivo),os.path.join(Ruta,'Ejecutables',archivo))

    elif archivo.endswith('.fits') or archivo.endswith('.fit'):
        shutil.move(os.path.join(Ruta,archivo),os.path.join(Ruta,'FITS',archivo))

    elif archivo.endswith('.json') or archivo.endswith('.html') or archivo.endswith('.htm') or archivo.endswith('.mp4'):
        shutil.move(os.path.join(Ruta,archivo),os.path.join(Ruta,'Otros',archivo))




