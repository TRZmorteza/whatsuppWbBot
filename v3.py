from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import fileMover as F
import xpath as X
import time
import os
import pickle
from datetime import date
options = Options()
options.add_experimental_option("prefs", {
    "download.default_directory": os.getcwd(),
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
})
def back():
    act.send_keys(Keys.ESCAPE).perform()
def s(s=5):
    time.sleep(s)
#=-=-=-=-=-=-=-==-=-==-=-=-=-=-
print('options are looded...')
dv=webdriver.Chrome(options=options)
act=ActionChains(dv)
dv.get('https://web.whatsapp.com')
with open('c.pkl', 'rb') as file:
    cookie = pickle.load(file)
for c in cookie:
    c['domain']='.web.whatsapp.com'
    try:
     dv.add_cookie(c)
    except Exception as e :
        pass
s()
dv.get('https://web.whatsapp.com')

input('press any key to contuie...')
if chat := dv.find_elements(By.XPATH, X.chatPresent)!=[]:
    chat=dv.find_elements(By.XPATH,X.chatPresent)
    print('you scan the code currectly...')
    try:
        for C in chat:
            print('clicking on a chat')
            C.click()
            F.make(dv.find_element(By.XPATH,X.chatName).text)
            s()#sleep
            if name:=dv.find_element(By.XPATH,X.chatName):#chat name
                print('looking to :',name.text)
                print('looking for imgs in this chat..')
                if dv.find_elements(By.XPATH,X.imgs) !=[]:
                    lanEimg=dv.find_elements(By.XPATH,X.imgs)
                    print('loooooooooooooooooooooooooooooooook at this\n',f"{dv.find_element(By.XPATH,X.chatName).text} has imgs :",len(lanEimg))
                    print('languge of driver is english also img stats are <TRUE>\ntrying to download')
                    s(3)
                    for imgF in lanEimg:
                        try:
                            
                                dv.execute_script("arguments[0].scrollIntoView();", imgF)
                                s(3)
                                if imgF.is_displayed():
                                    print('img is visibel')
                                    dv.execute_script("arguments[0].click();", imgF)
                                
                               
                                print('ok 55..............................................')
                                print('clicked on img checking if its a grop our not')
                                if dv.find_element(By.XPATH,X.singleImgE)!=None:
                                    print('its single img trying to download')
                                    
                                    single=dv.find_element(By.XPATH,X.singleImgE)
                                    single.click()
                                    s()
                                    F.seek(dv.find_element(By.XPATH,X.chatName).text,f"{date.today().year}_{date.today().month}_{date.today().day}")
                                    print('clicked download button is true')
                                    #add download move file and check here........................................
                                    s(3)
                                    back()    
                                    s(2)                               
                                
                                    dv.execute_script("arguments[0].scrollIntoView();", imgF)
                                    s(7)
                                   
                                
                                print('its not a single')
                                if Groupmenu:=dv.find_elements(By.XPATH,X.knewGmenu):
                                    Groupmenu[0].click()
                                    s(2)
                                    groupmenuD=dv.find_element(By.XPATH,X.knewGmenuD)
                                    if groupmenuD:
                                        groupmenuD.click()
                                        s(2)
                                    back()
                                    F.seek(dv.find_element(By.XPATH,X.chatName).text,f"{date.today().year}_{date.today().month}_{date.today().day}")
                                        #download move here..............
                                    back()
                                    s(2)
                                        
                                
                        except Exception as clickError:
                            print('some thing went wrong while clicking img :',clickError)
                            print('look with iss...')
                            
                            s()
            if elementtexts:=
                elif lanPimg:=dv.find_elements(By.XPATH,X.imgP)!=[]:
                    print('settings on persian..')

            else:
                print('no name found..')
    except Exception as error:
        
        print('look at it god whyyyyyyy:',error)
        s()
else:
    print('no chat found')