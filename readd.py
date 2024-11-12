import cv2
import pytesseract
import numpy as np
from datetime import date
import shutil


import os
def lastChats():
    currentchat=os.path.join(os.getcwd(),'tempRead','chats.txt')
    main=os.path.join(os.getcwd(),'lastChat')
    os.makedirs(main,exist_ok=True)
    if os.path.isdir(os.path.join(main,f'{date.today().month}_{date.today().day}','chats.txt')):
        tempMain=tempNew=''
        pathToMain=os.path.join(main,str(date.today().day),'chats.txt')
        with open(pathToMain,'r' ,encoding='utf-8')as mainT,open(currentchat,'r',encoding='utf-8')as newT:
            tempMain=mainT.readlines()
            tempMain=''.join(tempMain)
            tempNew=newT.readlines()
            tempNew=''.join(tempNew)
        if len(tempNew)>len(tempMain):
            with open(pathToMain,'w',encoding='utf-8') as newMain:
                newMain.writelines(tempNew)
    else:
        os.makedirs(os.path.join(main,f'{date.today().month}_{date.today().day}'),exist_ok=True)
        shutil.copy(currentchat,os.path.join(main,f'{date.today().month}_{date.today().day}','chats.txt'))


def combine(old,new):
    with open(old,'r',encoding='utf-8') as f1 ,open(new,'r',encoding='utf-8') as f2:
        text1=f1.readlines()
        text2= f2.readlines()
    return(''.join(text1)+'\n'+''.join(text2))
# =-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-

def comapre(NewTextFile,main,chats):
    chats=os.path.join(chats,'chats.txt')
    if not os.path.exists(main):
        open(main, 'w').close()
        return True
            
    text1=text2=text3=''
    with open(chats,'r',encoding='utf-8') as f1,open(NewTextFile,'r',encoding='utf-8') as f2,open(main,'r',encoding='utf-8') as f3:
        text1= f1.readlines()#chat text
        text2= f2.readlines()#OCRs text
        text3= f3.readlines()#last combine
    
    chat=''.join(text1)
    myOCR=''.join(text2)
    lastCo=''.join(text3)
    result=myOCR+chat
    if  result!=lastCo:
        
        if len(result)>len(lastCo):
            print('this is bigger\nnew price added')
            return True
    
    return False    
# =-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-

pytesseract.pytesseract.tesseract_cmd = r'D:\project needs\py tesserect\tesseract.exe'
def readd(pathOfImg=os.path.join(os.getcwd(),'tempRead')):
    if not os.path.isdir(pathOfImg):
        os.makedirs(pathOfImg,exist_ok=True)
    files = [f for f in os.listdir(pathOfImg) if os.path.isfile(os.path.join(pathOfImg, f))]
    myFile='C:/xampp/htdocs/Watsapp/myfile.txt'
    currentchat=os.path.join(os.getcwd(),'tempRead')#,'chats.txt'
    file=os.path.join(os.getcwd(),'tempRead','result.txt')
    
    open(file,'w').close()
   
    if not os.path.exists(myFile):
        open(myFile,'w').close()
    for f in files:
        _,Ftypes=os.path.splitext(f)
        
        if Ftypes in ['.jpeg', '.jpg']:
            print('looking at',f,'')
           
            main(os.path.join(pathOfImg,f))
            TextFromNew=resltText=''
            
            with open(file,'a',encoding='utf-8') as f,open('new.txt','r',encoding='utf-8')as f2:
                
                TextFromNew=f2.readlines()
                TextFromNew=''.join(TextFromNew)
                f.writelines(TextFromNew)
    open(os.path.join(currentchat,'chats.txt'),'w').close()
    tempText=''
    for f in files:
        NoName,Ftypes=os.path.splitext(f)

        if Ftypes in ['.jpeg', '.jpg']:
               
                try:
                    os.remove(os.path.join(os.getcwd(),'tempRead', f))
                except:
                     pass
        
        if Ftypes in['.txt']and  NoName not in['result','chats']:
            with open(os.path.join(currentchat,f),'r',encoding='utf-8') as chattext:
                tempText=chattext.readlines()
                tempText+=''.join(tempText)
            os.remove(os.path.join(currentchat,f))
    with open(os.path.join(currentchat,'chats.txt'),'w',encoding='utf-8')as final:
        final.writelines(tempText)
    lastChats()

         
    

    print(myFile)
    if comapre(file,myFile,currentchat):# NewTextFile,main,chats
        currentchat=os.path.join(currentchat,'chats.txt')
        result=''
        with open(file,'r',encoding='utf-8') as newFile,open(currentchat,'r',encoding='utf-8')as chats,open(myFile,'w',encoding='utf-8')as myfile:
                myOCR=newFile.readlines()
                Tchat=chats.readlines() 
                myOCR=''.join(myOCR)       
                Tchat=''.join(Tchat)
                result=myOCR+Tchat       
                myfile.writelines(result)
# =-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-

def NoNoice(img):
        kernel=np.ones((1,1),np.uint8)
        img=cv2.dilate(img,kernel,iterations=1)
        img=cv2.erode(img,kernel,iterations=3)
        img=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
        img=cv2.medianBlur(img,3)
        return img
# =-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-

def main(path): 

    imgPath =path

    img = cv2.imread(imgPath)
    height, width, _ = img.shape

    got=False

    if True:#models for lists
        if height==838 and width==804:#case1
            f=1
            cords=[[42,232,381,531]]
            got=True

        if height==606 and width==679:#case25
            f=1
            cords=[[  1 ,1 ,605 ,678]]
            got=True




        if height==1080 and width==893:#case 2
            f=2
            cords=[[0 ,130 ,944 ,417],[416 ,130 ,950 ,477]]
            got=True



        if height==928 and width==924:#case 3
            f=3
            cords=[[  630 ,132 ,478 ,245]
                ,[  334 ,132 ,476 ,260],[  61 ,132 ,606 ,244]]
            got=True




        if height==1280 and width==905:#case 4
            f=2
            cords=[[ 9 ,199 ,987 ,423]
                ,[ 457 ,201 ,991 ,427]
                ]
            got=True


        if height==1280 and width==1278:#case 5
            f=3
            cords=[[  53 ,129, 1033, 321 ],
                [  371 ,124 ,771 ,420 ],
                [ 798 ,126 ,855 ,441 ]
                ]
            got=True


        if height==724 and width==1094:#case 6
            f=2
            cords=[
                    [ 61 ,33 ,582 ,323],
                    [ 399 ,32 ,568 ,333]
                ]
            got=True




        if height==1080 and width==918:#case 7
            f=1
            cords=[
                    [ 0 ,186 ,530 ,665]
                ]
            got=True




        if height==1080 and width==1053:#case 8
            f=2
            cords=[
                    [ 0 ,118 ,861 ,529],
                    [ 540 ,120 ,875 ,513]
                ]
            got=True

        if height==1080 and width==942:#case 9
            f=3
            cords=[
                    [ 0 ,36 ,1044 ,251],
                    [  255 ,29 ,1051 ,312 ],
                    [  567 ,38 ,1041 ,327]
                ]
            got=True


        if height==1080 and width==834:#case 10
            f=2
            cords=[
                    [84 ,15 ,1033 ,308],
                    [395 ,19 ,1025 ,317],
                ]
            got=True


        if height==766 and width==1080:#case 11
            f=3
            cords=[
                    [   14 ,70 ,676 ,328],
                    [   350 ,70 ,675 ,354],
                    [  711 ,70 ,675 ,352]
                ]
            got=True



        if height==1600 and width==1308:#case 12
            f=1
            cords=[[ 70 ,264 ,887 ,1173]]
            got=True

        if height==766 and width==1080:#case 13
            f=3
            cords=[
                    [   0 ,53 ,710 ,319],
                    [   321 ,51 ,711 ,374],
                    [   695 ,49 ,714 ,385]
                ]
            got=True
        if height==1080 and width==770:#case 14
            f=2
            cords=[
                    [ 0 ,127 ,953 ,385],
                    [ 391 ,126 ,954 ,379],
                    
                ]
            got=True


        if height==1080 and width==763:#case 15
            f=4
            cords=[
                    [ 5 ,55 ,930 ,187],
                    [ 194 ,52 ,936 ,184],
                    [ 381 ,50 ,935 ,184],
                    [ 566 ,46 ,941 ,196]
                ]
            got=True


        if height==662 and width==1080:#case 16
            f=5
            cords=[
                    [   3 ,0 ,660 ,237],
                    [   239 ,0 ,608 ,225],
                    [   465 ,0 ,662 ,227],
                    [   694 ,0 ,661 ,210 ],
                    [   906 ,0 ,662 ,164 ]
                ]
            got=True

        if height== 532 and width==503:#17
            f=1
            cords=[[ 0 ,1 ,102 ,503]]
            got=True


        if height==774 and width==1080:#case 18
            f=4
            cords=[
                    [  0 ,51 ,723 ,254],
                    [  257 ,51 ,723 ,282],
                    [  538 ,51 ,688 ,267],
                    [  808 ,48 ,692 ,272]
                ]
            got=True


        if height==1461 and width==1182:#case 19
            f=3
            cords=[
                    [  0 ,98 ,1308 ,350],
                    [  350 ,100 ,1361 ,410],
                    [  766 ,102 ,1115 ,416]
                ]
            got=True

        if height==950 and width==953:#case 20
            f=3
            cords=[
                    [  0 ,98 ,1308 ,350],
                    [  350 ,100 ,1361 ,410],
                    [  766 ,102 ,1115 ,416]
                ]
            got=True


        if height==1461 and width==1182:#case 20
            f=2
            cords=[
                    [    8 ,296 ,802 ,574],
                    [    602 ,296 ,806 ,572]
                ]
            got=True


        if height==1080 and width==893:#case 23
            f=2
            cords=[[0 ,130 ,944 ,417],[416 ,130 ,950 ,477]]
            got=True
    text=''

    if got:    
       
        if f!=1:
            for j in range(0,f):
                x,y,h,w=cords[j][0],cords[j][1],cords[j][2],cords[j][3]
                roi=img[y:y+h,x:x+w]

                text+= pytesseract.image_to_string(roi,lang="eng+fas")


        else:
                x,y,h,w=cords[0][0],cords[0][1],cords[0][2],cords[0][3],
                roi=img[y:y+h,x:x+w]
             
                text+= pytesseract.image_to_string(roi,lang='eng+fas')

 
        
    else:
        print("need new model!!!")
        img = cv2.imread(path)
        if os.path.isdir(path):
            _,fileName=os.path.split(path)
            num=0
            for root,dirs,filesPresent in os.walk(os.path.join(os.getcwd(),'debug')):
                 num+=len(filesPresent)   
            
            cv2.imwrite(os.path.join(os.getcwd(),'debug',f'{fileName}_debug({num+1})'),img)
        img=cv2.bitwise_not(img)


        img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        # cv2.imwrite('img/blwck.jpg', img_gray)

        blur = cv2.GaussianBlur(img_gray, (9, 9), 0)
        # cv2.imwrite('img/blur.jpg', blur)

        threshclear = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        # cv2.imwrite('img/trClear.jpg',threshclear)

        thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        thresh=NoNoice(thresh)
        # cv2.imwrite('img/tr.jpg',thresh)

        kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(20,2))
        dilate=cv2.dilate(thresh,kernel,iterations=5)
        cv2.imwrite('img/dilate.jpg',dilate)
        dilateClear=cv2.dilate(threshclear,kernel,iterations=2)
        cv2.imwrite('img/dilateClear.jpg',dilateClear)
        cnts=cv2.findContours(dilate,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cnts=cnts[0] if len(cnts)== 2 else cnts[1]
        cnts=sorted(cnts,key=lambda x:cv2.boundingRect(x)[1])
        
            
        print('poto shop done..\ncreating new new.txt')
        open('new.txt', 'w').close()
        for c in cnts:
            print('looking at results')
            x,y,w,h=cv2.boundingRect(c)
            if h>10:
                print(x,y,w,h)
                
                roi=img[y:y+h,x:x+w]
            
            
                # resultName=name+'.txt'
                foundT=''
                text+=pytesseract.image_to_string(roi,lang='eng+fas')
                
            
                # for re in ret:
                #     if ',' in re:
                #         # with open(os.path.join(dir,resultName),'a',encoding='utf-8')as found:
                #         foundT+='\n'+re
                os.system('cls')
    with open('new.txt','a',encoding='utf-8')as found:
            found.writelines(text)
                


    print('new file created......')
if __name__ =="__main__":
    readd()