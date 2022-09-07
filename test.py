'''
    Selenium test code
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# The container's built-in chromedriver path.
path_driver = '/opt/google/chrome/chromedriver'


def main():
    option = webdriver.ChromeOptions()
    option.add_argument('--no-sandbox')
    option.add_argument('--disable-dev-shm-usage')
    option.add_argument('--headless')
    option.add_argument('--disable-gpu')      
    
    driver = webdriver.Chrome(options=option, executable_path=path_driver)
    driver.set_window_size(1000,1000)
    
    driver.get('https://www.selenium.dev/')
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.TAG_NAME, 'h1'))
    )
    element = driver.find_element_by_tag_name('h1')
    print(element.text)


if __name__ == '__main__':
    main()
