'''
    Selenium test code
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def main():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')      
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.set_window_size(1000,1000)
    
    driver.get('https://www.selenium.dev/')
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.TAG_NAME, 'h1'))
    )
    element = driver.find_element(By.CSS_SELECTOR, 'h1')
    print(element.text)


if __name__ == '__main__':
    main()
