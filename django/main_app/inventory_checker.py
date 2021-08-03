from .send_mail import *
import requests
from .models import *
from allauth import *

def check(url, product_name, email):
    
    r = requests.post("http://miniprojectuwu.ngrok.io/check", data={'data': url})
    
    if r.text == 'Sold out':

        return sendMail(email, 'New Request from "Is It in Stock?"', f"Sup, \n You currently placed a query in our app, for '{product_name}' from target.com, We'll check it for 24 hours. \n If that was not you contact us.  ")

    else:
        
        return sendMail(email, 'New Request from "Is It in Stock?"', f'Sup, \n You currently placed a query in our app, for "{product_name}" from target.com. \nHowever, this request failed. Please, try again and make sure that the item is it actually "Sold out". Thanks, \n If that was not you contact us.')
    
