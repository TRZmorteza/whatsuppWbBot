import shutil
import os

import readd as A
def direct():
    # reN(os.getcwd(),'my secrate')
    seek('test','t_e_s_t')

def findDop(path=os.path.join(os.getcwd(),'tempRead')):    
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    for f in files:
       
        if ')'in f:
            os.remove(os.path.join(path, f))


def reN(name,date):
    files=[f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(),f))]
    for i,f in enumerate(files):
        isNew,fileType=os.path.splitext(f)
        
        if fileType in ['.txt','.jpeg','.jpg']and isNew not in['new','result']:
            os.rename(f,f"{name}_{date}{fileType}")

B = r'C:\xampp\htdocs\Watsapp' 
def make(name):
    destination_dir = os.path.join(B, name)
    if not os.path.isdir(destination_dir):
        os.makedirs(destination_dir, exist_ok=True)
        print('new chat folder created...') 
    else:
        print('folder for this chat already exists....')

def seek(path,date):
        reN(path,date)
        move(path,date)


def notToDay(date,fullDate):
    os.makedirs('C:/xampp/htdocs/Watsapp/baygani/', exist_ok=True)
    new_path=f'C:/xampp/htdocs/Watsapp/baygani/{fullDate}.txt'
    os.rename('C:/xampp/htdocs/Watsapp/myfile.txt', new_path)
    return date


def move(name,date):
    
    

    files = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]
    secDes=os.path.join(B,'tempRead')
    print(files)
    destination_dir = os.path.join(B, name,date)
    if not os.path.isdir(destination_dir) and not os.path.isdir(secDes):
        os.makedirs(destination_dir, exist_ok=True)  
        os.makedirs(os.path.join(B,'tempRead'), exist_ok=True)  
        for f in (files):
            _,Ftypes=os.path.splitext(f)       
            if Ftypes in ['.jpeg', '.jpg','.txt']: 
                shutil.copy(os.path.join(os.getcwd(), f),os.path.join(B,'tempRead', f))
                #shutil.move(os.path.join(os.getcwd(), f), os.path.join(destination_dir, f))
    else:                           
        for f in (files):
            _,Ftypes=os.path.splitext(f)       
            if Ftypes in ['.jpeg', '.jpg','.txt']: 
                shutil.copy(os.path.join(os.getcwd(), f),os.path.join(B,'tempRead', f))
                #shutil.move(os.path.join(os.getcwd(), f), os.path.join(destination_dir, f))


if __name__=='__main__':
    direct()