from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("user-data-dir=C:/Users/MortezaNoei/AppData/Local/Google/Chrome/User Data/selenium_chrome_profile")

# Initialize the webdriver with the saved profile
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Navigate to the website (optional, as the previous session's tabs should still be open)
driver.get("https://web.whatsapp.com/")

input()
driver.quit()
