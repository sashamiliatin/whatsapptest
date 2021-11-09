from pyppeteer import browser, launch, page
from pyppeteer.browser import Browser
from pyppeteer.page import Page
import asyncio
import time
class Whatsapp:
    def __init__(self, browser: Browser) -> None:
        self.browser = browser

    async def sendMessage(self,message,contact):
        #browser = await launch({'headless': False,'userDataDir': './myUserDataDir'})
        page = await self.browser.newPage()
        await page.setUserAgent('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3542.0 Safari/537.36')
        await page.goto('https://web.whatsapp.com/')
        await page.screenshot({'path': 'web.png'})
        await page.waitForSelector('#pane-side')
        #await asyncio.sleep(30)
        await page.type('[role=textbox]',contact)
        await page.keyboard.press('Enter')
        await asyncio.sleep(2)
        await asyncio.sleep(2)
        await page.keyboard.type(message)
        await asyncio.sleep(2)
        await page.keyboard.press('Enter')
        return page


    async def receiveMessage(self, message, contact, page):
        # await page.waitForSelector('#pane-side')
        # await page.type('[role=textbox]',contact)
        # await page.keyboard.press('Enter')
        # await asyncio.sleep(1)
        element = await page.querySelectorAll('._1Gy50')
        answere = await page.evaluate('(element) => element.textContent', element[-1])
        if answere in message:
            return True
        else:return False