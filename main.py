import re
import time

from discord.ext import commands, tasks

from aiogram import Bot, types
from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils import executor
import requests

from config import TOKEN, PASSWORD

bot = Bot(token=TOKEN)

storage = MemoryStorage()
admin0 = [362837453, 297054806, 362032370, 547605427]
admin1 = [int]
admin2 = [int]
dp = Dispatcher(bot=bot, storage=storage)
urlList = ['https://sfedu.ru/www2/web/student/muam',
           #   'https://sfedu.ru/www/stat_pages15.show?p=LKS/enroll/D'
           ]
urlResultlist = []


class AdminSetClass(StatesGroup):
    otvet = State()


async def start():
    print("starting....")
    s = await login()
    await loadPages(s)

    print("started")
    return ""


async def loadPages(s: requests.session):
    for a in range(0, len(urlList)):
        res1 = s.get(urlList[a])
        res = res1.text
        print(urlList[a])
        print(res)
        print()
        print()
        print()
        urlResultlist.append(res)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    print("process_start_command started")
    await message.reply("Приветик")


@dp.message_handler(commands=['startServer'])
async def startingServer(query: types.CallbackQuery):
    if query.from_user.id == admin0[0]:
        await bot.send_message(query.from_user.id, "starting...")
        await start()
        await bot.send_message(query.from_user.id, "started")


@dp.message_handler(commands=['getId'])
async def notification_callback_handler(query: types.CallbackQuery):
    print("hands update. user: " + str(query.from_user.id))
    await bot.send_message(query.from_user.id, "Ваш id " + f"{query.from_user.id}")


@dp.message_handler(commands=['update'])
async def updating(query: types.CallbackQuery):
    if query.from_user.id == admin0[0]:
        await check()
        await bot.send_message(query.from_user.id, "ready")


@dp.message_handler(commands=['c'])
async def c(query: types.CallbackQuery):
    if query.from_user.id == admin0[0]:
        print("изменяем")
        print(str(urlResultlist[0]))
        urlResultlist[0] = ""


async def notifyAdmin0(s: str):
    # for a in admin0:
    # print("notify" + f" {a}")
    await bot.send_message(362837453, s)


@dp.message_handler(state=AdminSetClass.otvet)
async def getUrl(message: types.Message, state: FSMContext):
    print(message.text)
    await state.finish()


@dp.message_handler(commands=['help'])
async def help(query: types.CallbackQuery):
    answ = "/update вызывает ручное обновление\n/isAdmin проверка, являетесь ли вы админом\naddAdmin добавляет " \
           "администратора "
    await bot.send_message(query.from_user.id, answ)


@dp.message_handler(commands=['isAdmin'])
async def notification_callback_handler(query: types.CallbackQuery):
    answ = admin1.__contains__(query.from_user.id) or admin2.__contains__(query.from_user.id) or admin0.__contains__(
        query.from_user.id)
    await bot.send_message(query.from_user.id, str(answ))


@tasks.loop(minutes=10)
async def check():
    try:
        if len(urlResultlist) == 0:
            await start()
        time.sleep(20)
        print("updating...")
        s = await login()
        flag = await checkPages(s)
        print(flag)
        if not flag:
            for a in range(3):
                await notifyAdmin0("Тревога")
        print("updated")
    except Exception:
        print("Ошиб очка")


async def checkPages(s: requests.session):
    for a in range(0, len(urlList)):
        res1 = s.get(url=urlList[a], allow_redirects=False)
        print(res1.text)
        if not (res1.text == urlResultlist[a]):
            return False

    return True


async def login():
    url = 'https://adfs.sfedu.ru/adfs/ls/?client-request-id=567eafd2-9f6d-4405-8983-862beacae9b3&wa=wsignin1.0&wtrealm=urn%3afederation%3aMicrosoftOnline&wctx=LoginOptions%3D3%26estsredirect%3d2%26estsrequest%3drQIIATWPP0jcUBzH85q7qz0qFengVDI4Kbn3J7mXXEBQ6yA62B5S4RZ5efmFi94ld3kJF25wKYhurnYpdOxSqIvo4uJykzqJdOqmU-nUsYrcZ_jw3T5853RWI96spOBzS3BTENs1bWI5pu8SZjYsvw4O52HDIel0dermx96n7tfyyuHn_fmH0f3JKUJXCN29eLOxlGdt9qQkjYbwRTcYERYLObdA2kSIUFICIYFGQB3XtR3nuz5LnrHMJz9LjteYn3pFJt1uEo_0-aQHcRQYvTQJow4YSRh2ohi2hZSglJErSGspiKAmOp1bHf3WJ4XK1aIKIchraX5VQg-l10T3JiaqU9qMZmj_Suhb-fHVu-Ng5bq4XD3_W6H2r5E2KuN-YfWD1SFsJdHHtahYL1r4QxN6O6q7_N4Rjl-4m60m58NmfWmBevSogv5U0MFL7exVvZ1lPeVhPO7iwWDA8AB8rLI8gDjDMoljkBkWwzwFLNsgd--qbxlh1CS2SVyDUY_VPcpbF5Pafw2&cbcxt=&username=asus%40sfedu.ru&mkt=&lc= HTTP/1.1'

    headers = {
        "POST": "",
        "Host": "adfs.sfedu.ru",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Prefer": "safe",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "79",
        "Origin": "https://adfs.sfedu.ru",
        "DNT": "1",
        "Connection": "close",
        "Referer": "https://adfs.sfedu.ru/adfs/ls/?client-request-id=567eafd2-9f6d-4405-8983-862beacae9b3&wa=wsignin1.0&wtrealm=urn%3afederation%3aMicrosoftOnline&wctx=LoginOptions%3D3%26estsredirect%3d2%26estsrequest%3drQIIATWPP0jcUBzH85q7qz0qFengVDI4Kbn3J7mXXEBQ6yA62B5S4RZ5efmFi94ld3kJF25wKYhurnYpdOxSqIvo4uJykzqJdOqmU-nUsYrcZ_jw3T5853RWI96spOBzS3BTENs1bWI5pu8SZjYsvw4O52HDIel0dermx96n7tfyyuHn_fmH0f3JKUJXCN29eLOxlGdt9qQkjYbwRTcYERYLObdA2kSIUFICIYFGQB3XtR3nuz5LnrHMJz9LjteYn3pFJt1uEo_0-aQHcRQYvTQJow4YSRh2ohi2hZSglJErSGspiKAmOp1bHf3WJ4XK1aIKIchraX5VQg-l10T3JiaqU9qMZmj_Suhb-fHVu-Ng5bq4XD3_W6H2r5E2KuN-YfWD1SFsJdHHtahYL1r4QxN6O6q7_N4Rjl-4m60m58NmfWmBevSogv5U0MFL7exVvZ1lPeVhPO7iwWDA8AB8rLI8gDjDMoljkBkWwzwFLNsgd--qbxlh1CS2SVyDUY_VPcpbF5Pafw2&cbcxt=&username=asus%40sfedu.ru&mkt=&lc=",
        "Upgrade-Insecure-Requests": "1",
    }

    body = {
        "UserName": "asus@sfedu.ru",
        "Password": PASSWORD,
        "AuthMethod": "FormsAuthentication",
    }

    s = requests.session()
    s.get(url="https://sfedu.ru/www2/web/student/muam", allow_redirects=True)

    res1 = s.post(url, headers=headers, data=body, allow_redirects=True)

    wa = re.search(r'(?<=(name="wa" value=")).*?(?=(" \/>))', res1.text).group(0)
    wresult = re.search(r'(?<=(name="wresult" value=")).*?(?=(" \/>))', res1.text).group(0).replace('&lt;',
                                                                                                    '<').replace(
        '&quot;', '"')

    wctx = re.search(r'(?<=(name="wctx" value=")).*?(?=(" \/>))', res1.text).group(0).replace('&amp;', '&')

    url = 'https://login.microsoftonline.com/login.srf'
    headers = {
        "POST": "/login.srf HTTP/1.1",
        "Host": "login.microsoftonline.com",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Prefer": "safe",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "7181",
        "Origin": "https://adfs.sfedu.ru",
        "DNT": "1",
        "Connection": "close",
        "Referer": "https://adfs.sfedu.ru/",
        "Upgrade-Insecure-Requests": "1",
    }
    body = {
        "wa": wa,
        "wresult": wresult,
        "wctx": wctx,
    }
    res1 = s.post(url, headers=headers, data=body, allow_redirects=True)

    url = 'https://aadcdn.msftauth.net/shared/1.0/content/js/ConvergedKmsi_Core_41mpWztdGVyDdwYzkhE6VQ2.js'
    headers = {
        "GET": "/shared/1.0/content/js/ConvergedKmsi_Core_41mpWztdGVyDdwYzkhE6VQ2.js HTTP/1.1",
        "Host": "aadcdn.msftauth.net",
        "Accept": "*/*",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Prefer": "safe",
        "Referer": "https://login.microsoftonline.com/",
        "Origin": "https://login.microsoftonline.com/",
        "DNT": "1",
        "Connection": "close",
    }
    res1 = s.get(url, headers=headers, allow_redirects=True)

    url = 'https://aadcdn.msftauth.net/ests/2.1/content/cdnbundles/ux.converged.kmsi.strings-ru.min_losqnzte13wdgjnift3xyw2.js'
    headers = {
        "GET": "/ests/2.1/content/cdnbundles/ux.converged.kmsi.strings-ru.min_losqnzte13wdgjnift3xyw2.js HTTP/1.1",
        "Host": "aadcdn.msftauth.net",
        "Accept": "*/*",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Prefer": "safe",
        "Referer": "https://login.microsoftonline.com/",
        "X-Moz": "prefetch",
        "DNT": "1",
        "Connection": "close",
    }
    res1 = s.get(url, headers=headers, allow_redirects=True)

    url = 'https://sfedu.ru/www2/web/student/connect/azure'
    headers = {
        "GET": "/www2/web/student/connect/azure HTTP/1.1",
        "Host": "sfedu.ru",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Prefer": "safe",
        "Referer": "https://sfedu.ru/www/stat_pages22.show?p=STD/lks/D",
        "X-Moz": "prefetch",
        "DNT": "1",
        "Connection": "close",
    }
    res1 = s.get(url, headers=headers, allow_redirects=False)

    url = re.search(r'<title>Redirecting to (https://login\.microsoftonline\.com(/.*))</title>', res1.text).group(
        1).replace("&amp;", "&")
    GET = re.search(r'<title>Redirecting to (https://login\.microsoftonline\.com(/.*))</title>', res1.text).group(
        2).replace("&amp;", "&") + " HTTP/1.1"
    headers = {
        "GET": GET,
        "Host": "login.microsoftonline.com",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Prefer": "safe",
        "Referer": "https://sfedu.ru/",
        "DNT": "1",
        "Connection": "close",
    }
    res1 = s.get(url, headers=headers, allow_redirects=False)

    url = re.search(r'<a href="(https://sfedu.ru(.*))">here</a>.</h2>', res1.text).group(
        1).replace("&amp;", "&")
    GET = re.search(r'<a href="(https://sfedu.ru(.*))">here</a>.</h2>', res1.text).group(
        2).replace("&amp;", "&") + " HTTP/1.1"
    headers = {
        "GET": GET,
        "Host": "sfedu.ru",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Prefer": "safe",
        "Referer": "https://sfedu.ru/",
        "DNT": "1",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1"
    }

    res1 = s.get(url, headers=headers, allow_redirects=False)

    '''print()
    print("Сайт")
    print(res1.text)
    print()
    print()
    print("Печеньки")
    print(str(s.cookies))'''
    url = "https://sfedu.ru" + re.search(r'<a href="(.*)">', res1.text).group(
        1).replace("&amp;", "&")
    GET = re.search(r'<a href="(.*)">', res1.text).group(
        1).replace("&amp;", "&") + " HTTP/1.1"
    headers = {
        "GET": GET,
        "Host": "sfedu.ru",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Prefer": "safe",
        "DNT": "1",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1"
    }

    res1 = s.get(url, headers=headers, allow_redirects=False)
    return s

    # print(execjs.eval(res1.text))


if __name__ == '__main__':
    print("launched")
    check.start()
    executor.start_polling(dp)
