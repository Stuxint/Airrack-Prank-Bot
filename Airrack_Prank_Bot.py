#--------------MADE BOT WHICH SENDS GIF TO RICK ROLL AIRRACK!!!!!!!----------------------------------

import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import random
import os
import pyautogui

web = uc.Chrome()
web.get("https://docs.google.com/document/u/0/")

#--------RANDOMIZING PART----------------------
names1 = ['peter', 'john', 'james', 'andrew', 'vladmir', 'James', 'Michael',
          'Anthony','Nathan','Adam','Henry','Zachary',
          'Douglas','Arthur', 'Bruce', 'Elijah', 'Alan','Juan', 'Liam']

names2 = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 
          'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 
          'Thompson', 'Garcia', 'Martinez', 'Robinson', 'Clark', 'Rodriguez', 'Lewis', 'Lee', 
          'Walker', 'Hall', 'Allen', 'Young', 'Hernandez',]

phone = ['9123 4567', '9987 6543', '9654 3210', '9345 6789', '9876 5432', '9567 8901', '9432 1098', '9789 0123', '9234 5678', '9012 3456', '7123 4567']

thing = ['felix.fizzlebottom@cosmiccupcake.com', 'poppy.moonbeam@gigglemail.net', 'barnaby.whiskers@fantastichat.com', 
         'penny.pumpernickel@bouncycastle.co', 'zara.zingzing@wizardsguild.io', 'arthur.gigglesworth@superduper.net', 
         'seraphina.sparkle@laughingllama.com', 'milo.buttercup@goofygoose.io', 'luna.lovesong@rainbowrabbit.net', 
         'oliver.oatmeal@mysticmuffin.com', 'chloe.cuddlesworth@happyhippo.io', 'sebastian.sprinkles@sunnyday.co', ]

f_name = random.choice(names1)
l_name = random.choice(names2)
number = random.choice(phone)
address = random.choice(thing)
#--------LOGIN IN PART----------------------

usern = web.find_element('xpath', '//*[@id="identifierId"]')
usern.send_keys('Your Gmail Address')
usern.send_keys(Keys.ENTER)

passw= WebDriverWait(web, 10).until(
                EC.presence_of_element_located(('xpath', '//*[@id="password"]/div[1]/div/div[1]/input'))
            )
passw.send_keys('Your Password')
passw.send_keys(Keys.ENTER)

#--------CREATING PART----------------------
create= WebDriverWait(web, 20).until(
                EC.presence_of_element_located(('xpath', '//*[@id=":1i"]/div[1]/img'))
            )
create.click()

time.sleep(5)

actions = ActionChains(web)

#1. Center text
actions.key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys('e').key_up(Keys.CONTROL).key_up(Keys.SHIFT).perform()

#2. Increase font(x5)
for x in range(5):
    actions.key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys('.').key_up(Keys.CONTROL).key_up(Keys.SHIFT).perform()

#3. Write text
actions.send_keys(f'Sorry, but if you are reading this, you sadly made the stupid mistake of being rick-rolled.\nSo enjoy, cry and look stupid, and tell Airrack Illuseum says hi. Anyway, see ya suckers!').perform()


#4. Add emojis
for x in range(2):
    actions.send_keys(Keys.ENTER).perform()

for x in range(2):
   actions.send_keys(":laughing").perform()
   time.sleep(0.5)
   actions.send_keys(Keys.TAB).perform()
   time.sleep(0.5)


for x in range(2):
    actions.send_keys(":imp-frown").perform()
    time.sleep(0.5)
    actions.send_keys(Keys.TAB).perform()
    time.sleep(0.5)

#5. Inserting Image
for x in range(2):
    actions.send_keys(Keys.ENTER).perform()

actions.key_down(Keys.ALT).send_keys('/').key_up(Keys.ALT).perform()

time.sleep(2)
actions.send_keys("Insert image using URL").perform()
time.sleep(1)
actions.send_keys(Keys.ENTER).perform()


time.sleep(2)
actions.send_keys("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExbzQ5dGN5bG16cGU1bXVtNTB3amhzbmFzeDV6YzZjZ2xlZzVtYjU0YyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/g7GKcSzwQfugw/giphy.gif").perform()
actions.send_keys(Keys.ENTER).perform()
time.sleep(1)
for x in range(3):
    actions.send_keys(Keys.TAB).perform()
    time.sleep(0.001)
actions.send_keys(Keys.ENTER).perform()

time.sleep(2)
for x in range(3):
    actions.key_down(Keys.CONTROL).send_keys('-').key_up(Keys.CONTROL).perform()


actions.key_down(Keys.ALT).send_keys('/').key_up(Keys.ALT).perform()
time.sleep(2)
actions.send_keys("Download as Microsoft Word").perform()
time.sleep(1)
actions.send_keys(Keys.ENTER).perform()
#--------APPLYING PART----------------------
time.sleep(5)
web.get('https://apply.workable.com/airrack/j/FEBA4FBE34/apply/')

#Decline cookies
time.sleep(3)
decline = web.find_element('xpath', '//*[@id="app"]/div/div/div[2]/div[2]/div/div/button[2]')
decline.click()

#First and last names
first = WebDriverWait(web, 10).until(
                EC.presence_of_element_located(('xpath', '//*[@id="firstname"]'))
)
first.send_keys(f'{f_name}')

second = WebDriverWait(web, 10).until(
                EC.presence_of_element_located(('xpath', '//*[@id="lastname"]'))
)
second.send_keys(f'{l_name}')

#Email address
email = WebDriverWait(web, 10).until(
                EC.presence_of_element_located(('xpath', '//*[@id="email"]'))
)
email.send_keys(f'{address}')

#Phone Number
number2 = WebDriverWait(web, 10).until(
                EC.presence_of_element_located(('xpath', '//*[@id="app"]/div/div/div/main/form/section[1]/div[2]/div[5]/label/div/div/div/div/input'))
)
number2.send_keys(f'{number}')

#Uploading file part
for x in range(8):
    actions.send_keys(Keys.TAB).perform()
actions.send_keys(Keys.ENTER).perform()

time.sleep(3)
file_path = os.path.abspath("Path to Google Docs")
pyautogui.typewrite(f'{file_path}')
pyautogui.hotkey('enter')

#Submitting it
time.sleep(5)
actions.send_keys(Keys.TAB).perform()
actions.send_keys(Keys.ENTER).perform()


time.sleep(30)