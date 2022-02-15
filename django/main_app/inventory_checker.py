from .send_mail import *
import requests
from .models import *
from allauth import *
import json
import threading
def product_name(data):
    print(data)
    return data

def check(amount, url, product_name, email):
    print('we are checking the website!')
    r = requests.post("http://miniprojectuwu.ngrok.io/check",
                      data={'data': url})
    soldout = 'Sold out'
    json_text = r.json()
    
    if amount != 2:
        amount += 1
        if json_text['text'] == soldout and amount == 1:
            sendMail(email, 'New Request from "Is It in Stock?"',
                     f"Sup, \n You currently placed a query in our app, for '{product_name}' from target.com, We'll check it for 24 hours. \n If that was not you contact us.  ")
        elif json_text['text'] != soldout and amount == 1:
            amount = 5
            sendMail(email, 'New Request from "Is It in Stock?"',
                     f'Sup, \n You currently placed a query in our app, for "{product_name}" from target.com. \nHowever, this request failed. Please, try again and make sure that the item is it actually "Sold out". Thanks, \n If that was not you contact us.')
        elif json_text['text'] != 'Sold out' and amount != 1:
            sendMail(email, 'Hey your Item from "Is It in Stock?"',
                     f'Sup, \n Do you remember {product_name}, good news. It is in stock!. \n You can go and buy it here {url}. \n Please take a second and rate this query! :D')
        threading.Timer(60.0, check, args=[
                        amount, url, product_name, email]).start()
    else:
        sendMail(email, 'Hey your Item from "Is It in Stock?"',
                 f'Sup, \n Do you remember {product_name}, the query you placed expired. \n Please go back to our website and place the query again!')
        
    return json_text['product_name']

def check_p(url):
    print('we are checking the product name!')
    r = requests.post("http://miniprojectuwu.ngrok.io/check_p",
                      data={'data': url})
    json_text = r.json()
    print(json_text)
    return json_text