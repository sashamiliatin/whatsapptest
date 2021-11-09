from os import wait
from pyppeteer import browser, launch, page
import asyncio
import time
class SendMessageWhatsapp:
    async def sendMessage(self ,message,contact):
        browser = await launch({'headless': False,'userDataDir': './myUserDataDir'})
        page = await browser.newPage()
        await page.goto('https://web.whatsapp.com/')
        await page.waitForSelector('#pane-side')
        await page.type('[role=textbox]',contact)
        await page.keyboard.press('Enter')
        time.sleep(1)
        await page.keyboard.type(message)
        await page.keyboard.type('Enter')
        time.sleep(1)
        await browser.close()
