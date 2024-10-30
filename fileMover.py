import shutil
import os

def direct():
    seek('test','t_e_s_t')

B = r'C:\xampp\htdocs\Watsapp' 
def make(name):
    destination_dir = os.path.join(B, name)
    if not os.path.isdir(destination_dir):
        os.makedirs(destination_dir, exist_ok=True)
        print('new chat folder created...') 
    else:
        print('folder for this chat already exists....')

def seek(path,date):
    fileTypeS = slice(-4, None) 
    files = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]
    destination_dir = os.path.join(B, path,date)
    numberFiles=0
    for f in (files):

        if f[fileTypeS] in ['jpeg', '.jpg','.txt']: 
            numberFiles+=1#count the amount if files present in download list
    if os.path.isdir(destination_dir):#check if the path is exists our not
        presentNumberFiles=0
        files = [f for f in os.listdir(destination_dir) if os.path.isfile(os.path.join(destination_dir, f))]
        if f[fileTypeS] in ['jpeg', '.jpg','.txt']:  
            presentNumberFiles+=1#count amount of files presenet in save messages
        if numberFiles>presentNumberFiles:
            shutil.rmtree(destination_dir)
            print('found new imgs old ones are deleted')
            files = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]
            if not os.path.isdir(destination_dir):
                os.makedirs(destination_dir, exist_ok=True)  
                for f in (files):  
                    if f[fileTypeS] in ['jpeg', '.jpg','.txt']: 
                        shutil.move(os.path.join(os.getcwd(), f), os.path.join(destination_dir, f))
        else:
            print('noting new here every thing is same and safe calling it a day')
    else:
        move(path,date)

    
def move(name,date):
    
    fileTypeS = slice(-4, None)  

    files = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]

    destination_dir = os.path.join(B, name,date)
    if not os.path.isdir(destination_dir):
        os.makedirs(destination_dir, exist_ok=True)  
        for f in (files):
             
            if f[fileTypeS] in ['jpeg', '.jpg','.txt']: 
                shutil.move(os.path.join(os.getcwd(), f), os.path.join(destination_dir, f))
    else:
        print('i already get this img checking the amount....')
        if seek(name,date):  
            if f[fileTypeS] in ['jpeg', '.jpg','.txt']: 
                os.makedirs(destination_dir, exist_ok=True)  
                shutil.move(os.path.join(os.getcwd(), f), os.path.join(destination_dir, f))
        else:
            for f in (files):
                
                if f[fileTypeS] in ['jpeg', '.jpg','.txt']: 
                    os.remove(os.path.join(os.getcwd(), f))
            print('deleted the unwanted img...')
if __name__=='__main__':
    direct()