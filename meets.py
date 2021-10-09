import json
import time
import asyncio
from pyppeteer import launch

with open('link.txt') as f:
    link=f.read()
with open('msg.txt') as f:
    msg=f.read()

async def run():
    browser = await launch(headless=False , slowMo = 20, executablePath='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',args=['--use-fake-ui-for-media-stream','--use-file-for-fake-video-capture'])

    page = await browser.newPage()
    await page.setViewport({ 'width': 1280, 'height': 800 })

    with open('mail.google.com.cookies.json') as data_file:
        data_loaded = json.load(data_file)

    for cookie in data_loaded:
        await page.setCookie(cookie)

    await page.goto(link,{'timeout':0,'waitUntil':'domcontentloaded'})

    await page.waitForXPath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div')
    mic_btn=await page.xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div')
    await mic_btn[0].click()

    cam_btn=await page.xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div')
    await cam_btn[0].click()

    join_btn=await page.xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span')
    await join_btn[0].click()

    # await page.waitFor(5000)
    time.sleep(5)

    chat_btn=await page.xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[10]/div[3]/div[2]/div/div/div[3]/span/button/i[1]')
    await chat_btn[0].click()

    await page.type('#ow3 > div.T4LgNb > div > div:nth-child(9) > div.crqnQb > div.R3Gmyc.qwU8Me > div.WUFI9b > div.hWX4r > div > div.BC4V9b > div > div.RpC4Ne.oJeWuf > div.Pc9Gce.Wic03c > textarea',msg)
    send_btn=await page.xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div[2]/div[2]/div/div[4]/span')
    await send_btn[0].click()

    await page.waitFor(10000)
    end_btn=await page.xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[10]/div[2]/div/div[7]/span/button')
    await end_btn[0].click()

    await page.waitFor(1000)
    await browser.close()

asyncio.get_event_loop().run_until_complete(run())