# import libraries
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

class IgBot():

    @classmethod
    def setUpClass(self):
        #specify the path to chromedriver.exe (download and save on your computer)
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        self.driver.maximize_window()
        #open the webpage
        self.driver.get("http://www.instagram.com")
        

    def cookies_alert(self):
        # accept cookies
        try:
            cookie_buttom = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/button[2]'))).click()
            # wait 3 seconds
            time.sleep(3)
        except:
            print("Error accepting cookies")


    def login(self):        
        #find fields
        username = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
        password = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

        #enter username and password
        username.clear()
        username.send_keys(username)
        password.clear()
        password.send_keys(password)

        time.sleep(2)

        #find login button and click it
        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()


    def alerts(self):
        time.sleep(5)
        # don't save login information
        try:
            alert = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/button'))).click()
        except:
            print("error refusing to save login information")
        # don't turn on notifications
        try:
            alert2 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]'))).click()
        except:
            print("error when denying to activate the notifications")


    def find_user(self):
        # search user or hashtag
        search_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/input"))).send_keys("username or hashtag")

        try:
            # xpath for users
            click_user = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div[1]/div/div/div[1]"))).click()
        except:
            # xpath for hashtags
            click_hashtag = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div[1]/div/div"))).click()


    def select_last_post(self):
        try:
            # xpath for post on user page
            click_on_post = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a"))).click()
        except:
            # xpath for post on hashtag page
            click_on_post = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a"))).click()


    def like_comment(self):
        # like and comment on the last 5 posts
        for i in range(5):
            # click on the like button
            like = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button"))).click()

            time.sleep(1)

            commentary = 'some commentary'

            # it is necessary to find and click the text area twice to enter the comment
            comment = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea")))
            comment.click()
            comment = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea")))
            comment.click()
            comment.send_keys(commentary)

            time.sleep(1)
            
            # click to post comment
            click_sumbit = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

            time.sleep(1)

            # click to go to the next post
            click_next = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button"))).click()

            time.sleep(2)

    @classmethod
    def teardownClass(self):
        print('closing the browser...')
        time.sleep(1)
        # close the browser
        self.driver.close()

if __name__ == "__main__":
    i = IgBot()
    i.setUpClass()
    i.cookies_alert()
    i.login()
    i.alerts()
    i.find_user()
    i.select_last_post()
    i.like_comment()
    i.teardownClass()
