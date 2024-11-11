import cv2
import pytesseract
import numpy as np
import os
def combine(old,new):
    with open(old,'r',encoding='utf-8') as f1 ,open(new,'r',encoding='utf-8') as f2:
        text1=f1.readlines()
        text2= f2.readlines()
    return(''.join(text1)+'\n'+''.join(text2))
# =-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-

def comapre(NewTextFile,main):
    if not os.path.exists(main):
        with open(main, 'w') as f:
            pass
    text2=text3=''
    with open(NewTextFile,'r',encoding='utf-8') as f2,open(main,'r',encoding='utf-8') as f3:
        text2= f2.readlines()
        text3= f3.readlines()
    result=''.join(text2)
    main=''.join(text3)
    if  result!=main:
        print('this are not the same')
        if len(result)<len(main):
            print('this is bigger new price added')
            return True
    print('this are same')
    return False    
# =-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def readd(pathOfImg,name):
    fileTypeS = slice(-4, None) 
    files = [f for f in os.listdir(pathOfImg) if os.path.isfile(os.path.join(pathOfImg, f))]
    myFile='C:/xampp/htdocs/Watsapp/myfile.txt'
    file='result.txt'
    if os.path.exists(file):
        open(file,'w').close()
    else:
        open(file,'w').close()
    if not os.path.exists(myFile):
        open(myFile,'w').close()
    for f in files:
        if f[fileTypeS] in ['jpeg', '.jpg']:
            print('this is',f,'img')
           
            main(os.path.join(pathOfImg,f),name,pathOfImg)
            TextFromNew=resltText=''
            
            with open(file,'a',encoding='utf-8') as f,open('new.txt','r',encoding='utf-8')as f2:
                
                TextFromNew=f2.readlines()
                TextFromNew=''.join(TextFromNew)
                f.writelines(TextFromNew)


    if comapre(myFile,file):
        open(myFile,'w',encoding='utf-8').close()
        with open(file,'r',encoding='utf-8') as f,open(myFile,'w',encoding='utf-8')as f2:
                resltText=f.readlines()
                resltText=''.join(resltText)
                f2.writelines(resltText)        
                      

# =-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-

def NoNoice(img):
        kernel=np.ones((1,1),np.uint8)
        img=cv2.dilate(img,kernel,iterations=1)
        img=cv2.erode(img,kernel,iterations=3)
        img=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
        img=cv2.medianBlur(img,3)
        return img
# =-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-

def main(pathOfImg,name,dir): 

    imgPath = pathOfImg
    img = cv2.imread(imgPath)
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
            text=pytesseract.image_to_string(roi,lang='eng+fas')
            
           
            # for re in ret:
            #     if ',' in re:
            #         # with open(os.path.join(dir,resultName),'a',encoding='utf-8')as found:
            #         foundT+='\n'+re
            with open('new.txt','a',encoding='utf-8')as found:
                        found.writelines(text)
            
            os.system('cls')


    print('new file created......')
