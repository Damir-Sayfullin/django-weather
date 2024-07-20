### Тестовое задание
Прошу дать обратную связь по поводу выполненного задания 
по одному из способов связи со мной:
* Telegram - https://t.me/DamirS16
* VK - https://vk.com/damirsaifullin
* HeadHunter - https://kazan.hh.ru/resume/80087a9bff0b5a2c9a0039ed1f70516970566c
* Телефон - +79173877619
* Email - saifullin.d02@mail.ru

# django-weather
Веб-приложение для получения текущей погоды в любом городе. 
На сайте можно посмотреть историю поиска по городам, а также получить эти данные с API.
Для получения координат используется API [DaData](https://dadata.ru/), а для получения погоды по этим координатам - API [Open-Meteo](https://open-meteo.com).

### Скриншоты
*Главная страница с автодополнением и историей поиска для каждого пользователя*

<img src="https://i.ibb.co/GRdyDQH/django-weather-1.png" alt="django-weather-1" border="0" width="500px">

*Ошибка при вводе несуществующего города*

<img src="https://i.ibb.co/g41tx86/django-weather-3.png" alt="django-weather-3" border="0" width="500px">

*Вывод текущей погоды*

<img src="https://i.ibb.co/dM5LYsp/django-weather-2.png" alt="django-weather-2" border="0" width="500px">

*История поиска*

<img src="https://i.ibb.co/r788MCL/django-weather-4.png" alt="django-weather-4" border="0" width="500px">

*Страница "Об API"*

<img src="https://i.ibb.co/8DqjkcZ/django-weather-5.png" alt="django-weather-5" border="0" width="500px">

*Страница "О сайте"*

<img src="https://i.ibb.co/2gZCkX0/django-weather-6.png" alt="django-weather-6" border="0" width="500px">

### Используемый стек технологий:
* python 3.9
* django 4.2.14
* requests 2.32.3
* djangorestframework 3.15.2

### Задачи:
* ✅ Ввод названия города и получение прогноза погода в этом городе на ближайшее время. 
Вывод данных должен быть в удобно читаемом формате.
API для погоды: https://open-meteo.com/
* ✅ API, показывающее сколько раз вводили какой город
* ✅ Сделать автодополнение (подсказки) при вводе города
* ✅ При повторном посещении сайта будет предложено посмотреть погоду в городе,
  в котором пользователь уже смотрел ранее и история поиска для каждого пользователя
* ✅ Написать тесты
* ✅ Поместить в Docker

### Использование:
1. Клонируйте репозиторий с помощью команды:
```commandline
git clone https://github.com/Damir-Sayfullin/django-weather.git
```
2. Создайте в папке проекта файл `secret.json` и запишите в нем ключи в виде:
```json
{
  "SECRET_KEY": "your-django-secret-key",
  "DADATA_KEY": "your_dadata_api_key"
}
```
3. Создайте виртуальное окружение и установите зависимости:
```commandline
python -m venv venv
venv\Scripts\activate.bat (Windows)
source venv/bin/activate (Linux и MacOS)
pip install -r requirements.txt
```
4. Запустите проект, выполнив команды:
```commandline
cd .\django_weather
python manage.py runserver
```
### API:
* Получение всех данных о всех городах:
```
GET /api/
```
* Получение данных о конкретном городе. Подставьте свой город вместо {city}:
```
GET /api/?city={city}
```
