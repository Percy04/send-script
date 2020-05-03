from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


class Annoy:
    def __init__(self, username, password):
        """Creates an instance of the Annoy class

        Args:
            username:str: The username of the user
            password:str: The password of the user
        """
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def login(self):
        """
        Logs a user into Instagram via the web portal
        """
        self.driver.get("https://www.instagram.com/")
        sleep(2)

        username_path = "//input[@name=\"username\"]"
        password_path = "//input[@name=\"password\"]"

        self.driver.find_element_by_xpath(username_path).send_keys(self.username)
        self.driver.find_element_by_xpath(password_path).send_keys(self.password)

        log_in_path = "//button[@type='submit']"
        self.driver.find_element_by_xpath(log_in_path).click()
        sleep(3)

        not_now_path = "//button[@class='aOOlW   HoLwm ']"
        self.driver.find_element_by_xpath(not_now_path).click()
        sleep(2)

    def enter_inbox(self, target_user):
        """
        Enters the Inbox and selects the specified user

        Args:
            target_user:str: The username of the person you want to send the movie script
        """
        driver = self.driver

        # Enters the inbox
        inbox = driver.find_element_by_class_name("xWeGp")
        inbox.click()
        sleep(2)

        # Clicks on the send message button
        send_message = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/button")
        send_message.click()
        sleep(2)

        # Searching for the target username specified
        find_user_area = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[1]/div/div[2]/input")
        find_user_area.send_keys(target_user)
        sleep(2)

        driver.find_element_by_class_name("dCJp8 ").click()

        driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/div/button").click()
        sleep(4)

    def send_script(self, script):
        """This function send each word of the script to the target user

            Args:
                script:str: The name of the downloaded script
        """
        driver = self.driver

        text_area = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/"
                                                 "div[2]/div/div[2]/div/div/div[2]/textarea")

        # Opens the movie script to send the words
        with open(script, 'r') as file:
        	
            # Sends the movie script word by word to the target user
            for words in file.read().split(" "):
                text_area.send_keys(words)
                text_area.send_keys(Keys.ENTER)


if __name__ == '__main__':
    a = Annoy("", "")
    a.login()
    a.enter_inbox("")
    a.send_script("Shrek script.txt")  # I have put shrek and aladdin movie script. SO if you wanna change that then
    # just download the new script and change the name present in ("Shrek script.txt") to the name of the script you
    # downloaded"
