import requests  #talk to website
from bs4 import BeautifulSoup as bs  #scrape the table
import pandas as pd  # rewrite the table
from twilio.rest import Client  # text the table
import schedule #automate text message
import time #automate text message



# twilio info
account_sid = 'AC3925064efd87bcf1babad99605c5b095'
auth_token = '014e986fa3ee4bb87ea747d3fe02c9d3'
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
            from_='+16202209554',
             to='+13606096137'
         )

    print(message.sid)


schedule.every().day.at("08:00").do(scrape)

while True:
    schedule.run_pending()
    time.sleep(1)
