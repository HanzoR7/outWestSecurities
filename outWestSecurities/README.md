# outWestSecurities (OWS)
Кратко: эмулятор биржи

Развёрнуто: 
- Акции
- Покупка / Продажа
- Торговля в лонг
- Торговля в шорт
- Торговля с плечом
- Margin call
- История - загружается в виде массива котировок. Позже - эмулируется ботами.

## Технологический стек
- Python 3.8 (не меньше)
- Django 3
- Django REST Framework


## Подготовка рабочего места разработчика.

### Установка необходимых библиотек
```bash
sudo apt install make gcc g++
curl -fsSL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs
````

### Backend

1. Создать venv, установить библиотеки
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

2. Подготовить БД
   * Установить postgresql
     ```bash
     sudo apt install postgresql
     sudo systemctl start postgresql.service
     sudo systemctl enable postgresql.service
     ```
   * Создать юзера и базу
     ```bash
     sudo -u postgres psql
     ```
     Далее в консоли postgresql
     ```sql
     create database exchange;
     create user shp with encrypted password 'promprog';
     grant all privileges on database exchange to shp;
     \q
     ```

   * Актуализировать схему
     ```bash
     ./manage.py migrate
     ```
   * создать юзера (выполняется только для разработки))
     ```bash
     ./manage.py shell -c "from django.contrib.auth import get_user_model; get_user_model().objects.create_superuser('vasya', '1@abc.net', 'promprog')"
     ```


### Запуск проекта
```bash
python price_bot.py    # открыть в отдельной вкладке, команда будет работать на протяжении всего времени
python candles_bot.py    # открыть в отдельной вкладке, команда будет работать на протяжении всего времени
./manage.py runserver  # открыть в отдельной вкладке, команда будет работать на протяжении всего времени
```

## Тесты
Для тестирования чистоты кода введите в терминал команду:
```bash
DJANGO_SETTINGS_MODULE=exchange_engine.settings pylint --load-plugins pylint_django --load-plugins pylint_django.checkers.migrations *
```

Для тестирования самого кода введите в терминал:
```bash
./manage.py test
```
