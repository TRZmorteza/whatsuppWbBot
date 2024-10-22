import os
import shutil

def make(name):
    destination_dir = os.path.join(os.getcwd(), 'downlods', name)
    if not os.path.isdir(destination_dir):
        os.makedirs(destination_dir, exist_ok=True)
        print('new chat folder created...') 
    else:
        print('folder for this chat already exists....')

def seek(path,date):
    fileTypeS = slice(-5, None) 
    files = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]
    destination_dir = os.path.join(os.getcwd(), 'downlods', path,date)
    numberFiles=0
    for f in (files):
        if f[fileTypeS] in ['.jpeg', '.jpg']: 
            numberFiles+=1#count the amount if files present in download list
    if os.path.isdir(destination_dir):#check if the path is exists our not
        presentNumberFiles=0
        files = [f for f in os.listdir(destination_dir) if os.path.isfile(os.path.join(destination_dir, f))]
        if f[fileTypeS] in ['.jpeg', '.jpg']:  
            presentNumberFiles+=1#count amount of files presenet in save messages
        if numberFiles>presentNumberFiles:
            shutil.rmtree(destination_dir)
            print('found new imgs old ones are deleted')
            return True
        else:
            print('noting new here every thing is same and safe')
            return False

    
def move(name,date):
    
    fileTypeS = slice(-5, None)  

    files = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]

    destination_dir = os.path.join(os.getcwd(), 'downlods', name,date)
    if not os.path.isdir(destination_dir):
        os.makedirs(destination_dir, exist_ok=True)  
        for f in (files):
            print(f[fileTypeS])  
            if f[fileTypeS] in ['.jpeg', '.jpg']: 
                shutil.move(os.path.join(os.getcwd(), f), os.path.join(destination_dir, f))
    else:
        print('i already get this img checking the amount....')
        if seek(name,date):  
            if f[fileTypeS] in ['.jpeg', '.jpg']: 
                os.makedirs(destination_dir, exist_ok=True)  
                shutil.move(os.path.join(os.getcwd(), f), os.path.join(destination_dir, f))
        else:
            for f in (files):
                
                if f[fileTypeS] in ['.jpeg', '.jpg']: 
                    os.remove(os.path.join(os.getcwd(), f))
            print('deleted the unwanted img...')
