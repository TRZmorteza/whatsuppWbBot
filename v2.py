from selenium import webdriver
b=webdriver.Chrome()
b.get('https://web.whatsapp.com')
input()
import pickle
coookie=b.get_cookies()
pickle.dump(coookie,open('c.pkl','wb'))
