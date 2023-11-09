import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

#global tanımlamalar
url = "https://twitter.com/i/flow/login"
tweet_url = "https://twitter.com/compose/tweet"
tweet = "Bu tweet python botu tarafından yollanmıştır!"

mail_adresleri = [
    "mail1@outlook.com",
    "mail2@outlook.com"
]
usernames = [
    "username1",
    "username2"
]
şifreler = [
    "şifre1",
    "şifre2"
]

for i in range(len(mail_adresleri)):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(random.randint(7, 10))
    mail = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
    mail.send_keys(mail_adresleri[i])
    next = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div")
    next.click()
    time.sleep(random.randint(2, 5))
    username = driver.find_element(By.TAG_NAME, "input")
    username.send_keys(usernames[i])
    next_again = driver.find_element(By.XPATH, "//div[@data-testid='ocfEnterTextNextButton']")
    next_again.click()
    time.sleep(random.randint(2, 4))
    password = driver.find_element(By.XPATH, "//input[@name='password']")
    password.send_keys(şifreler[i])
    giris_yap = driver.find_element(By.XPATH, "//div[@data-testid='LoginForm_Login_Button']")
    giris_yap.click()
    time.sleep(random.randint(5, 8))
    driver.get(tweet_url)
    time.sleep(random.randint(5, 8))
    tweet_yaz = driver.find_element(By.XPATH, "//div[contains(@class, 'public-DraftStyleDefault-block')]")
    tweet_yaz.send_keys(tweet)
    tweet_gonder = driver.find_element(By.XPATH, "//div[@data-testid='tweetButton']")
    tweet_gonder.click()
    time.sleep(random.randint(3,5))
    log_out_menu = driver.find_element(By.XPATH, "//div[@aria-label='Account menu']")
    log_out_menu.click()
    time.sleep(1)
    log_out = driver.find_element(By.XPATH, "//div[@data-testid='AccountSwitcher_AddAccount_Button']")
    log_out.click()


time.sleep(5)




