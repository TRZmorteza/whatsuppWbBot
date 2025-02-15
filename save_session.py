from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
if os.path.isdir('C:/Users/Administrator/AppData/Local/Google/Chrome/User Data/seleniumprofile_wt'):
    pass
else:
    os.makedirs(r'C:/Users/Administrator/AppData/Local/Google/Chrome/User Data/seleniumprofile_wt', exist_ok=True)
try:
    chrome_options = Options()
    chrome_options.add_argument("user-data-dir=C:/Users/Administrator/AppData/Local/Google/Chrome/User Data/seleniumprofile_wt")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--remote-debugging-port=9222")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    driver.get("https://web.whatsapp.com/")
    print("Successfully opened Google")
except Exception as e:
    print(f"An error occurred: {str(e)}")
finally:
        input()
        driver.quit()
