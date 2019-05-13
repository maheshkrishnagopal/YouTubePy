"""
YouTube Views Booster v.0.1.1
---------------------

Python implementation for increasing the YouTube video's views with the help of the video's URL.

Amateur YouTubers are really struggling in getting the views for their videos in the video streaming app. To get rid of
it and to kick start a small learning project, this program has been created in a simplest way possible and will be
expanded in revealing the possibilities further.

This program is not a proper module to be deployed, which will require alot of updates to be a proper module. Moreover,
this snippet has a dependencies of Chrome Driver of Selenium.

The program is completely to explore the knowledge and not to monetize or being commercially used.

Author: Maheshkrishna A G
Email: maheshkrishnagopal@gmail.com
"""

import time
import datetime
import os
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options


def init_chrome_driver(driver_path):
    """
    This function will initiate the Chrome Driver taking the driver path as input, where the chromedriver.exe is 
    residing. Upon the initiation the driver is automated to navigate to the provided Youtube URL and will play the
    video which will increase the view.
    :param driver_path: directory path where the chromedriver.exe is residing.
    :return:
    """
    chrome_path = 'C:\\Users\\VAIO\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe'
    cwd = os.getcwd()
    window_size = "1920,1080"
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % window_size)
    chrome_options.add_argument("download.default_directory=" + cwd)
    chrome_options.add_argument('--disable-gpu')
    chrome_options.binary_location = chrome_path
    prefs = {'download.default_directory': cwd}
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
    # This command enables the chrome to download the file even in the headless mode.
    driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd': 'Page.setDownloadBehavior',
                   'params': {'behavior': 'allow', 'downloadPath': cwd}}
    driver.execute("send_command", params)
    driver.get('http://www.youtube.com/watch?v=eU8-nu4BHoI')
    play_button = driver.find_element_by_xpath('//*[@id="movie_player"]/div[4]/button')
    play_button_class = driver.find_elements_by_class_name('ytp-large-play-button.ytp-button')
    play_button.click()
    # play_button_class.click()
    time.sleep(900)
    driver.close()


if __name__ == "__main__":
    driver_path = os.getcwd() + '\\chromedriver.exe'
    init_chrome_driver(driver_path)
