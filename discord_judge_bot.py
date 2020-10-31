import discord
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

token = 'insert your token'
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('RTFC'):
        await message.channel.send('Im Working on it, calm down')
        card = message.content.replace('RTFC', '')
        bot = webdriver.Firefox()
        bot.get('https://scryfall.com/')
        time.sleep(3)
        search = bot.find_element_by_id("q")
        search.clear
        search.send_keys(card)
        search.send_keys(Keys.RETURN)
        time.sleep(3)
        oracle = bot.find_element_by_class_name("card-text-oracle")
        await message.channel.send(oracle.text)
        bot.close()

    if message.content.startswith('JUDGE'):
        await message.channel.send('Im Working on it, calm down')
        card = message.content.replace('JUDGE', '')
        bot = webdriver.Firefox()
        bot.get('https://scryfall.com/')
        time.sleep(3)
        search = bot.find_element_by_id("q")
        search.clear
        search.send_keys(card)
        search.send_keys(Keys.RETURN)
        time.sleep(3)
        judge = bot.find_elements_by_class_name("rulings-item")
        for rule in judge:
            await message.channel.send(rule.text)
        bot.close()





client.run(token)
