#import test_whatsapp 
from os import error, wait

from pyppeteer.launcher import executablePath
from test_whatsapp import *
import test_whatsapp
#import test_whatsapp


async def main():
    waitingMeseges =['Без проблем - Це може зайняти декілька хвилин...','Буде зроблено - Це може зайняти декілька хвилин...','Я працюю над цим - Це може зайняти декілька хвилин...','Звичайно - Це може зайняти декілька хвилин...']
    browser = await launch({'headless':True,'userDataDir': './myUserDataDir'})
    whatsapp = Whatsapp(browser) 
    page = await whatsapp.sendMessage(contact = 'DevOps-PRD', message = 'show me aiola greeting world')
    result = await whatsapp.receiveMessage(contact='DevOps-PRD',message=waitingMeseges, page=page)

    while not result:
        result = await whatsapp.receiveMessage(contact='DevOps-PRD',message=waitingMeseges, page=page)
    print(result)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())