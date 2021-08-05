from flask import Flask, request
import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=chrome_options)

app = Flask('')

@app.route('/')
def g_home():
    return "Hello"


@app.route('/check', methods=['POST'])
def checks():
    driver.get(request.form['data'])
    find = driver.find_element_by_css_selector('.h-text-orangeDark')
    result = find.text
    return result
       
    
def run():
    app.run(host='localhost',port=3000, debug=True)

run()
