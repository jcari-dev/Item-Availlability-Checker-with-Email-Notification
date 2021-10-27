
# Item Availability Checker with Email Notification

Made one full stack application using Django and PostgreSQL, that allows registered users to check for out-of-stock items in a supported websites.
The users are limited of only one request per week (can easily be changed), when a request is in place and validated a request is send to the server running on the Raspberry Pi and using Selenium a headless version of Chromium is used to open the check for the item requested by the user.  

The users request (along with more information) and email is stored in the database using PostgreSQL. This is with the purpose to run validations and check for usage timers.
## Features

- Account Creation using Google login
- Request History
- Email Notification
- Request Validation
- Support to various websites



## Tech Stack

**Web App  | Front/End**: Django / PostgreSQL

**On Pi**: Flask / Ngrok / Selenium

