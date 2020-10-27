import requests  #talk to website
from bs4 import BeautifulSoup as bs  #scrape the table
import pandas as pd  # rewrite the table
from twilio.rest import Client  # text the table
import schedule #automate text message
import time #automate text message



# twilio info
account_sid = 'insert account_sid'
auth_token = 'insert auth_token'
client = Client(account_sid, auth_token)


def scrape():
    #scraper brain
    response = requests.get("https://www.mtggoldfish.com/movers/paper/standard")
    soup = bs(response.text, "html.parser")

    #finds and sets up table
    table = soup.find_all('table')
    df = pd.read_html(str(table))[0]

    # makes it read able
    final = df.to_string()
    f_test = 'please work'

    #print(final)

    # text the table

    message = client.messages \
        .create(
            body=final,
            from_='+'from number'',
             to='+'to number''
         )

    print(message.sid)


schedule.every().day.at("08:00").do(scrape)

while True:
    schedule.run_pending()
    time.sleep(1)
