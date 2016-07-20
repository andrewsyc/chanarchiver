#!/usr/bin/env python

from selenium import webdriver


driver = webdriver.PhantomJS(executable_path='/root/anaconda2/bin/phantomjs') # or add to your PATH
driver.set_window_size(1024, 768) # optional
driver.get('https://google.com/')
driver.save_screenshot('screen.png') # save a screenshot to disk
sbtn = driver.find_element_by_css_selector('button.gbqfba')
sbtn.click()