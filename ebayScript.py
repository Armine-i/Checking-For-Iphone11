from lxml import html
from twilio.rest import Client
import requests

page = requests.get('https://www.ebay.ca/sch/indiestartup/m.html?_nkw=&_armrs=1&_ipg=&_from=')
tree = html.fromstring(page.content)

items = tree.xpath('//a[@class="vip"]/text()')

account_sid = 'AC854b91ea15ddb0552b5fbff4de2827e6'
auth_token = 'ce566dbf560fc70946bf5d08d0127b42'
client = Client(account_sid, auth_token)

while True:
  for i in items:
    if "11" in i:
      message = client.messages.create(body=items, from_='+15149006687', to='+15149963923')
