from lxml import html
from twilio.rest import Client
import requests
import time

# url of Ebay seller's store
page = requests.get('https://www.ebay.ca/sch/indiestartup/m.html?_nkw=&_armrs=1&_ipg=&_from=')
tree = html.fromstring(page.content)

# list where we save items we already know about
items_list = []

# Twilio credentials
account_sid = 'AC854b91ea15ddb0552b5fbff4de2827e6'
auth_token = 'TWILIO_TOKEN'
client = Client(account_sid, auth_token)

while True:
  # xpath of html element containing items being sold
  items = tree.xpath('//a[@class="vip"]/text()')
  for i in items:
    # Check if it's a new item and search for "11" for iPhone 11
    if i not in items_list and "11" in i:
      # Send me a text
      message = client.messages.create(body=items, from_='+15149006687', to='+15149963923')
    # save item
    items_list.append(i)
  time.sleep(60)