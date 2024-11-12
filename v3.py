from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import date
import fileMover as F
import xpath as X
import time
import os
import readd
# Configure Chrome options
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    "download.default_directory": os.getcwd(),
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
})
options.add_argument("user-data-dir=C:/Users/MortezaNoei/AppData/Local/Google/Chrome/User Data/selenium_chrome_profile")
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
    print('loading chats...')
    for chat in chats:
        chat.click()
        try:
            sleep()
            today = bot.find_element(By.XPATH, X.today)
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
        if name=="mortezanoee":
            try:
                print('admin found')
                textbBr=bot.find_element(By.XPATH,X.textBar)
                textbBr.click()
                
                textbBr.send_keys('running......')
                textbBr.send_keys(Keys.RETURN)
                continue
            except:
                print('something went wrong admin')
        F.make(name)
        print('Looking at:', name)
        if name != 'Whatsapp':
            try:
                today = bot.find_element(By.XPATH, X.today)
                act.scroll_to_element(today).perform()
                sleep(6)
                try:
                    sleep()
                    gText = bot.find_elements(By.XPATH, X.groptxt)
                    print(len(gText))
                    if gText:
                        filename = f"{name}_fromgGp.txt"
                        sleep()
                        
                        for i in gText:
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
                    preloads = bot.find_elements(By.XPATH, X.downloadButtonLoad)
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
                    album = bot.find_elements(By.XPATH, X.albumImg)
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
                    img = bot.find_elements(By.XPATH, X.imgs)
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
                
                F.seek(name, f"{date.today().year}_{date.today().month}_{date.today().day}")
                
            except: 
                print('no message found')

        else:
            print('skipping WhatsApp')
    if todayDate==date.today().day:
        pass
    else:
        todayDate=F.notToDay(date.today().day,f"{date.today().year}-{date.today().month}-{date.today().day}")
      
      
        
    
    readd.readd(os.path.join(os.getcwd(),'tempRead'))
    chats = bot.find_elements(By.XPATH, X.chatPresent)
    sleep(60*1)
