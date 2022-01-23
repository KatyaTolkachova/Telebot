from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

place_cinema = InlineKeyboardMarkup(resize_keyboard=True,
                                    one_time_keyboard=True,
                                    row_width=2)
cinema_1 = InlineKeyboardButton(text='Silver Screen в ТЦ "Арена-Сити"',
                                url="https://silverscreen.by/cinemas/minsk/arena/")
cinema_2 = InlineKeyboardButton(text='Silver Screen в ТРЦ DANA MALL',
                                url="https://silverscreen.by/cinemas/minsk/dana/")
cinema_3 = InlineKeyboardButton(text='«3D Кино» в ТЦ «Замок»',
                                url="http://www.tczamok.by/poster/facility/28844")
cinema_4 = InlineKeyboardButton(text='3D Кинотеатр в Корона-сити',
                                url="http://www.tczamok.by/poster/facility/1291602")
cinema_5 = InlineKeyboardButton(text='АртКинотеатр ТЦ Европа',
                                url="https://artkinoteatr.by")
cinema_6 = InlineKeyboardButton(text='АртКинотеатр ТЦ Титан',
                                url="https://artkinoteatr.by")
place_cinema.add(cinema_1, cinema_2, cinema_3, cinema_4, cinema_5, cinema_6)

Circus = InlineKeyboardMarkup(resize_keyboard=True,
                              one_time_keyboard=True,
                              row_width=1)
cir = InlineKeyboardButton(text='ℹ️', url="https://circus.by")
Circus.add(cir)

ice_r = InlineKeyboardMarkup(resize_keyboard=True,
                             one_time_keyboard=True,
                             row_width=2)
ice1 = InlineKeyboardButton(text='Ледовый каток в ТЦ Замок', callback_data='ТЦ Замок')
ice2 = InlineKeyboardButton(text='Каток Чижовка-Арена', callback_data='Чижовка-Арена')
ice3 = InlineKeyboardButton(text='Ледовый дворец на Петровщине', callback_data='Петровщина')
ice4 = InlineKeyboardButton(text='Конькобежный стадион «Минск-Арена»', callback_data='«Минск-Арена»')
ice_r.add(ice1, ice2, ice3, ice4)

Zamok_ice_r = InlineKeyboardMarkup(resize_keyboard=True,
                                   one_time_keyboard=True,
                                   row_width=3)
pl_i1 = InlineKeyboardButton(text='ℹ️', url="http://www.tczamok.by/katok")
pl_i2 = InlineKeyboardButton(text='💰', callback_data='Z_price')
pl_i3 = InlineKeyboardButton(text='📍', callback_data='Z_street')
Zamok_ice_r.add(pl_i1, pl_i2, pl_i3)

ChA_ice_r = InlineKeyboardMarkup(resize_keyboard=True,
                                 one_time_keyboard=True,
                                 row_width=3)
pl_i1 = InlineKeyboardButton(text='ℹ️', url="https://chizhovka-arena.by/fizkultura-i-sport/katanie-na-konkah")
pl_i2 = InlineKeyboardButton(text='💰', callback_data='ChA_price')
pl_i3 = InlineKeyboardButton(text='📍', callback_data='ChA_street')
ChA_ice_r.add(pl_i1, pl_i2, pl_i3)

Led_Pet = InlineKeyboardMarkup(resize_keyboard=True,
                               one_time_keyboard=True,
                               row_width=3)
pl_i1 = InlineKeyboardButton(text='ℹ️', url="https://katki.gdevminske.by/Malinovka%20.html")
pl_i2 = InlineKeyboardButton(text='💰', callback_data='Led_price')
pl_i3 = InlineKeyboardButton(text='📍', callback_data='Led_street')
Led_Pet.add(pl_i1, pl_i2, pl_i3)

Minsk_arena = InlineKeyboardMarkup(resize_keyboard=True,
                                   one_time_keyboard=True,
                                   row_width=3)
pl_i1 = InlineKeyboardButton(text='ℹ️', url="https://minskarena.by/taxonomy/term/6")
pl_i2 = InlineKeyboardButton(text='💰', callback_data='MA_price')
pl_i3 = InlineKeyboardButton(text='📍', callback_data='MA_street')
Minsk_arena.add(pl_i1, pl_i2, pl_i3)

museum = InlineKeyboardMarkup(resize_keyboard=True,
                              one_time_keyboard=True,
                              row_width=2)
m1 = InlineKeyboardButton(text='Музей Страна мини', callback_data='Страна мини')
m2 = InlineKeyboardButton(text='Музей истории Великой Отечественной войны', callback_data='Музей ВОВ')
m3 = InlineKeyboardButton(text='Национальный художественный музей', callback_data='Художественный музей')
m4 = InlineKeyboardButton(text='Национальный центр современных искусств', callback_data='Центр искусств')
m5 = InlineKeyboardButton(text='Музей пивоварения «Аливария»', callback_data='«Аливария»')
m6 = InlineKeyboardButton(text='Музей денег Groshi', callback_data='Groshi')
museum.add(m1, m2, m3, m4, m5, m6)

small_city = InlineKeyboardMarkup(resize_keyboard=True,
                                  one_time_keyboard=True,
                                  row_width=2)
s_c1 = InlineKeyboardButton(text='ℹ️', url='https://belarusmini.by')
s_c2 = InlineKeyboardButton(text='⏰', callback_data='SC_clock')
small_city.add(s_c1, s_c2)

mus_vov = InlineKeyboardMarkup(resize_keyboard=True,
                               one_time_keyboard=True,
                               row_width=2)
m_v1 = InlineKeyboardButton(text='ℹ️', url='http://www.warmuseum.by')
m_v2 = InlineKeyboardButton(text='⏰', callback_data='MV_clock')
mus_vov.add(m_v1, m_v2)

h_m = InlineKeyboardMarkup(resize_keyboard=True,
                           one_time_keyboard=True,
                           row_width=2)
h_m1 = InlineKeyboardButton(text='ℹ️', url='https://www.artmuseum.by')
h_m2 = InlineKeyboardButton(text='⏰', callback_data='HM_clock')
h_m.add(h_m1, h_m2)

si_m = InlineKeyboardMarkup(resize_keyboard=True,
                            one_time_keyboard=True,
                            row_width=2)
h_m1 = InlineKeyboardButton(text='ℹ️', url='http://ncsm.by')
h_m2 = InlineKeyboardButton(text='⏰', callback_data='MSI_clock')
si_m.add(h_m1, h_m2)

pivavar = InlineKeyboardMarkup(resize_keyboard=True,
                               one_time_keyboard=True,
                               row_width=1)
p1 = InlineKeyboardButton(text='ℹ️', url='https://alivariamuseum.by')
pivavar.add(p1)

money_mus = InlineKeyboardMarkup(resize_keyboard=True,
                                 one_time_keyboard=True,
                                 row_width=2)
m_m1 = InlineKeyboardButton(text='ℹ️', url='http://mgroshi.by')
m_m2 = InlineKeyboardButton(text='⏰', callback_data='MM_clock')
money_mus.add(m_m1, m_m2)

night_club = InlineKeyboardMarkup(resize_keyboard=True,
                                  one_time_keyboard=True,
                                  row_width=2)
n_c1 = InlineKeyboardButton(text='HookahPlace Yakuba Kolasa', url="http://hookah-place.by")
n_c2 = InlineKeyboardButton(text='Nuahule', url="https://nua.by")
n_c3 = InlineKeyboardButton(text='Dictator Bar', url="http://www.dictator.by")
n_c4 = InlineKeyboardButton(text='TNT Rock Club', url="https://tntrockclub.com")
n_c5 = InlineKeyboardButton(text='MADMEN', url="https://madmenminsk.business.site")
n_c6 = InlineKeyboardButton(text='Банки Бутылки', url="https://www.instagram.com/bankibutylki/")
night_club.add(n_c1, n_c2, n_c3, n_c4, n_c5, n_c6)


Home_film = InlineKeyboardMarkup(resize_keyboard=True,
                                 one_time_keyboard=True,
                                 row_width=2)
hf1 = InlineKeyboardButton(text='Комедия', callback_data='comedy')
hf2 = InlineKeyboardButton(text='Мультфильмы', callback_data='cartoon')
hf3 = InlineKeyboardButton(text='Боевики', callback_data='action_movie')
hf4 = InlineKeyboardButton(text='Ужасы', callback_data='horror')
Home_film.add(hf1, hf2, hf3, hf4)


one_home = InlineKeyboardMarkup(resize_keyboard=True,
                                one_time_keyboard=True,
                                row_width=1)
o_h1 = InlineKeyboardButton(text='Смотреть здесь ℹ️', url="https://kinogo.la/216-odin-doma-1990_19_58_08.html")
one_home.add(o_h1)


holiday = InlineKeyboardMarkup(resize_keyboard=True,
                               one_time_keyboard=True,
                               row_width=1)
hol1 = InlineKeyboardButton(text='Смотреть здесь ℹ️', url="https://kinogo.la/28621-holidate_2020.html")
holiday.add(hol1)


man_vegas = InlineKeyboardMarkup(resize_keyboard=True,
                                 one_time_keyboard=True,
                                 row_width=1)
mn1 = InlineKeyboardButton(text='Смотреть здесь ℹ️', url="https://kinogo.biz/25348-malchishnik-v-vegase.html")
man_vegas.add(mn1)


kd = InlineKeyboardMarkup(resize_keyboard=True,
                          one_time_keyboard=True,
                          row_width=1)
k1 = InlineKeyboardButton(text='Смотреть здесь ℹ️', url="https://kinogo.biz/21887-kadry.html")
kd.add(k1)

mam = InlineKeyboardMarkup(resize_keyboard=True,
                           one_time_keyboard=True,
                           row_width=1)
mam1 = InlineKeyboardButton(text='Смотреть здесь ℹ️', url="https://kinogo.la/440-macho-i-botan-2012-smotret-onlayn.html")
mam.add(mam1)


million = InlineKeyboardMarkup(resize_keyboard=True,
                               one_time_keyboard=True,
                               row_width=1)
mil1 = InlineKeyboardButton(text='Смотреть здесь ℹ️', url="https://kinogo.la/1112-my-millery-2013-smotret-onlayn.html")
million.add(mil1)


seven = InlineKeyboardMarkup(resize_keyboard=True,
                             one_time_keyboard=True,
                             row_width=1)
s1 = InlineKeyboardButton(text='Смотреть здесь ℹ️', url="https://kinogo.la/18531-sem-uzhinov_2019.html")
seven.add(s1)

g_voic = InlineKeyboardMarkup(resize_keyboard=True,
                              one_time_keyboard=True,
                              row_width=1)
v1 = InlineKeyboardButton(text='Смотреть здесь ℹ️', url="https://kinogo.la/18080-gromkaya-svyaz_2018.html")
g_voic.add(v1)

friday = InlineKeyboardMarkup(resize_keyboard=True,
                              one_time_keyboard=True,
                              row_width=1)
fr1 = InlineKeyboardButton(text='Смотреть здесь ℹ️', url="https://kinogo.biz/32887-pjatnica.html")
friday.add(fr1)

davay = InlineKeyboardMarkup(resize_keyboard=True,
                             one_time_keyboard=True,
                             row_width=1)
dav1 = InlineKeyboardButton(text='Смотреть здесь ℹ️', url="https://kinogo.la/23022-davay-razvedemsya.html")
davay.add(dav1)

dysha = InlineKeyboardMarkup(resize_keyboard=True,
                             one_time_keyboard=True,
                             row_width=1)
dsh1 = InlineKeyboardButton(text='Смотреть здесь ℹ️', url="https://kinogo.la/30081-soul_2020.html")
dysha.add(dsh1)

zooam = InlineKeyboardMarkup(resize_keyboard=True,
                             one_time_keyboard=True,
                             row_width=1)
za1 = InlineKeyboardButton(text='Смотреть здесь ℹ️', url="https://kinogo.la/2944-zveropolis-2016-smotret-onlayn.html")
zooam.add(za1)

live_an = InlineKeyboardMarkup(resize_keyboard=True,
                               one_time_keyboard=True,
                               row_width=1)
la1 = InlineKeyboardButton(text='Смотреть здесь ℹ️', url="https://kinogo.la/3661-taynaya-zhizn-domashnih-zhivotnyh-2016-smotret-onlayn.html")
live_an.add(la1)

main_pr = InlineKeyboardMarkup(resize_keyboard=True,
                               one_time_keyboard=True,
                               row_width=1)
mp1 = InlineKeyboardButton(text='Смотреть здесь ℹ️', url="https://kinogo.la/33536-free-guy.html")
main_pr.add(mp1)

peopl = InlineKeyboardMarkup(resize_keyboard=True,
                             one_time_keyboard=True,
                             row_width=1)
peop1 = InlineKeyboardButton(text='Смотреть здесь ℹ️', url="https://kinogo.la/31598-wrath-of-man.html")
peopl.add(peop1)

ybludki = InlineKeyboardMarkup(resize_keyboard=True,
                               one_time_keyboard=True,
                               row_width=1)
ybl1 = InlineKeyboardButton(text='Смотреть здесь ℹ️', url="https://kinogo.biz/12016-besslavnye-ubljudki.html")
ybludki.add(ybl1)

ono = InlineKeyboardMarkup(resize_keyboard=True,
                           one_time_keyboard=True,
                           row_width=1)
on1 = InlineKeyboardButton(text='Смотреть здесь ℹ️', url="https://kinogo.biz/19895-ono.html")
ono.add(on1)

train_t = InlineKeyboardMarkup(resize_keyboard=True,
                               one_time_keyboard=True,
                               row_width=1)
trat1 = InlineKeyboardButton(text='Смотреть здесь ℹ️', url="https://kinogo.la/3876-smotret-onlayn-poezd-v-pusan_2016-11-10.html")
train_t.add(trat1)

proch = InlineKeyboardMarkup(resize_keyboard=True,
                             one_time_keyboard=True,
                             row_width=1)
pr1 = InlineKeyboardButton(text='Смотреть здесь ℹ️', url="https://kinogo.la/5068-watch-online-movie-proch_get-out_2017.html")
proch.add(pr1)