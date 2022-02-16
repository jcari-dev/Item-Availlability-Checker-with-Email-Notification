from .send_mail import *
import requests
from .models import *
from allauth import *
import json
import re
import threading
from email.mime.text import MIMEText

def product_name(data):
    print(data)
    return data


def check(amount, url, product_name, email):
    print('we are checking the website!')
    r = requests.post("http://miniprojectuwu.ngrok.io/check",
                      data={'data': url})
    soldout = 'Sold out'
    json_text = r.json()
    
    message = f'''<html>
  <body>
<p>Hey, this is an automated response from "Is It In Stock?".</p>
<p><img src="https://cdn.discordapp.com/attachments/303372529077321739/943296513587695656/JennieAmaAJorge1.png" alt="Happy Man" width="300" height="300" /></p>
<p>You just placed a query for ({product_name}) from <a href="https://www.target.com">Target.com</a> using our services. We will check the URL provided for 24 hours. You will be notified when the query expires and if the item becomes available.</p>
  </body>
</html>'''
    message_expired = f'''<html>
  <body>
<p>Hey, this is an automated response from "Is It In Stock?".</p>
<p><img src="https://cdn.discordapp.com/attachments/303372529077321739/943297801486475356/JennieAmaAJorge1_1.png" alt="expired" width="300" height="300" /></p>
<p>Your query for ({product_name}) from <a href="https://www.target.com">Target.com</a> expired. Please feel free to place another query in 24 hours.</p>
  </body>
</html>'''

    message_got_it = f'''<html>
  <body>
<p>Hey, this is an automated response from "Is It In Stock?".</p>
<p><img src="https://cdn.discordapp.com/attachments/303372529077321739/942941399454736524/seikou_banzai_man.png" alt="got it" width="300" height="300" /></p>
<p>Good news! {product_name}, it is in stock! Go get it <a href="{url}">HERE</a>!</p>
  </body>
</html>'''
    

    my_email = MIMEText(message, "html")    

    if amount != 2:
        amount += 1
        if json_text['text'] == soldout and amount == 1:
            sendMail(
                email, 'New Request from "Is It In Stock?"', message)
        elif json_text['text'] != soldout and amount == 1:
            amount = 5
            sendMail(
                email, 'New Request - "Is It in Stock?"',
                f'''Sup, \n You currently placed a query in our app, for "{product_name}" from target.com. \nHowever, this request failed. Please, try again and make sure that the item is it actually "Sold out". Thanks, \n If that was not you contact us.'''
            )
        elif json_text['text'] != 'Sold out' and amount != 1:
            sendMail(
                email, 'Hurry! Your Item Is Now Available! - "Is It in Stock?"', message_got_it)
        threading.Timer(60.0, check, args=[amount, url, product_name,
                                           email]).start()
    else:
        sendMail(
            email, 'Query Expired - "Is It in Stock?"', message_expired)

    return json_text['product_name']


def check_p(url):
    print('we are checking the product name!')
    r = requests.post("http://miniprojectuwu.ngrok.io/check_p",
                      data={'data': url})
    json_text = r.json()
    print(json_text, '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    return json_text


def clean_url(url):

    list_of_supported_websites = ['www.target.com']

    url_without_https = re.sub(r'https://', '', url)

    url_domain_name = re.sub(r'(com.*)', '', url_without_https)

    if url_domain_name + 'com' not in list_of_supported_websites:
        return False
    else:
        return True
