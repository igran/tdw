# -*- coding: utf-8 -*-

type_list={
'Фильмы':'1',
'Сериалы':'4',
'Мультфильмы':'14899',
'ТВ':'14902',
'Музыка':'14903'
}

quality_list={
'Blu-Ray':'20',
'HDTV':'49',
'DVD9':'48',
'DVD5 ':'46',
'HDTVRip':'140',
'BDRip':'3',
'DVDRip':'45',
'WebRip HD':'144',
'DVDScreener':'55',
'TVRip':'50',
'WebRip':'6',
'TeleCine':'51',
'VHSRip':'54',
'TeleSynch':'52',
'CamRip':'53',
'КПК':'18'
}

countries_list={
'Австралия':'36',
'Австрия':'40',
'Азербайджан':'31',
'Аландские острова':'248',
'Албания':'8',
'Алжир':'12',
'Американские Виргинские острова':'850',
'Американское Самоа':'16',
'Ангилья':'660',
'Ангола':'24',
'Аргентина':'32',
'Армения':'51',
'Аруба':'533',
'Афганистан':'4',
'Багамы':'44',
'Беларусь':'112',
'Бельгия':'56',
'Болгария':'100',
'Боливия':'68',
'Босния и Герцеговина':'70',
'Ботсвана':'72',
'Бразилия':'76',
'Бутан':'64',
'Великобритания':'826',
'Венгрия':'348',
'Венесуэла':'862',
'Вьетнам':'704',
'Гаити':'332',
'Гана':'288',
'Германия':'276',
'Гондурас':'340',
'Гонконг':'344',
'Греция':'300',
'Грузия':'268',
'Дания':'208',
'Египет':'818',
'Замбия':'894',
'Израиль':'376',
'Индия':'356',
'Индонезия':'360',
'Ирак':'368',
'Иран':'364',
'Ирландия':'372',
'Исландия':'352',
'Испания':'724',
'Италия':'380',
'Казахстан':'398',
'Камерун':'120',
'Канада':'124',
'Катар':'634',
'Кения':'404',
'Кипр':'196',
'Киргизия':'417',
'Китайская Республика (Тайвань)':'158',
'КНДР':'408',
'КНР':'156',
'Колумбия':'170',
'Коста-Рика':'188',
'Куба':'192',
'Латвия':'428',
'Либерия':'430',
'Ливан':'422',
'Ливия':'434',
'Литва':'440',
'Лихтенштейн':'438',
'Люксембург':'442',
'Малайзия':'458',
'Мальта':'470',
'Марокко':'504',
'Мексика':'484',
'Молдавия':'498',
'Монако':'492',
'Монголия':'496',
'Намибия':'516',
'Непал':'524',
'Нидерланды':'528',
'Новая Зеландия':'554',
'Новая Каледония':'540',
'Норвегия':'578',
'ОАЭ':'784',
'Палестина':'275',
'Панама':'591',
'Парагвай':'600',
'Перу':'604',
'Польша':'616',
'Португалия':'620',
'Пуэрто-Рико':'630',
'Республика Македония':'807',
' Россия':'643',
'Румыния':'642',
'Саудовская Аравия':'682',
'Сербия':'688',
'Сербия и Черногория':'891',
'Сингапур':'702',
'Сирия':'760',
'Словакия':'703',
'Словения':'705',
' СССР':'810',
' США':'840',
'Таджикистан':'762',
'Таиланд':'764',
'Тайвань':'2',
'Танзания':'834',
'Тунис':'788',
'Туркмения':'795',
'Турция':'792',
'Узбекистан':'860',
'Украина':'804',
'Уругвай':'858',
'Филиппины':'608',
'Финляндия':'246',
'Франция':'250',
'Хорватия':'191',
'Чад':'148',
'Черногория':'499',
'Чехия':'203',
'Чехословакия':'3',
'Чили':'152',
'Швейцария':'756',
'Швеция':'752',
'Шри-Ланка':'144',
'Эквадор':'218',
'Эстония':'233',
'ЮАР':'710',
'Югославия':'1',
'Южная Корея':'410',
'Япония':'392'
}

translation_list={
'Русский фильм ':'44',
'Проф. (полное дублирование)':'41',
'Проф. (многоголосный, закадровый)':'40',
'Проф. (полное  дублирование)  [звук из кинотеатра]':'18',
'Проф. (многоголосный)':'38',
'Проф. (двухголосный)':'39',
'Проф. (Гоблин)':'36',
'Проф. (одноголосный)':'37',
'Любительский (многоголосный)':'35',
'Любительский (одноголосный)':'34',
'Субтитры':'42',
'Отсутствует':'43',
'Немое кино':'1'
}

tag_list={
'3D':'1',
'HDTV/HDTVRip 1080i':'4',
'HDTV/HDTVRip 720p':'5',
'Sci-Fi (Научная фантастика)':'11',
'to be continued...':'8',
'trash (треш) movies':'9',
'Авангард и Сюрреализм':'43',
'Аниме ':'2',
'Антиутопия':'42',
'Вампиры':'49',
'Гангстеры':'65',
'Зомби':'48',
'Индийское кино':'6',
'Киберпанк':'10',
'Коллекция':'47',
'Комикс':'57',
'Наркотики':'40',
'Новогодние':'51',
'Оборотни':'50',
'Параллельные миры':'59',
'Пеплум':'62',
'Перевод Гоблина':'7',
'Подростковая жестокость':'46',
'Постапокалипсис':'41',
'Призраки':'54',
'Пришельцы':'55',
'Псевдодокументальный':'64',
'Путешествия во времени':'58',
'Режиссерская версия':'3',
'Релакс':'39',
'Роуд-муви':'66',
'Слэшер':'63',
'Танцы':'56',
'Тюрьма':'53',
'Фанаты и Скинхеды':'45',
'Шпионы':'67',
'Экранизация':'60'
}

genre_list={
'Анимация':'22453' ,
'Аниме':'22409' ,
'Аниме сериалы':'22410' ,
'Арт-хаус / Авторское кино':'22450' ,
'Биография':'397'   ,
'Боевик':'15'    ,
'Боевые искусства':'22378' ,
'вампиры':'22412' ,
'Вестерн':'16'    ,
'Видеоклипы':'22502' ,
'Видовой':'22503' ,
'Военный':'21088' ,
'Война':'22413' ,
'Гипотезы':'22483' ,
'Детектив':'17'    ,
'Детский':'12760' ,
'Для взрослых':'22511' ,
'Документальные сериалы':'22500' ,
'Документальный':'394'   ,
'Дополнительные материалы':'22505' ,
'Драма':'18'    ,
'Загадки истории':'22492' ,
'Зарубежные мультфильмы':'22407' ,
'Зарубежный сериал':'22452' ,
'Зарубежный фильм':'22512' ,
'Земля':'22499' ,
'Искусство':'22509' ,
'Исторический':'19'    ,
'Катастрофа':'22481' ,
'киберпанк':'22417' ,
'Комедия':'20'    ,
'Концертное видео':'22501' ,
'Короткометражный':'5482'  ,
'Космос':'22484' ,
'Криминал':'22'    ,
'Кулинария':'22508' ,
'Личности':'22489' ,
'махо-сёдзё':'22419' ,
'Мелодрама':'23'    ,
'меха':'22420' ,
'Мистика':'24'    ,
'Музыка':'395'   ,
'Музыкальные программы':'22507' ,
'музыкальный':'22423' ,
'Мультсериалы':'22408' ,
'Мюзикл':'348'   ,
'Наука и технологии':'22485' ,
'Немое кино ':'22380' ,
'Нуар':'2243'  ,
'Пародия':'26'    ,
'повседневность':'22426' ,
'постапокалиптика':'22428' ,
'Приключения':'27'    ,
'Природа и животные':'22487' ,
'психология':'22430' ,
'Путешествия':'22491' ,
'Расследования':'22497' ,
'Религия':'22488' ,
'Роман':'21213' ,
'романтика':'22431' ,
'Русские мультфильмы':'22406' ,
'Русский сериал':'22451' ,
'Русский фильм':'22405' ,
'самурайский боевик':'22432' ,
'Семейный':'3645'  ,
'сёдзё':'22433' ,
'сёнэн':'22434' ,
'сёнэн-ай':'22435' ,
'Сказка':'15533' ,
'Советский фильм':'22404' ,
'Социум':'22494' ,
'Спектакль':'13950' ,
'Спорт':'29'    ,
'сэйнэн':'22436' ,
'Техника':'22486' ,
'Триллер':'30'    ,
'Увлечения':'22504' ,
'Ужасы':'31'    ,
'Фантастика':'32',
'Феномен':'22493',
'Фэнтези':'33',
#'хентай':'22448' ,
'Церемонии награждения':'22510' ,
'Цивилизации':'22496' ,
'Человек':'22490' ,
'школа':'22437' ,
'Эволюция':'22495' ,
'Экстрим':'22498' ,
'Эротика':'13944' ,
'этти':'22446' ,
#'яой':'22447'
}

award_list={
'After Dark Film Festival в Торонто':'42',
'After Dark Horrorfest':'14',
'Fangoria Chainsaw Awards':'25',
'Берлинский кинофестиваль':'26',
'Бодил (Дания)':'20',
'Британская академия (BAFTA)':'8' ,
'Брюссельский МКФ фэнтези, Sci-fi и триллеров':'38',
'Венецианский кинофестиваль':'27',
'Гойя (Испания)':'16',
'Давид (Италия)':'17',
'Джини (Канада)':'23',
'Европейская киноакадемия':'9' ,
'Золотая малина':'12',
'Золотой глобус':'2' ,
'Золотой Жук (Швеция)':'19',
'Золотой Орел':'44',
'Каннский кинофестиваль':'28',
'Кинофестиваль «Сандэнс»':'31',
'Лола (Германия)':'21',
'Международный кинофестиваль в Торонто':'34',
'МКФ в Карловых Варах':'30',
'МКФ в Ситжесе':'33',
'МКФ Сан-Себастьян':'32',
'МКФ фантастических фильмов в Жерармеере':'39',
'МКФ фантастических фильмов в Нёвшатель':'41',
'Московский МКФ':'29',
'Независимый дух':'13',
'Ника':'11',
'Оскар':'1' ,
'Премия Аманда (Норвегия)':'18',
'Премия британского независимого кино':'35',
'Премия Ирландской киноакадемии (IFTA)':'46',
'Премия канала «MTV»':'10',
'Премия общества независимого кино Chlotrudis':'36',
'Сатурн':'24',
'Сезар (Франция)':'15',
'Скримфест':'40',
'Фестиваль фантастических фильмов Фантаспорто':'37',
'Чешский лев':'45',
'Энни':'43',
'Юсси (Финляндия)':'22'
}

year_list={
' -- ':'не важно',
'2013':'2013'
}

sort_list={
'По релевантности':'14',
'Дате добавления (по убыванию)':'0',
'Дате добавления (по возрастанию)':'1',
'Популярности (по убыванию)':'2',
'Популярности (по возрастанию)':'3',
'Дате Релиза (по убыванию)':'6',
'Дате Релиза (по возрастанию)':'7',
'рейтингу (по убыванию)':'8',
'рейтингу (по возрастанию)':'9',
'Качество (по убыванию)':'10',
'Качество (по возрастанию)':'11',
'Новые фильмы на сайте':'12',
'Количество рекомендаций':'13'
}