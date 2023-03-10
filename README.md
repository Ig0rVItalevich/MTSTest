## Задание

На кинопоиске есть страница: https://www.kinopoisk.ru/lists/movies/popular/

Эта страница является стартовой для списка из 1000 самых популярных фильмов/сериалов.

Нужно собрать информацию о всех этих 1000 фильмах. 

Необходимо выбрать:

- Номер в рейтинге
- Название на русском
- Название  на английском
- Год выпуска
- Рейтинг кинопоиска

## Комментарий

Задание выполнено с помощью библиотек **requests** и **BeautifulSoup**. Выбор был сделан в их пользу, так как задание и объем данных парсинга небольшие и использовать **scrapy** я посчитал излишним. Интервал между запросами 5 секунд для избежания блокировки. 

## Запуск скрипта

Тестирование проводилось на ОС Linux Ubuntu.

1. Склонировать репозиторий с помощью команды ```git clone https://github.com/Ig0rVItalevich/MTSTest.git```

2. Перейти в каталог проекта ```cd ./MTSTest```

3. Создать виртуальное окружение ```python3 -m venv venv```

4. Активировать виртуальное окружение ```source venv/bin/activate```

5. Установить библиотеки и зависимости ```pip install -r requirements.txt```

6. Запустить скрипт ```python3 parse.py```

После выполнения в каталоге проекта появится файл **items.json**