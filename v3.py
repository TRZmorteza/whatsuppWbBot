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
options.add_argument("user-data-dir=C:/Users/Administrator/AppData/Local/Google/Chrome/User Data/seleniumprofile_wt")
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

while True:
       
        sleep()
        wait = WebDriverWait(bot,60*60*60*5 , poll_frequency=0.5, ignored_exceptions=[Exception])
        trget = wait.until(EC.visibility_of_element_located((By.XPATH, X.unRead)))
        act.scroll_to_element(trget).perform()
       
        sleep()
        trget.click()
        sleep(5)
        try:
            gText = bot.find_elements(By.XPATH, X.unread_texts)
            print('messages',len(gText))
        except:
            print('no message....')
      
        try:
            img = bot.find_elements(By.XPATH, X.unread_imgs)
            print('img',len(img))
        except:
            print('no img....')
 

        print('TRYING TO CLICK')
        sleep()
        name = bot.find_element(By.XPATH, X.chatname).text


        
        try:
            try:
                with open(f'{name}.txt','a',encoding='utf-8') as f:
                    for i in gText:
                        act.scroll_to_element(i).perform()
                        if i.is_displayed():
                            text=i.text
                            f.write(text+'\n')

            except Exception as e:
                print('no message found')
                    
            
            

            

            print('looking for all single imgs')
            try:
                
                if img :
                    for i in img:
                        act.scroll_to_element(i).perform()
                        if i.is_displayed():
                            bot.execute_script("arguments[0].click();", i)
                            db=wait.until(EC.visibility_of_element_located((By.XPATH, X.download_button)))
                            bot.execute_script("arguments[0].click();", db)
                            sleep()
                            act.send_keys(Keys.ESCAPE).perform()
                            sleep()

            except:
                print('no download button')
            print('looking for group messages')
            
            
        except: 
            print('no message found')

      
        
            
        F.seek(name, f"{date.today().year}_{date.today().month}_{date.today().day}")
        print(f"last look chat :{name}\nfind imgs:{len(img)}\nfind texts as line:{len(gText)}" )
        esc()
        #readd.readd(os.path.join(os.getcwd(),'tempRead'))
        # chats = bot.find_elements(By.XPATH, X.chatPresent)
       
