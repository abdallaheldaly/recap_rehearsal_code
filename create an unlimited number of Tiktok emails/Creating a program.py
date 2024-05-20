#Create a program for which I enter a valid number and it creates personal accounts for me with the same number as the valid number that I entered for it on Facebook, TikTok or Instagram.

# $ pip install selenium
# $ pip install webdriver-manager

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import time

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

class Bot:
    def __init__(self, username, password, users, message):
        self.username = username
        self.password = password
        self.users = users
        self.message = message
        self.bot = driver

    def login(self):
        self.bot.get('https://www.instagram.com/accounts/login/')
        time.sleep(2)

        username_field = WebDriverWait(self.bot, 10).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        password_field = WebDriverWait(self.bot, 10).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )

        username_field.send_keys(self.username)
        password_field.send_keys(self.password)
        password_field.submit()

        time.sleep(5)

        self.bot.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button').click()
        time.sleep(5)

    def send_messages(self):
        for user in self.users:
            self.bot.get('https://www.instagram.com/direct/new/')
            time.sleep(2)

            search_box = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-label="Search"]'))
            )
            search_box.send_keys(user)
            time.sleep(2)

            search_result = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/' + user + '"]'))
            )
            search_result.click()

            message_box = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea[aria-label="Message"]'))
            )
            message_box.send_keys(self.message)
            message_box.send_keys(Keys.RETURN)

            time.sleep(2)

if __name__ == '__main__':
    bot = Bot('your_username', 'your_password', ['user1', 'user2', 'user3'], 'Hello!')
    bot.login()
    bot.send_messages()














# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# # Initialize the Firefox WebDriver
# driver = webdriver.Firefox()

# def create_account(email, username, password):
#     # Navigate to the website's sign-up page
#     driver.get('https://www.facebook.com/r.php')

#     # Fill in the email field
#     email_field = driver.find_element(By.NAME, 'email')
#     email_field.send_keys(email)

#     # Fill in the username field
#     username_field = driver.find_element(By.NAME, 'username')
#     username_field.send_keys(username)

#     # Fill in the password field
#     password_field = driver.find_element(By.NAME, 'password')
#     password_field.send_keys(password)

#     # Submit the form
#     password_field.send_keys(Keys.RETURN)

#     # Wait for a few seconds to ensure the form is submitted
#     time.sleep(5)

# def post_comment(comment):
#     # Navigate to the website's post/comment page
#     driver.get('https://www.example.com/post')

#     # Fill in the comment field
#     comment_field = driver.find_element(By.NAME, 'comment')
#     comment_field.send_keys(comment)

#     # Submit the comment
#     comment_field.send_keys(Keys.RETURN)

#     # Wait for a few seconds to ensure the comment is posted
#     time.sleep(5)

# def create_accounts_and_post_comments(account_data, comments):
#     for data in account_data:
#         email = data['email']
#         username = data['username']
#         password = data['password']
#         create_account(email, username, password)
#         for comment in comments:
#             post_comment(comment)

# # Example usage
# account_data = [
#     {'email': 'test1@example.com', 'username': 'testuser1', 'password': 'YourSecurePassword'},
#     {'email': 'test2@example.com', 'username': 'testuser2', 'password': 'YourSecurePassword'},
#     {'email': 'test3@example.com', 'username': 'testuser3', 'password': 'YourSecurePassword'}
# ]

# comments = ['This is a test comment 1', 'This is a test comment 2', 'This is a test comment 3']

# # Create accounts and post comments
# create_accounts_and_post_comments(account_data, comments)

# # Close the driver
# driver.quit()















# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# # Initialize the Firefox WebDriver
# driver = webdriver.Firefox()

# def create_account(email, username, password):
#     # Navigate to the website's sign-up page
#     driver.get('https://www.tiktok.com/signup')

#     # Fill in the email field
#     email_field = driver.find_element(By.NAME, 'email')
#     email_field.send_keys(email)

#     # Fill in the username field
#     username_field = driver.find_element(By.NAME, 'username')
#     username_field.send_keys(username)

#     # Fill in the password field
#     password_field = driver.find_element(By.NAME, 'password')
#     password_field.send_keys(password)

#     # Submit the form
#     password_field.send_keys(Keys.RETURN)

#     # Wait for a few seconds to ensure the form is submitted
#     time.sleep(5)

# def post_comment(comment):
#     # Navigate to the website's post/comment page
#     driver.get('https://www.tiktok.com/')

#     # Fill in the comment field
#     comment_field = driver.find_element(By.NAME, 'comment')
#     comment_field.send_keys(comment)

#     # Submit the comment
#     comment_field.send_keys(Keys.RETURN)

#     # Wait for a few seconds to ensure the comment is posted
#     time.sleep(5)

# # Example usage
# emails = ['test1@example.com', 'test2@example.com', 'test3@example.com']
# usernames = ['testuser1', 'testuser2', 'testuser3']
# password = 'YourSecurePassword'
# comments = ['This is a test comment 1', 'This is a test comment 2', 'This is a test comment 3']

# # Create accounts and post comments
# for email, username in zip(emails, usernames):
#     create_account(email, username, password)
#     post_comment(comments.pop(0))

# # Close the driver
# driver.quit()

