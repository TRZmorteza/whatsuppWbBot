import shutil
import os


def direct():
    # os.makedirs(B, exist_ok=True) 
    # imgChatName('some name' )
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

B = r'C:\xampp\htdocs\whatsapp' 
def make(name):
    destination_dir = os.path.join(B, name)
    if not os.path.isdir(destination_dir):
        os.makedirs(destination_dir, exist_ok=True)
        print('new chat folder created...') 
    else:
        print('folder for this chat already exists....')





def notToDay(date,fullDate):
    os.makedirs('C:/xampp/htdocs/whatsapp/baygani/', exist_ok=True)
    new_path=f'C:/xampp/htdocs/whatsapp/baygani/{fullDate}.txt'
    os.rename('C:/xampp/htdocs/whatsapp/myfile.txt', new_path)
    return date


def seek(name,date):
    os.makedirs(B, exist_ok=True) 
    os.makedirs(os.path.join(B,'tempRead'), exist_ok=True) 
    os.makedirs(os.path.join(B,name,date), exist_ok=True) 
    imgChatName(name)
    chekAndRename()


    files = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]
    secDes=os.path.join(B,'tempRead')
    # print(files)
    destination_dir = os.path.join(B, name,date)
    if not os.path.isdir(destination_dir) and not os.path.isdir(secDes):
        os.makedirs(destination_dir, exist_ok=True)  
        os.makedirs(os.path.join(B,'tempRead'), exist_ok=True)  
        for f in (files):
            name,Ftypes=os.path.splitext(f)       
            chekAndRename(name)
            if Ftypes in ['.jpeg', '.jpg','.txt'] and name!='users': 
                shutil.copy(os.path.join(os.getcwd(), f),os.path.join(B,'tempRead', f))
                shutil.move(os.path.join(os.getcwd(), f), os.path.join(destination_dir, f))
    else:          
        for f in (files):
            name,Ftypes=os.path.splitext(f)  
          
            if Ftypes in ['.jpeg', '.jpg','.txt'] and name!='users': 
                shutil.copy(os.path.join(os.getcwd(),f'{name}{Ftypes}'),os.path.join(B,'tempRead', f))
                shutil.move(os.path.join(os.getcwd(), f), os.path.join(destination_dir, f))
def chekAndRename ():
    oldfiles = [f for f in os.listdir('C:\\xampp\\htdocs\\whatsapp\\tempRead\\') if os.path.isfile(os.path.join('C:\\xampp\\htdocs\\whatsapp\\tempRead\\', f))]
    newFiles= [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]
    
    for old in oldfiles:
       
        count=0
        oldName,_=os.path.splitext(old)

        try:
            for new in newFiles:
                newName,type=os.path.splitext(new)
                
                if oldName==newName and type not in '.py' and oldName!='users':
                    notHere=True
                    i=0
                    src =f'{oldName}{i}{type}'
                    
                    while   notHere:
                        newFiles= [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]

                        for new in newFiles:
                            newName,type=os.path.splitext(new)
                            
                            if src==newName and type not in '.py':
                                src =f'{oldName}{i}{type}'
                                i+=1
                        cfiles = [f for f in os.listdir('C:\\xampp\\htdocs\\whatsapp\\tempRead\\') if os.path.isfile(os.path.join('C:\\xampp\\htdocs\\whatsapp\\tempRead\\', f))]
                        for c in cfiles:
                            if src == c:
                                pass
                        
                        os.rename(old,src)
        except:
            print('y')          
      
def imgChatName(chatName ):
    oldfiles = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]
    toRename=[]
    for file in oldfiles:
        _,typ=os.path.splitext(file)
        if typ in ['.jpeg','.png','.jpg']:
            toRename.append(file)
    for index,img in enumerate(toRename):
        _,typ=os.path.splitext(img)
        os.rename(img,f'{chatName}{index}{typ}')
    print(toRename)
     
if __name__=='__main__':
    direct()