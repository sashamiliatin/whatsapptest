from pyppeteer import browser, launch, page
import asyncio
import time
class ReceiveMessageWhatsapp:
    async def receiveMessage(selfe,message,contact):
        browser = await launch({'headless': False,'userDataDir': './myUserDataDir'})
        page = await browser.newPage()
        await page.goto('https://web.whatsapp.com/')
        await page.waitForSelector('#pane-side')
        await page.type('[role=textbox]',contact)
        await page.keyboard.press('Enter')
        time.sleep(1)
        element = await page.querySelectorAll('._1Gy50')
        answere = await page.evaluate('(element) => element.textContent', element[-1])
        await browser.close()
        if message == answere:
            return True
        else:return False