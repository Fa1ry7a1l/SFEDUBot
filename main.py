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
urlList = [str]


class AdminSetClass(StatesGroup):
    otvet = State()


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    print("process_start_command started")
    await message.reply("Приветик")


@dp.message_handler(commands=['getId'])
async def notification_callback_handler(query: types.CallbackQuery):
    print("hands update. user: " + str(query.from_user.id))
    await bot.send_message(query.from_user.id, "Ваш id " + f"{query.from_user.id}")


@dp.message_handler(commands=['update'])
async def updating(query: types.CallbackQuery):
    """print("hands update. user: " + str(query.from_user.id))
    await AdminSetClass.otvet.set()
    await bot.send_message(query.from_user.id, "Введите строку запроса")"""
    print("Send request")
    await login()
    await bot.send_message(query.from_user.id, "ready")


##@dp.message_handler(commands=['c'])
async def notifyAdmin0(tst: str):
    for a in admin0:
        await bot.send_message(a, "Собираемся")


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


'''
@dp.message_handler(commands=['addAdmin'])
async def notification_callback_handler(query: types.CallbackQuery):
    await AdminSetClass.otvet.set()
    await bot.send_message(query.from_user.id, "Введите номер админки 1 или 2 и id пользователя")



@dp.message_handler(state=AdminSetClass.otvet)
async def process_message(message: types.Message, state: FSMContext):
    message.text
'''


async def update():
    print("updating")


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
    print()
    print()
    print()
    print("Куки")
    print(str(s.cookies))

    res1 = s.post(url, headers=headers, data=body, allow_redirects=True)
    print()
    print()
    print()
    print("Куки")
    print(str(s.cookies))
    print()
    print("Сайт")
    print(str(res1.text))
"""
    url = 'https://adfs.sfedu.ru/adfs/ls/?client-request-id=567eafd2-9f6d-4405-8983-862beacae9b3&wa=wsignin1.0&wtrealm=urn%3afederation%3aMicrosoftOnline&wctx=LoginOptions%3D3%26estsredirect%3d2%26estsrequest%3drQIIATWPP0jcUBzH85q7qz0qFengVDI4Kbn3J7mXXEBQ6yA62B5S4RZ5efmFi94ld3kJF25wKYhurnYpdOxSqIvo4uJykzqJdOqmU-nUsYrcZ_jw3T5853RWI96spOBzS3BTENs1bWI5pu8SZjYsvw4O52HDIel0dermx96n7tfyyuHn_fmH0f3JKUJXCN29eLOxlGdt9qQkjYbwRTcYERYLObdA2kSIUFICIYFGQB3XtR3nuz5LnrHMJz9LjteYn3pFJt1uEo_0-aQHcRQYvTQJow4YSRh2ohi2hZSglJErSGspiKAmOp1bHf3WJ4XK1aIKIchraX5VQg-l10T3JiaqU9qMZmj_Suhb-fHVu-Ng5bq4XD3_W6H2r5E2KuN-YfWD1SFsJdHHtahYL1r4QxN6O6q7_N4Rjl-4m60m58NmfWmBevSogv5U0MFL7exVvZ1lPeVhPO7iwWDA8AB8rLI8gDjDMoljkBkWwzwFLNsgd--qbxlh1CS2SVyDUY_VPcpbF5Pafw2&cbcxt=&username=asus%40sfedu.ru&mkt=&lc= HTTP/1.1'

    headers = {
        "GET": "",
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

    res1 = s.get(url, headers=headers, allow_redirects=True)
    print()
    print()
    print()
    print("Куки")
    print(str(s.cookies))
    print()
    print("Страница")
    print(str(res1.status_code))
    print(str(res1.text))
    
     res2 = s.get(url="http://lks.sfedu.ru", allow_redirects=True)

    print()
    print()
    print()
    print("Куки")
    print(str(s.cookies))

    print()
    print()
    print()
    print("Страница")
    print(res2.text)

    res3 = s.get(url="https://sfedu.ru/www2/web/student/muam", allow_redirects=True)
    print()
    print()
    print()
    print("Куки")
    print(str(s.cookies))

    print()
    print()
    print()
    print("Страница")
    print(res3.text)"""


"""
    res2 = requests.get("http://lks.sfedu.ru", cookies=res.cookies)

    print()
    print()
    print()
    print("Гет запрос")
    print(res2.text)
    print(str(res2.cookies))"""

if __name__ == '__main__':
    print("started")
    executor.start_polling(dp)
