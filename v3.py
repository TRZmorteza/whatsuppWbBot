from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from datetime import date
import fileMover as F
import xpath as X
import time
import os

# Configure Chrome options
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    "download.default_directory": os.getcwd(),
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
})
options.add_argument("user-data-dir=C:/Users/Administrator/AppData/Local/Google/Chrome/User Data/seleniumprofile")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

todayDate=date.today().day
def extract_number(input):
    words = input.split()
    if int(words[2]): 
        return int(words[2]) - int(words[0])
    else:
        return -1

# Function to sleep for a specified number of seconds
def sleep(s=3):
    time.sleep(s)

# Initialize ActionChains and WebDriver
def esc():
    act.send_keys(Keys.ESCAPE).perform()

bot = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
act = ActionChains(bot)
bot.get('https://web.whatsapp.com')

sleep(10)

# Find chat elements
chats = bot.find_elements(By.XPATH, X.chatPresent)

while True:
        users=[]
        with open('users.txt','r')as user:
            users = [line.strip() for line in user]

        wait = WebDriverWait(bot,60*60*60*5 , poll_frequency=0.5, ignored_exceptions=[Exception])
        trget = wait.until(EC.visibility_of_element_located((By.XPATH, X.unRead)))
        act.scroll_to_element(trget).perform()
       
        sleep()
        trget.click()
        sleep(5)
        try:
            gText = bot.find_elements(By.XPATH, X.groptxt)
            print('messages',len(gText))
        except:
            print('no message....')
        try:
            album = bot.find_elements(By.XPATH, X.albumImg)
            print('album',len(album))
        except:
            print('no album....')
        try:
            img = bot.find_elements(By.XPATH, X.imgs)
            print('img',len(img))
        except:
            print('no img....')
 

        print('TRYING TO CLICK')
        sleep()
        name = bot.find_element(By.XPATH, X.chatName).text


        if name in users or True:
            try:
                today = bot.find_element(By.XPATH, X.today)
                act.scroll_to_element(today).perform()
                sleep(6)
                try:
                    sleep()
                    
                    print(len(gText))
                    if gText:
                        filename = f"{name}_fromgGp.txt"
                        sleep()
                        
                        for index,i in enumerate(gText):
                            act.move_to_element(i).perform()
                            try:
                                readMores=bot.find_element(By.XPATH,X.readmore)
                                act.scroll_to_element(readMores).perform()

                                bot.execute_script("arguments[0].click();", readMores)
                            except:
                                print('no read more..')
                            sleep()
                            text = i.text
                            with open(filename, 'a', encoding='utf-8') as f:
                                f.write(text + '\n')
                            
                        
                except Exception as e:
                    print('no group text or error:', e)
               

                try:
                    preloads = bot.find_elements(By.XPATH, X.preLoad)
                    for preload in preloads:
                        act.scroll_to_element(preload).perform()
                        sleep(6)
                        
                        print('looking for download icon')
                        if preload:
                            bot.execute_script("arguments[0].click();", preload)
                            print('click on element')
                            sleep(10) 
                except:
                    print('no download button')
                    print('looking for album')
                try:
                    album = bot.find_elements(By.XPATH, X.albumImg)
                    act.scroll_to_element(album[0]).perform()
                    sleep(6)
                    print('album found:', len(album))
                    
                    if album:    
                        for i in album:
                            print('trying to click')
                            act.move_to_element(i).perform()
                            sleep(5)
                            i.click()
                            sleep(5)
                            lenOfAlbum = bot.find_element(By.XPATH, X.lenOfImgs).text
                            le = extract_number(lenOfAlbum)
                            if le != -1:
                                nextBn = bot.find_element(By.XPATH, X.nextButton)
                                menuBn = bot.find_element(By.XPATH, X.downloadMenu)

                                for i in range(0, le+1):
                                    sleep(5)
                                    bot.execute_script("arguments[0].click();", menuBn)
                                    sleep()
                                    try:
                                        dtap = bot.find_element(By.XPATH, X.downloadTab)
                                        bot.execute_script("arguments[0].click();", dtap)
                                    except:
                                        db = bot.find_element(By.XPATH, X.downloadButton)
                                        bot.execute_script("arguments[0].click();", db)
                                    sleep()
                                    bot.execute_script("arguments[0].click();", nextBn)
                            else:
                                print('no valid album find')
                            sleep()
                            act.send_keys(Keys.ESCAPE).perform()
                            sleep(5)

                except Exception as e:
                    print('no album img or error:', e)    

                print('looking for all single imgs')
                try:
                    
                    if img :
                        for i in img:
                            act.scroll_to_element(i).perform()
                            sleep(5)
                            bot.execute_script("arguments[0].click();", i)
                            sleep()
                            db = bot.find_element(By.XPATH, X.downloadButton)
                            bot.execute_script("arguments[0].click();", db)
                            sleep()
                            act.send_keys(Keys.ESCAPE).perform()
                            sleep()

                except:
                    print('no download button')
                print('looking for group messages')
                
                
            except: 
                print('no message found')

        else:
            print('skipping WhatsApp')
        if todayDate==date.today().day:
            pass
        else:
            todayDate=F.notToDay(date.today().day,f"{date.today().year}-{date.today().month}-{date.today().day}")
            
        F.seek(name, f"{date.today().year}_{date.today().month}_{date.today().day}")
        
        esc()
        #readd.readd(os.path.join(os.getcwd(),'tempRead'))
        # chats = bot.find_elements(By.XPATH, X.chatPresent)
       
