# Sending SMS
# we import the Twilio client from the dependency we just installed
from twilio.rest import Client

def sendSms(phone_number,message):
    
    # the following line needs your Twilio Account SID and Auth Token
    client = Client("ACe1524097b8317d2b99cf180ddf68d6eb", "9cce5f85cc1902d76ce63a3be04214f7")
    
    # change the "from_" number to your Twilio number and the "to" number
    # to the phone number you signed up for Twilio with, or upgrade your
    # account to send SMS to any phone number
    PhoneNum = ["+916304602370", "+919381438985"]
    for num in PhoneNum:
        client.messages.create(to = num, 
                           from_ = "+12707516966", 
                           body = message)
    
    print("Message Sent")

