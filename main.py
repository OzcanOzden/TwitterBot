import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

#global tanımlamalar
url = "https://twitter.com/i/flow/login"
tweet_url = "https://twitter.com/compose/tweet"
mail_address = "Buraya Mail adresin"
username_address = "Buraya username"
password_address = "Buraya da şifre"
tweet = "Bu tweet python botu tarafından yollanmıştır!"

#Windows işletim sisteminde, Chrome argümanı için Chrome uygulaması yolunu .exe olarak kopyala?
driver = webdriver.Chrome()
driver.get(url)

#ara ara böyle yüklenmesini beklemek için sleep atıyorum, internetim bok
time.sleep(random.randint(7, 10))

#Login ekranını açtığımıza göre mail ve şifre girebiliriz, seçelim;

#mail
mail = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
mail.send_keys(mail_address)
#tıkla
next = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div")
next.click()
time.sleep(random.randint(2,5))

#username
username = driver.find_element(By.TAG_NAME, "input")
username.send_keys(username_address)
#tıkla
next_again = driver.find_element(By.XPATH, "//div[@data-testid='ocfEnterTextNextButton']")
next_again.click()
time.sleep(random.randint(2, 4))

#şifre
password = driver.find_element(By.XPATH, "//input[@name='password']")
password.send_keys(password_address)
#tıkla
giris_yap = driver.find_element(By.XPATH, "//div[@data-testid='LoginForm_Login_Button']")
giris_yap.click()
time.sleep(random.randint(5, 8))

#tweet yaz
driver.get(tweet_url)
time.sleep(random.randint(5, 8))
tweet_yaz = driver.find_element(By.XPATH, "//div[contains(@class, 'public-DraftStyleDefault-block')]")
tweet_yaz.send_keys(tweet)

#tweeti gönder
tweet_gonder = driver.find_element(By.XPATH, "//div[@data-testid='tweetButton']")
tweet_gonder.click()


time.sleep(5)




