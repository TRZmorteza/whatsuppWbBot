from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import date
import fileMover as F
import xpath as X
import time
import os
import readImg as ri

# Configure Chrome options
options = Options()
options.add_experimental_option("prefs", {
    "download.default_directory": os.getcwd(),
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
})
def extract_number(input):
    
    words = input.split()
   # print(words)
    if  int(words[2]): 
        return int(words[2])-int(words[0])
    else:
        return -1

 


# Function to sleep for a specified number of seconds
def sleep(s=3):
    time.sleep(s)
# Initialize ActionChains and WebDriver
def esc ():
    act.send_keys(Keys.ESCAPE).perform()
bot = webdriver.Chrome(options=options)
act=ActionChains(bot)
bot.get('https://web.whatsapp.com')
sleep(10)

# Find chat elements
chats = bot.find_elements(By.XPATH, X.chatPresent)

while True:
    print('loading chats...')
    for chat in chats:
            chat.click()
            try:
               
                sleep()
                today=bot.find_element(By.XPATH,X.today)
                act.move_to_element(today).perform()
                sleep(5)
                act.scroll_to_element(today).perform()
                sleep()
            except Exception as e:
                act.send_keys(Keys.ESCAPE).perform()
                print('how')

    for chat in chats:
        act.move_to_element(chat).perform()
        sleep()
        chat.click()
        sleep()
        name = bot.find_element(By.XPATH, X.chatName).text
        F.make(name)
        print('Looking at:', name)
        

        try:
            today=bot.find_element(By.XPATH,X.today)
            act.scroll_to_element(today).perform()
            sleep(6)
            
            try:
                preload=bot.find_element(By.XPATH,X.downloadButtonLoad)
                act.scroll_to_element(preload).perform()
                sleep(6)
                preload=bot.find_element(By.XPATH,X.downloadButtonLoad)
                print('looking for download icon')
                if preload:
                    bot.execute_script("arguments[0].click();", preload)
                    print('click on element')
                    sleep(10) 
            except:#done
                print('no download button')
                print('looking for album')
            try:
                
                album=bot.find_elements(By.XPATH,X.albumImg)
                act.scroll_to_element(album[0]).perform()
                sleep(6)
                print('album found:',len(album))
                album=bot.find_elements(By.XPATH,X.albumImg)
                if album :    
                    for i in album:
                        print('trying to click')
                        act.move_to_element(i).perform()
                        sleep(5)
                        i.click()
                        sleep(5)
                        lenOfAlbum=bot.find_element(By.XPATH,X.lenOfImgs).text
                        le=extract_number(lenOfAlbum)
                        if le != -1:
                            nextBn=bot.find_element(By.XPATH,X.nextButton)
                        
                            menuBn=bot.find_element(By.XPATH,X.downloadMenu)

                            for i in range(0,le+1):
                                sleep(5)
                                bot.execute_script("arguments[0].click();", menuBn)
                                sleep()
                                try:
                                    dtap=bot.find_element(By.XPATH,X.downloadTab)
                                    bot.execute_script("arguments[0].click();", dtap)
                                except:
                                    db=bot.find_element(By.XPATH,X.downloadButton)
                                    bot.execute_script("arguments[0].click();", db)
                                sleep()
                                bot.execute_script("arguments[0].click();", nextBn)
                        else:
                            print('no valid album find')
                        sleep()
                        act.send_keys(Keys.ESCAPE).perform()
                        sleep(5)

            except Exception as e:#done /3
                print('no album img or error:',e)    

            print('looking for all single imgs')
            try:
                img=bot.find_elements(By.XPATH,X.imgs)
                if img :
                    for i in img:
                        act.scroll_to_element(i).perform()
                        sleep(5)
                        bot.execute_script("arguments[0].click();", i)
                        sleep()
                        db=bot.find_element(By.XPATH,X.downloadButton)
                        bot.execute_script("arguments[0].click();", db)
                        sleep()
                        act.send_keys(Keys.ESCAPE).perform()
                        sleep()

            except:
                print('no download button')
            print('looking for grop messages`')
            try:
                sleep()
                gText=bot.find_elements(By.XPATH,X.groptxt)
                if  gText:
                    filename=f"{name}_fromgGp.txt"
                    sleep()
                    print(len(gText),':texts found')
                    for i in gText:
                        act.move_to_element(i).perform()
                        sleep()
                        text=i.text
                     #   print(text)
                        with open(filename,'a',encoding='utf-8') as f:
                            f.write(text+'\n')

            except Exception as e:
                print('no grope text our error:',e)
            print('looking for single messages')
            
            try:
                sleep()
                sText=bot.find_elements(By.XPATH,X.shorttext)
                if sText:
                    print('short text find:',len(sText))
                    filename=f"{name}_fromgGp_short.txt"
                    print(len(sText),':texts found')
                    for i in sText:
                        act.move_to_element(i).perform()
                        sleep()
                        text=i.text
                    #    print(text)

                        with open(filename,'a',encoding='utf-8') as f:
                            f.write(text+'\n')
            except Exception as e:
                print('no short text our error:',e)
        except: 
            print('no message found')
      
        F.seek(name,f"{date.today().year}_{date.today().month}_{date.today().day}")
    chats = bot.find_elements(By.XPATH, X.chatPresent)
    ri.maketextFile()
    #sleep((2*60*60))# do seat sleep