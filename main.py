
import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = 'your api token '

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

tugmacha_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Og\'iz ochish duosi🤲'),
            KeyboardButton('Og\'iz yopish duosi🤲')
        ],
        [
            KeyboardButton('Ramazon Taqvimi🗓')

        ],
        [
            KeyboardButton('Ramazon oyidagi eng afzal amallar😊🤍'),
            KeyboardButton('Ramazon muborak(music)!')
        ],
        [
            KeyboardButton('Murojat uchun admin🧑‍💻')
        ]

    ], resize_keyboard=True
)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer(f"Assalomu aleykum xurmatli: {message.from_user.first_name} "
                         f"Ramazon taqvimi botiga xush kelibsiz(23.03.23)\n Menyudan birini tanlang:",
                         reply_markup=tugmacha_menu)


@dp.message_handler(text='Og\'iz yopish duosi🤲')
async def send_time(message: types.Message):
    await message.answer(f"💫 Оғиз ёпиш дуоси: “Навайту ан асума совма шаҳри рамазона минал фажри илал мағриби, холисан"
                         f" лиллаҳи таъала. Aллоҳу акбар”,✅ Маъноси: Рамазон ойининг рўзасини тонг отганидан кун ботгунича "
                         f"холис Aллоҳ таоло учун тутишни ният қилдим. Aллоҳу акбар")
    file = open('photos/img.png', 'rb')
    await message.answer_photo(photo=file)


@dp.message_handler(text = 'Og\'iz ochish duosi🤲')
async def sendyopish(message: types.Message):
    await message.answer(f"💫 Оғиз очиш дуоси: “Aллоҳумма лака сумту ва бика аманту ва аълайка таваккалту ва аълаа"
                         f" ризқика афторту, фағфирлий ма қоддамту ва маа аххорту”.✅  Маъноси: Ё Aллоҳ! Сенга имон "
                         f"келтириб, Сенга таваккал қилиб, Сен учун рўза тутдим. Сен берган ризқ билан ифтор қилдим. Эй "
                         f"гуноҳларни кечиргувчи Зот! Олдинги ва кейинги гуноҳларимни кечир. Aмин!")

    file = open('photos/img_1.png', 'rb')
    await message.answer_photo(photo=file)


@dp.message_handler(text='Ramazon Taqvimi🗓')
async def taqvim(message: types.Message):
    file = open('photos/taqvimuz.jpg', 'rb')
    await message.answer_photo(photo=file)


@dp.message_handler(text = 'Murojat uchun admin🧑‍💻')
async def adminuz(message:types.Message):
    await message.answer("adminga murojat qilish uchun man shu userni ustiga bosing:@Bexruz_dev1🧑‍💻🤖")

ℬℯ𝓍𝓇𝓊𝓏 𝒩𝒶𝒷𝒾𝓎ℯ𝓋, [26.03.2023 10:51]
@dp.message_handler(text='Ramazon oyidagi eng afzal amallar😊🤍')
async def adminuz(message:types.Message):
    await message.answer('- Ro‘za tutishlik. Ro‘za tutishlik faqatgina yeb-ichishdan tiyilish emas,'
                         ' balki har qanday ma’siyatlar va yolg‘on, tuhmat va g‘iybat kabi Allohning g‘azabini'
                         ' keltiradigan amallardan ham uzoq bo‘lish lozim.'
                         '- Qur’on tilovat qilish. Bu oyda Qur’on tilovat qilish Alloh taologa eng mahbub ishlardandir.'
                         ' Namozlarni ko‘paytirish. Farz bo‘lgan 5 mahal namozdan tashqari, sunnat va nafl ibodatlarini'
                         ' ham ko‘paytirish lozim. Xususan,  jamoat bilan o‘qiladigan Taroveh namozlarni g‘animat bilish kerak.'
                         '- Silai-rahm qilish. Yaqinlar va qarindoshlarni ziyorat qilish. Chunki bunday amallar kishilar'
                         ' o‘rtasida o‘zaro muhabbat rishtalarini mustahkamlaydi.'
                         '- Xayr-ehson qilish. Bu oyda sadaqa qilish – eng afzal ishlardan bo‘lib, Alloh taolo bu amalni'
                         ' qiluvchini O‘zi mukofotlaydi. Shuningdek, Rosululloh sollallohu alayhi vasallam bu oyda boshqa '
                         'oylardan ko‘ra saxiyroq bo‘lar edilar.'
                         '- Laylatul qadr kechasini bedor o‘tkazish. Rasululloh sollallohu alayhi vasallam sahobalarini '
                         'Laylatul qadrni topishga va uni bedor o‘tkazishga undar edilar. Chunki, Alloh taolo bu kunning'
                         ' qadrini boshqa kunlarning mingtasidan afzal qilgan.')



@dp.message_handler(text='Ramazon muborak(music)!')
async  def hadislar(message:types.Message):
    await message.answer("yuklanmoqda🔎..")
    file = open('vidio1/Ramazon muborak!.mp4' , 'rb')
    await message.answer_video(video=file)


#
# @dp.message_handler()
# async def echo(message: types.Message):
#     # old style:
#     # await bot.send_message(message.chat.id, message.text)
#
#     await message.answer(message.text)


if name == 'main':
    executor.start_polling(dp, skip_updates=True)
