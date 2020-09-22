import schedule as schedule
from selenium import webdriver
import sys, time, datetime

username = sys.argv[1]
password = sys.argv[2]
timeInput = sys.argv[3]


def do_browser():
    print("It's time!")
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=options)
    browser.get("https://lolesports.com")

    browser.implicitly_wait(10)
    
    browser.find_element_by_link_text("LOGIN").click()
    browser.find_element_by_name("username").send_keys(username)
    browser.find_element_by_name("password").send_keys(password)
    browser.find_element_by_xpath("/html/body/div/div/div/div[2]/div[1]/div/button").click()


schedule.every().day.at(timeInput).do(do_browser)

while True:
    print("Waiting for: " + timeInput)
    print("It is currently: " + str(datetime.datetime.now().time())[0:5])
    schedule.run_pending()
    time.sleep(60)

