# django-weather
Веб-приложение для получения текущей погоды в любом городе.

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
* ⬛ Сделать автодополнение (подсказки) при вводе города
* ⬛ При повторном посещении сайта будет предложено посмотреть погоду в городе,
  в котором пользователь уже смотрел ранее и история поиска для каждого пользователя
* ⬛ Написать тесты
* ⬛ Поместить в Docker

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