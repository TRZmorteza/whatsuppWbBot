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


def reN(path,name):
    files=[f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))]
    for i,f in enumerate(files):
        isNew,fileType=os.path.splitext(f)
        
        if fileType in ['.txt','.jpeg','.jpg']and isNew not in['new','result']:
            os.rename(f,f"{name}_{i}{fileType}")

B = r'C:\xampp\htdocs\Watsapp' 
def make(name):
    destination_dir = os.path.join(B, name)
    if not os.path.isdir(destination_dir):
        os.makedirs(destination_dir, exist_ok=True)
        print('new chat folder created...') 
    else:
        print('folder for this chat already exists....')

def seek(path,date):
    os.makedirs(os.path.join(os.getcwd(),'tempRead'), exist_ok=True)
    fileTypeS = slice(-4, None) 
    files = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]
    destination_dir = os.path.join(B, path,date)
    numberFiles=0
    findDop(os.getcwd())
    reN(os.getcwd(),path)
    for f in (files):
        _,Ftype=os.path.splitext(f)
        if Ftype in ['.jpeg', '.jpg','.txt']: 
            numberFiles+=1#count the amount if files present in download list
    if os.path.isdir(destination_dir):#check if the path is exists our not
        presentNumberFiles=0
        files = [f for f in os.listdir(destination_dir) if os.path.isfile(os.path.join(destination_dir, f))]
        for f in files:
            _,Ftype=os.path.splitext(f)
            if Ftype in ['jpeg', '.jpg','.txt']:  
                presentNumberFiles+=1#count amount of files presenet in save messages
        if numberFiles>presentNumberFiles:
            shutil.rmtree(destination_dir)
            print('found new imgs old ones are deleted')
            files = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]
            if not os.path.isdir(destination_dir):
                os.makedirs(destination_dir, exist_ok=True)  
                for f in (files):
                    newTxt,Ftype=os.path.splitext(f)  
                    
                    if Ftype in ['.jpeg', '.jpg','.txt']and newTxt not in['new','result']: 
                        

                        shutil.copy(os.path.join(os.getcwd(), f),os.path.join(os.getcwd(),'tempRead', f))

                        shutil.move(os.path.join(os.getcwd(), f), os.path.join(destination_dir, f))           
        else:
            print('noting new here every thing is same and safe calling it a day')
        
    else:
        move(path,date)


def notToDay(date,fullDate):
    os.makedirs('C:/xampp/htdocs/Watsapp/baygani/', exist_ok=True)
    new_path=f'C:/xampp/htdocs/Watsapp/baygani/{fullDate}.txt'
    os.rename('C:/xampp/htdocs/Watsapp/myfile.txt', new_path)
    return date


def move(name,date):
    
    

    files = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]

    destination_dir = os.path.join(B, name,date)
    if not os.path.isdir(destination_dir):
        os.makedirs(destination_dir, exist_ok=True)  
        for f in (files):
            _,Ftypes=os.path.splitext(f)       
            if Ftypes in ['.jpeg', '.jpg','.txt']: 
                shutil.copy(os.path.join(os.getcwd(), f),os.path.join(os.getcwd(),'tempRead', f))
                shutil.move(os.path.join(os.getcwd(), f), os.path.join(destination_dir, f))
                           


if __name__=='__main__':
    direct()