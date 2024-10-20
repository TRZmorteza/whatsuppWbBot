from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import os
from selenium.webdriver.common.keys import Keys
import time
import fileMover


chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": os.getcwd(),
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
})


XeButton="//span[@data-icon='x-viewer']"
XdButton="//span[@data-icon='download']"
xchatName="//div[@id='main']//div[@class='_amie']//span[@dir='auto']"
#nonAnXimg="//div[@role='application']//img[@src]"#temami img haye gorohaye be joz anjomen
nonAnXimg="//div[@role='application']//span[text()='TODAY']//following::img[@src]"#feget aks haye pain tag span emroz deryaft khohed shod
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://web.whatsapp.com")
basePath='C:\\xampp\\webdav'
input("Scan the QR code and press Enter after logging in on your phone...")
actions = ActionChains(driver)
chat_elements = driver.find_elements(By.XPATH, "//div[contains(@role,'listitem')]")
for chat in chat_elements:
    chat.click()
    time.sleep(2)  
    chatName=driver.find_element(By.XPATH,xchatName).text
    print(f'looking to {chatName}')
    
    time.sleep(2)  
    img_elements =driver.find_elements(By.XPATH, nonAnXimg)
    if  img_elements!=[]:
        print (f"img found in{chatName}")
        for index,img in enumerate(img_elements):
            try:    
                if img.is_displayed():
                    print(f"img is visibelin {chatName}")
                    time.sleep(5)
                    try:
                        driver.execute_script("arguments[0].scrollIntoView();", img)
                        img.click()
                        time.sleep(3)
                    except Exception as e:
                        print(f'connot click on the img retrying to get bak to chat{chatName}..')
                        actions.send_keys(Keys.ESCAPE).perform()
                        actions.send_keys(Keys.ESCAPE).perform()
                        chat.click()
                        try:
                            driver.execute_script("arguments[0].scrollIntoView();", img)
                            if img.is_displayed():
                                print('img is visibul again')
                                img.click()
                                driver.find_element(By.XPATH,XdButton).click
                                actions.send_keys(Keys.ESCAPE)
                        except Exception as e:
                            print('not hope for this')
                            
                    try:
                        driver.find_element(By.XPATH,XdButton).click()
                        time.sleep(3)
                        driver.find_element(By.XPATH,XeButton).click()
                    except Exception as e:
                        print("there is not a Dbutton...")
                        actions.send_keys(Keys.ESCAPE).perform()
                        chat.click()
                        print('sleep 5 .....')
                        time.sleep(5)
            except Exception as e:
                print('img is no longer visibel...')
                try:
                    time.sleep(5)
                    chat.click()
                    driver.execute_script("arguments[0].scrollIntoView();", img)
                except Exception:
                    print('cannot locate the img going to next chat..')
                    break
        else:
            print(f"no img found in {chatName} !!!!")
    fileMover.move(chatName,'403_7_28')