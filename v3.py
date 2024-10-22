from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import fileMover as F
import xpath as X
import time
import os
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
input('press any key to contuie...')
if chat := dv.find_elements(By.XPATH, X.chatPresent)!=[]:
    chat=dv.find_elements(By.XPATH,X.chatPresent)
    print('you scan the code currectly...')
    try:
        for C in chat:
            print('clicking on a chat')
            C.click()
            s()#sleep
            if name:=dv.find_element(By.XPATH,X.chatName):
                print('looking to :',name.text)
                print('looking for imgs in this chat..')
                if dv.find_elements(By.XPATH,X.imgE2) !=[]:
                    lanEimg=dv.find_elements(By.XPATH,X.imgE2)
                    print('languge of driver is english also img stats are <TRUE>\ntrying to download')
                    for imgF in lanEimg:
                        try:
                            if not imgF.is_displayed():
                                dv.execute_script("arguments[0].scrollIntoView();", imgF)
                                s(3)
                            
                            if imgF.is_displayed():
                                dv.execute_script("arguments[0].scrollIntoView();", imgF)
                                s(2)
                                imgF.click() 
                                s(2)
                                print('clicked on img checking if its a grop our not')
                                if dv.find_element(By.XPATH,X.singleImgE)!=None:
                                    single=dv.find_element(By.XPATH,X.singleImgE)
                                    print('its single img trying to download')
                                    single.click()
                                    s()
                                    #add download move file and check here........................................
                                    print('clicked download button is true')
                                    back()    
                                    s(2)                               
                                    continue
                                
                                elif dv.find_elements(By.XPATH,X.gropImg)!=[]:
                                    print('its a grop massege')
                                    grop=dv.find_elements(By.XPATH,X.gropImg)
                                    grop[0].click()
                                    s(2)
                                    if dv.find_element(By.XPATH,X.gropImgP2)!=None:
                                        print('found the download button trynig to download')
                                        gropP2=dv.find_element(By.XPATH,X.gropImgP2)
                                        gropP2.click()
                                        s()
                                        #download move here..............
                                        back()
                                        s(2)
                                        continue
                                
                        except Exception as clickError:
                            print('some thing went wrong while clicking img :',clickError)
                            input('look with iss...')
                elif lanPimg:=dv.find_elements(By.XPATH,X.imgP)!=[]:
                    print('settings on persian..')

            else:
                print('no name found..')
    except Exception as error:
        print(error)
        input('look at it god whyyyyyyy')
else:
    print('no chat found')