import shutil
import os


def direct():

    # seek('test','t_e_s_t')
    # for i in range(0,10):
    #     open('hkhjkhkj.txt','w').close()
    #     seek('name','t_e_s_t')
    for i in range(0,5):
        open(f"thing{i}.txt",'w').close()
        open(f"thin{i}.jpg",'w').close()
    # imgChatName('name','today')
    seek('name','today')

B = r'C:\\xampp\htdocs\whatsapp' 
def make(name):
    destination_dir = os.path.join(B, name)
    if not os.path.isdir(destination_dir):
        os.makedirs(destination_dir, exist_ok=True)
        print('new chat folder created...') 
    else:
        print('folder for this chat already exists....')



def seek(name ,date):
    main=name
    os.makedirs(B, exist_ok=True) 
    os.makedirs(os.path.join(B,'tempRead'), exist_ok=True) 
    os.makedirs(os.path.join(B,name,date), exist_ok=True) 
    newfiles = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]
    oldfiles = [f for f in os.listdir(os.path.join(B, name,date)) if os.path.isfile(os.path.join(B, name,date, f))]
    renamed=[]
    imgCounter=0
    for file in newfiles:
        _,fileType=os.path.splitext(file)
        if fileType == '.jpg':
            imgCounter+=1
            os.rename(file,f'a{name}_{imgCounter}{fileType}')
            
    textCounter=0
    for file in newfiles:
        _,fileType=os.path.splitext(file)
        if fileType == '.txt' and not name[0]== 'users':
            textCounter+=1
            os.rename(file,f'a{name}_{textCounter}{fileType}')
    # print(imgCounter,textCounter) 
    bigest=[0,0]#0 img and 1 is txt   
    for files in oldfiles:
        #look for begest number
        name,typ=os.path.splitext(files)
        if typ=='.jpg':
            print('looking for begest img')
            name=name.split('_')
            
            if bigest[0]<int(name[1]):
                bigest[0]=int(name[1])
            
        if typ=='.txt' and not name[0]== 'users':
            print('looking for begest text')
            name=name.split('_')
            
            if bigest[1]<int(name[1]):
                bigest[1]=int(name[1])
        print(bigest[0],bigest[1])
        newfiles = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]
   
    for files in newfiles:
        name,typ=os.path.splitext(files)
        name=name.split('_')
        if typ=='.jpg':
            os.rename(files,f'{main}_{int(name[1])+int(bigest[0])}{typ}')
        if typ=='.txt' and not name[0]== 'users':
            os.rename(files,f'{main}_{int(name[1])+int(bigest[1])}{typ}')
    newfiles = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]
    for f in newfiles:
            name,Ftypes=os.path.splitext(f)  
          
            if Ftypes in ['.jpeg', '.jpg','.txt'] and name!='users': 
                shutil.copy(os.path.join(os.getcwd(),f),os.path.join(B,'tempRead'))
                shutil.move(os.path.join(os.getcwd(), f), os.path.join(B, main,date))    



    

if __name__=='__main__':
    direct()