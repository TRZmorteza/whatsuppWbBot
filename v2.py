from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import fileMover
import time
import os
from datetime import date
print('bot is starting...')

chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": os.getcwd(),
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
})
print('options are looded...')

#XeButton="//span[@data-icon='x-viewer']"# i just use esc keys ;-)
#nonAnXimg="//div[@role='application']//img[@src]"#temami img haye gorohaye be joz anjomen// may be use full
XdButton="//span[@data-icon='download']"
xchatName="//div[@id='main']//div[@class='_amie']//span[@dir='auto']"
nonAnXimg="//div[@role='application']//span[text()='TODAY']//following::img[@src]"#feget aks haye pain tag span emroz deryaft khohed shod
XimgE="//div[@role='application']//span[text()='TODAY']//following::img[@style='width: 100%; height: 100%; object-fit: cover;']"
print('lunching the driver...')
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://web.whatsapp.com")
print('all set have nice debuggingyes')
basePath='C:\\xampp\\webdav'
input("Scan the QR code and press Enter after logging in on your phone...")
actions = ActionChains(driver)
chat_elements = driver.find_elements(By.XPATH, "//div[contains(@role,'listitem')]")
while True:
    for chat in chat_elements:
        chat.click()
        time.sleep(2)  
        chatName=driver.find_element(By.XPATH,xchatName).text
        print(f'looking to {chatName}')
        fileMover.make(chatName)
        time.sleep(4)  
        img_elements =driver.find_elements(By.XPATH, nonAnXimg)
        img_elemets_secXpath=driver.find_elements(By.XPATH,XimgE)
        if img_elemets_secXpath!=[]:
            print (f"img found in {chatName} its first method")
            for img in img_elemets_secXpath:
                print('trying to download img')
                try:
                    img.click()
                    if Db:=driver.find_element(By.XPATH,XdButton):
                        Db.click()
                        print('download secses full...')
                        fileMover.move(chatName,f"{date.today().year}_{date.today().month}_{date.today().day}")
                        print("exit the download manu..")
                    else:
                        print('no download button...')
                    actions.send_keys(Keys.ESCAPE).perform()
                except Exception as e:
                    print('some ting went wrong in secound xpath metod this is error: ',e)
                
        
        elif False and img_elements!=[]:
            print (f"img found in {chatName} secound method")
            for index,img in enumerate(img_elements):
                try:#try for displayed img    
                    if img.is_displayed():
                        time.sleep(5)
                        print(f"img is visibelin {chatName}")
                        try:
                            driver.execute_script("arguments[0].scrollIntoView();", img)
                            img.click()
                            time.sleep(3)
                        except Exception as e:

                            print(f'cannot click on the img retrying to get back to chat{chatName}..')
                            actions.send_keys(Keys.ESCAPE).perform()
                            time.sleep(2)
                            actions.send_keys(Keys.ESCAPE).perform()
                            time.sleep(2)
                            chat.click()
                            try:
                                driver.execute_script("arguments[0].scrollIntoView();", img)
                                if img.is_displayed():
                                    print('img is visibul again')
                                    img.click()
                                    driver.find_element(By.XPATH,XdButton).click()
                                    fileMover.move(chatName,f"{date.today().year}_{date.today().month}_{date.today().day}")
                                    actions.send_keys(Keys.ESCAPE)
                            except Exception as e:
                                print('not hope for this')
                                
                        try:
                            driver.find_element(By.XPATH,XdButton).click()
                            fileMover.move(chatName,f"{date.today().year}_{date.today().month}_{date.today().day}")
                            time.sleep(3)
                            actions.send_keys(Keys.ESCAPE).perform()
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
                        img.click()
                        driver.execute_script("arguments[0].scrollIntoView();", img)
                    except Exception:
                        print('cannot locate the img going to next chat..')
                        break
            else:
                print(f"no img found in {chatName} !!!!")
    time.sleep(120*60)
        
driver.close()