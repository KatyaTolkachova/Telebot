from aiogram import types
from loader import dp, bot
from keyboards.default import menu, place, go_city
from keyboards.inline import place_cinema, Circus, ice_r, Zamok_ice_r, ChA_ice_r, Led_Pet, Minsk_arena, museum, \
    small_city, mus_vov, h_m, si_m, pivavar, money_mus, night_club, Home_film, one_home, holiday, man_vegas, kd, mam, \
    million, seven, g_voic, friday, davay, dysha, zooam, live_an, main_pr, peopl, ybludki, ono, train_t, proch


@dp.message_handler(commands=['start'])
async def create_keyboard(message: types.Message):
    await message.answer(f'{message.from_user.full_name},привет. '
                         f'Я бот помощник! Выберите, где хотите отдохнуть!',
                         reply_markup=menu)


@dp.message_handler(text='Назад')
async def otm(message: types.Message):
    await message.answer(f'{message.from_user.full_name},решили вернуться к главному меню.', reply_markup=menu)


@dp.message_handler(text='Просмотр фильма 🎬')
async def place_film(message: types.Message):
    await message.answer(f'{message.from_user.full_name},отличный выбор, осталось определиться где!',
                         reply_markup=place)


@dp.message_handler(text='В кинотеатре 🎥')
async def pl_f(message: types.Message):
    await message.answer(f'{message.from_user.full_name},выберите место:', reply_markup=place_cinema)


@dp.message_handler(text='Дома 🏠')
async def film_home(message: types.Message):
    await message.answer(f'{message.from_user.full_name},выберите жанр кино:', reply_markup=Home_film)


@dp.message_handler(text='Выйти в город')
async def city(message: types.Message):
    await message.answer(f'{message.from_user.full_name},определите место отдыха!', reply_markup=go_city)


@dp.message_handler(text='Цирк 🎪')
async def circus(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         'AgACAgIAAxkBAAIDb2Hlpd9-14rAncsVHM7ei7eikspjAAIttzEb7FMoS-zywrmLSWlxAQADAgADbQADIwQ',
                         caption='Сайт цирка:', reply_markup=Circus)


@dp.message_handler(text='Каток ⛸')
async def ice(message: types.Message):
    await message.answer(f'{message.from_user.full_name},выберите место:', reply_markup=ice_r)


@dp.message_handler(text='Выставки/музеи 🏛️')
async def mus(message: types.Message):
    await message.answer(f'{message.from_user.full_name},выберите место:', reply_markup=museum)


@dp.message_handler(text='Вечеринка🎉')
async def mus(message: types.Message):
    await message.answer(f'{message.from_user.full_name},выберите ночной клуб:', reply_markup=night_club)


@dp.callback_query_handler(lambda call: call.data == 'Страна мини')
async def s_m(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         'AgACAgIAAxkBAAIEYWHm3CGWhLCQpk3Rqo4a1LcGd7XZAAJuuDEbiho5S2Q1a4QyE6I-AQADAgADcwADIwQ',
                         caption='Музей Страна мини',
                         reply_markup=small_city)


@dp.callback_query_handler(lambda call: call.data == 'SC_clock')
async def ma_ice(message: types.Message):
    await bot.send_message(message.from_user.id, 'Пн-Пт: 13:00-20:00,\n'
                                                 'Сб- Вс: 11:00-20:00\n')


@dp.callback_query_handler(lambda call: call.data == 'Музей ВОВ')
async def m_vov(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         'AgACAgIAAxkBAAIEY2Hm3EsXZhhveUMvAZ8ob9bbRb3aAAJwuDEbiho5SwvSnP_C92XPAQADAgADeQADIwQ',
                         caption='Музей истории Великой Отечественной войны',
                         reply_markup=mus_vov)


@dp.callback_query_handler(lambda call: call.data == 'MV_clock')
async def ma_ice(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вт-Вс: 10:00-18:00,\n'
                                                 'Пн: выходной день\n')


@dp.callback_query_handler(lambda call: call.data == '«Аливария»')
async def piv(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         'AgACAgIAAxkBAAIEaWHm3L_PrpjirSrgwCyfb71lhtVKAAJzuDEbiho5S3MFYoJAt50zAQADAgADeQADIwQ',
                         caption='Музей пивоварения «Аливария»',
                         reply_markup=pivavar)


@dp.callback_query_handler(lambda call: call.data == 'Художественный музей')
async def mus_h(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         'AgACAgIAAxkBAAIEZWHm3HKSZULGi28n_I6O7QvaEh60AAJxuDEbiho5S2vI1i2pa9XeAQADAgADeQADIwQ',
                         caption='Национальный художественный музей',
                         reply_markup=h_m)


@dp.callback_query_handler(lambda call: call.data == 'HM_clock')
async def mus_clock(message: types.Message):
    await bot.send_message(message.from_user.id, 'Пн: 11:00 – 19:00,\n'
                                                 'Вт: выходной день,\n'
                                                 'Ср: 11:00 – 19:00,\n'
                                                 'Чт: 13:00 – 21:00,\n'
                                                 'Пт: 11:00 – 19:00,\n'
                                                 'Сб: 11:00 – 19:00,\n'
                                                 'Вс: 11:00 – 19:00,\n'
                                                 'Касса и сувенирный киоск прекращают свою работу за 30 мин. до закрытия музея\n')


@dp.callback_query_handler(lambda call: call.data == 'Центр искусств')
async def m_si(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         'AgACAgIAAxkBAAIEZ2Hm3JyRoPl_pHdiFY7HbOsVbeRkAAJyuDEbiho5S8TwdE3I8MexAQADAgADeQADIwQ',
                         caption='Национальный центр современных искусств',
                         reply_markup=si_m)


@dp.callback_query_handler(lambda call: call.data == 'MSI_clock')
async def ma_ice(message: types.Message):
    await bot.send_message(message.from_user.id, 'НЦСМ на Някрасава, 3:\n'
                                                 '   Ср-Вс: 12.00 – 20.00,\n'
                                                 '   Пн-Вт: выходные,\n '
                                                 'НЦСМ на Незалежнасці, 47:\n'
                                                 '   Вт-Вс: 12.00 – 20.00,\n'
                                                 '   Пн: выходной\n')


@dp.callback_query_handler(lambda call: call.data == 'Groshi')
async def m_money(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         'AgACAgIAAxkBAAIEa2Hm3Ns8rePAw2Aj4WW_6138TWgkAAJ0uDEbiho5SwSiv1Oo8pPSAQADAgADeQADIwQ',
                         caption='Музей денег Groshi',
                         reply_markup=money_mus)


@dp.callback_query_handler(lambda call: call.data == 'MM_clock')
async def mon_clock(message: types.Message):
    await bot.send_message(message.from_user.id, 'Пн-Вс 10.00-19.00')


@dp.callback_query_handler(lambda call: call.data == 'ТЦ Замок')
async def zamok_ice(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         'AgACAgIAAxkBAAIDOGHlo0-6II3aXa0d_nrAirrviOQeAAIjtzEb7FMoS_evZ3CFszldAQADAgADeAADIwQ',
                         caption='Ледовый каток в ТЦ Замок',
                         reply_markup=Zamok_ice_r)


@dp.callback_query_handler(lambda call: call.data == 'Z_price')
async def ma_ice(message: types.Message):
    await bot.send_message(message.from_user.id, 'Цена билетов:\n'
                                                 '   Взрослый билет:\n'
                                                 '       В будние дни - 7 р. 00 к.\n'
                                                 '       В выходные и праздничные дни - 8 р. 00 к.\n'
                                                 '   Дети от 3 до 14 лет:\n'
                                                 '       В будние дни - 5 р. 00 к.\n'
                                                 '       В выходные и праздничные дни - 6 р. 00 к.\n'
                                                 'Прокат коньков - 6 р. 00 к.\n'
                                                 'Прокат детского тренажера «Пингвин» - 6 р. 00 к.\n')


@dp.callback_query_handler(lambda call: call.data == 'Z_street')
async def ma_ice(message: types.Message):
    await bot.send_venue(message.from_user.id, latitude=53.92624, longitude=27.517582, title='ТЦ Замок',
                         address='Минск, просп. Победителей, 65')


@dp.callback_query_handler(lambda call: call.data == 'Чижовка-Арена')
async def cha_ice(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         'AgACAgIAAxkBAAIDOmHlo5fvOA4JzOMJ-hnKWBYfvHOMAAIktzEb7FMoS6YpqnTYbRe1AQADAgADeQADIwQ',
                         caption='Каток Чижовка-Арена',
                         reply_markup=ChA_ice_r)


@dp.callback_query_handler(lambda call: call.data == 'ChA_price')
async def ma_ice(message: types.Message):
    await bot.send_message(message.from_user.id, 'Цена билетов:\n'
                                                 '   Взрослый билет - 5 р. 00 к.\n'
                                                 '   Дети до 16 лет - 3 р. 00 к.\n'
                                                 'Прокат коньков - 3 р. 00 к.\n'
                                                 'Прокат детского тренажера «Пингвин» - 5 р. 00 к.\n')


@dp.callback_query_handler(lambda call: call.data == 'ChA_street')
async def ma_ice(message: types.Message):
    await bot.send_venue(message.from_user.id, latitude=53.844553, longitude=27.628657, title='Чижовка-Арена',
                         address='Минск, ул. Ташкенская, 19')


@dp.callback_query_handler(lambda call: call.data == 'Петровщина')
async def led_ice(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         'AgACAgIAAxkBAAIDPGHlo897RqsWf7On2NWsC2qwheDQAAImtzEb7FMoS5muzKoCJlS8AQADAgADeAADIwQ',
                         caption='Ледовый дворец на Петровщине',
                         reply_markup=Led_Pet)


@dp.callback_query_handler(lambda call: call.data == 'Led_price')
async def ma_ice(message: types.Message):
    await bot.send_message(message.from_user.id, 'Цена билетов:\n'
                                                 '   Взрослый билет:\n'
                                                 '       В будние дни и выходные (17:00 - 23:00) - 6 р. 00 к.\n'
                                                 '       В будние дни (07:00 - 17:00) - 4 р. 00 к.\n'
                                                 '   Дети:\n'
                                                 '       В будние дни и выходные (17:00 - 23:00) - 4 р. 50 к.\n'
                                                 '       В будние дни (07:00 - 17:00) - 3 р. 00 к.\n'
                                                 'Прокат коньков - 4 р. 00 к.\n'
                                                 'Прокат детского тренажера «Пингвин» - 5 р. 00 к.\n')


@dp.callback_query_handler(lambda call: call.data == 'Led_street')
async def ma_ice(message: types.Message):
    await bot.send_venue(message.from_user.id, latitude=53.857486, longitude=27.487972,
                         title='Ледовый дворец на Петровщине',
                         address='Минск, проезд Каролинский, 5-4 (Метро "Петровщина" (500м)')


@dp.callback_query_handler(lambda call: call.data == '«Минск-Арена»')
async def ma_ice(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         'AgACAgIAAxkBAAIDPmHlpAbWgnZIE7-ExykoLGDMmQvCAAIntzEb7FMoS-4-U5J4472gAQADAgADeAADIwQ',
                         caption='Конькобежный стадион «Минск-Арена»',
                         reply_markup=Minsk_arena)


@dp.callback_query_handler(lambda call: call.data == 'MA_price')
async def ma_ice(message: types.Message):
    await bot.send_message(message.from_user.id, 'Цена билетов:\n'
                                                 ' Конькобежный стадион:\n'
                                                 '   Взрослый билет - 5 р. 50 к.\n'
                                                 '   Дети до 16 лет - 3 р. 50 к.\n'
                                                 'Прокат коньков - 3 р. 00 к.\n'
                                                 'Прокат детского тренажера «Пингвин» - 5 р. 00 к.\n'
                                                 ' Арена:\n'
                                                 '   Взрослый билет - 9 р. 00 к.\n'
                                                 '   Дети до 16 лет - 6 р. 50 к.\n'
                                                 'Прокат коньков - 4 р. 00 к.\n')


@dp.callback_query_handler(lambda call: call.data == 'MA_street')
async def ma_ice(message: types.Message):
    await bot.send_venue(message.from_user.id, latitude=53.935930, longitude=27.481638,
                         title='Конькобежный стадион «Минск-Арена»', address='Минск, проспект Победителей, 111')


@dp.callback_query_handler(lambda call: call.data == 'comedy')
async def com(message: types.Message):
    await bot.send_message(message.from_user.id, 'Фильмы из этого жанра:\n'
                                                 '1.Один дома(1990; 8,3; /m838383)\n'
                                                 '2.Пара на праздники(2020; 6,5; /m656565)\n'
                                                 '3.Мальчишник в Вегасе(2009; 7,9; /m797979)\n'
                                                 '4.Кадры(2013; 7,1; /m717171)\n'
                                                 '5.Мачо и ботан(2012; 7,0; /m707070)\n'
                                                 '6.Мы – Миллеры(2013; 7,3; /m737373)\n'
                                                 '7.Семь ужинов(2019; 6,1; /m616161)\n'
                                                 '8.Громкая связь(2018; 6,8; /m686868)\n'
                                                 '9.Пятница(2016; 6,6; /m666666)\n'
                                                 '10. Давай разведемся!(2019; 5,9; /m595959)\n')


@dp.message_handler(commands=['m838383'])
async def comf1(message: types.Message):
    await bot.send_video(message.from_user.id,
                         'BAACAgIAAxkBAAIF_GHoVY1gx-Tp_kSwgiWNdcTE_x_nAAJ8FAACwR9AS33b7DQKugABriME',
                         caption='Один дома', reply_markup=one_home)


@dp.message_handler(commands=['m656565'])
async def comf2(message: types.Message):
    await bot.send_video(message.from_user.id,
                         'BAACAgIAAxkBAAIGCmHoVyvMfOJMbspA6TEfG9xaviiwAAKVFAACwR9AS-KzhpzJwHQkIwQ',
                         caption='Пара на праздники', reply_markup=holiday)


@dp.message_handler(commands=['m797979'])
async def comf3(message: types.Message):
    await bot.send_video(message.from_user.id,
                         'BAACAgIAAxkBAAIGD2HoWHB-aoQqb5HrUsKP64CuhSTuAAKeFAACwR9AS_lAySrI3qSWIwQ',
                         caption='Мальчишник в Вегасе', reply_markup=man_vegas)


@dp.message_handler(commands=['m717171'])
async def comf4(message: types.Message):
    await bot.send_video(message.from_user.id,
                         'BAACAgIAAxkBAAIGFGHoWQflRbMKIY0Y0dw-NRot7vctAAKiFAACwR9AS4GUIDpL4Ty2IwQ',
                         caption='Кадры', reply_markup=kd)


@dp.message_handler(commands=['m707070'])
async def comf5(message: types.Message):
    await bot.send_video(message.from_user.id,
                         'BAACAgIAAxkBAAIGGWHoWYzbGbao0ItgIy8JKdBPIgE7AAKoFAACwR9AS2RD4PxvmineIwQ',
                         caption='Мачо и ботан', reply_markup=mam)


@dp.message_handler(commands=['m737373'])
async def comf6(message: types.Message):
    await bot.send_video(message.from_user.id,
                         'BAACAgIAAxkBAAIGH2HoWiL_KW-6f37Uz4XniM3F4m90AAKxFAACwR9AS5qeAj4vFZaEIwQ',
                         caption='Мы – Миллеры', reply_markup=million)


@dp.message_handler(commands=['m616161'])
async def comf7(message: types.Message):
    await bot.send_video(message.from_user.id,
                         'BAACAgIAAxkBAAIGJGHoWsClCVEQgki8MUgnFg0RoRakAAKzFAACwR9AS6vjsdodWbcTIwQ',
                         caption='Семь ужинов', reply_markup=seven)


@dp.message_handler(commands=['m686868'])
async def comf8(message: types.Message):
    await bot.send_video(message.from_user.id,
                         'BAACAgIAAxkBAAIGKWHoWyGGhK8cGiw6c_O_rmklnNnfAAK0FAACwR9ASwnIpXQY3pBAIwQ',
                         caption='Громкая связь ', reply_markup=g_voic)


@dp.message_handler(commands=['m666666'])
async def comf9(message: types.Message):
    await bot.send_video(message.from_user.id,
                         'BAACAgIAAxkBAAIGLmHoW-35ZVvQORzj4JALtL28xFvCAAK7FAACwR9AS72-PKMFS7GyIwQ',
                         caption='Пятница', reply_markup=friday)


@dp.message_handler(commands=['m595959'])
async def comf10(message: types.Message):
    await bot.send_video(message.from_user.id,
                         'BAACAgIAAxkBAAIGM2HoXFuW_k-hyFY-r1p-2BLUGXtPAAK_FAACwR9AS1tu1i29v_hxIwQ',
                         caption='Давай разведемся!', reply_markup=davay)


@dp.callback_query_handler(lambda call: call.data == 'cartoon')
async def car(message: types.Message):
    await bot.send_message(message.from_user.id, 'Фильмы из этого жанра:\n'
                                                 '1.Душа (2020; 8,4; /m848484),\n'
                                                 '2.Зверополис (2016; 8,3; /m830830),\n'
                                                 '3.Тайная жизнь домашних животных (2016; 6,8; /m680680)\n')


@dp.message_handler(commands=['m848484'])
async def car1(message: types.Message):
    await bot.send_video(message.from_user.id,
                         'BAACAgIAAxkBAAIHKmHodS5YUxU7lckWBNueagwK5U4bAAICEgACwR9IS790JKSPqISpIwQ',
                         caption='Душа', reply_markup=dysha)


@dp.message_handler(commands=['m830830'])
async def car2(message: types.Message):
    await bot.send_video(message.from_user.id,
                         'BAACAgIAAxkBAAIHMWHodaSbG1lK729Wx50uRP00zAznAAIEEgACwR9IS164ZC7QaNW9IwQ',
                         caption='Зверополис', reply_markup=zooam)


@dp.message_handler(commands=['m680680'])
async def car3(message: types.Message):
    await bot.send_video(message.from_user.id,
                         'BAACAgIAAxkBAAIHNmHodg1Gg3eX_JdpreZ_Fh8pTdGWAAIFEgACwR9ISxU1tgY9RtPSIwQ',
                         caption='Тайная жизнь домашних животных', reply_markup=live_an)


@dp.callback_query_handler(lambda call: call.data == 'action_movie')
async def act(message: types.Message):
    await bot.send_message(message.from_user.id, 'Фильмы из этого жанра:\n'
                                                 '1.Главный герой (2021; 7,4; /m747474),\n'
                                                 '2.Гнев человеческий (2021; 7,6; /m760760),\n'
                                                 '3.Бесславные ублюдки (2009; 7,9; /m790790)\n')


@dp.message_handler(commands=['m747474'])
async def act1(message: types.Message):
    await bot.send_video(message.from_user.id,
                         'BAACAgIAAxkBAAIHO2Hodr86JeN3l9JYYkHUe0TGA0GpAAIHEgACwR9IS3kCXfLAFbR7IwQ',
                         caption='Главный герой', reply_markup=main_pr)


@dp.message_handler(commands=['m760760'])
async def act2(message: types.Message):
    await bot.send_video(message.from_user.id,
                         'BAACAgIAAxkBAAIHQGHodyjRUe75ZHxlLcOZs0aVv8tyAAIIEgACwR9IS1G6k9KQ6JjiIwQ',
                         caption='Гнев человеческий', reply_markup=peopl)


@dp.message_handler(commands=['m790790'])
async def act3(message: types.Message):
    await bot.send_video(message.from_user.id,
                         'BAACAgIAAxkBAAIHRWHod4Vb64AXeDdguPRl4tHVykINAAILEgACwR9IS5fDeR4mU5tfIwQ',
                         caption='Бесславные ублюдки', reply_markup=ybludki)


@dp.callback_query_handler(lambda call: call.data == 'horror')
async def hor(message: types.Message):
    await bot.send_message(message.from_user.id, 'Фильмы из этого жанра:\n'
                                                 '1.Оно (2017; 7,3; /m730730),\n'
                                                 '2.Поезд в Пусан (2016; 7,1; /m710710),\n'
                                                 '3.Прочь (2017; 7,1; /m720720)\n')


@dp.message_handler(commands=['m730730'])
async def hor1(message: types.Message):
    await bot.send_video(message.from_user.id,
                         'BAACAgIAAxkBAAIHSmHod_AAAdhMJJytDAfJiTKQkKC9TgACDBIAAsEfSEvwvNRxYFjqSSME',
                         caption='Оно', reply_markup=ono)


@dp.message_handler(commands=['m710710'])
async def hor2(message: types.Message):
    await bot.send_video(message.from_user.id,
                         'BAACAgIAAxkBAAIHT2HoeEBXz8nU531E7qEOYjPS8uhQAAINEgACwR9IS9V9bgABlFQpIiME',
                         caption='Поезд в Пусан', reply_markup=train_t)


@dp.message_handler(commands=['m720720'])
async def hor3(message: types.Message):
    await bot.send_video(message.from_user.id,
                         'BAACAgIAAxkBAAIHVGHoeLc59GkTwV7RZSzd3Ad-fUx5AAIOEgACwR9ISzS4UmvyShRLIwQ',
                         caption='Прочь', reply_markup=proch)
