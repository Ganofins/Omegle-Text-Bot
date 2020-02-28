#!/usr/bin/python3

import argparse
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

parser = argparse.ArgumentParser(description="Omegle text bot to send message automatically.")
parser.add_argument("-m", "--message", dest="message", type=str, required=True, help="Message text to send to the receiver")
parser.add_argument("-c", "--count", dest="count", type=int, default=3, help="Times you want to send this message to an individual receiver (default=3)")

args = parser.parse_args()

#arguments via terminal
message = args.message
times_count = args.count

#for maximizing the browser's window
options = Options()
options.add_argument("--start-maximized")
#options.headless = True

browser = webdriver.Chrome('./chromedriver', options=options)

try:
    browser.get("https://omegle.com")
    text_btn = browser.find_element_by_id("textbtn")
    text_btn.click()
except:
    exit("Internet not working")

#variable to compare the times a msg is sent to an individual receiver
count = 0

sleep(3)

while True:

    if count < times_count:
        sleep(4)
        chat_box = browser.find_element_by_css_selector("textarea.chatmsg")
        disconnect_btn = browser.find_element_by_css_selector("button.disconnectbtn")

        if "disabled" in chat_box.get_attribute("class"):
            sleep(3)
            if "disabled" in chat_box.get_attribute("class"):
                disconnect_btn.click()
                count = 0
            else:
                count = 0
                #stranger disconnects in between sending the message
                try:
                    chat_box.send_keys(message)
                    chat_box.send_keys(Keys.ENTER)
                except:
                    continue
                count = 1

        else:
            #stranger disconnects in between sending the message
            try:
                chat_box.send_keys(message)
                chat_box.send_keys(Keys.ENTER)
            except:
                continue
            count += 1
            sleep(4)
    
    else:
        browser.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)
        sleep(1)
        browser.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)
        count = 0
        