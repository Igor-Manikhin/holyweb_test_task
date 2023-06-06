# holyweb_test_task
## Описание задания

Даны модели "Категория Блюд" и "Блюдо" для ресторана.

Даны сериализаторы.
  
В выборку попадают только Блюда у которых is_publish=True.
Если в категории нет блюд (или все блюда данной категории 
имеют is_publish=False) - не включаем ее в выборку.
  
Запрос в БД сделать любым удобным способом:
Django ORM (предпочтительно), Raw SQL, Sqlalchemy... 

Написать View который вернет для API 127.0.0.1/api/v1/foods/ 
JSON следующего формата:
  
    [
      {
         "id":1,
         "name_ru":"Напитки",
         "name_en":null,
         "name_ch":null,
         "order_id":10,
         "foods":[
            {
               "internal_code":100,
               "code":1,
               "name_ru":"Чай",
               "description_ru":"Чай 100 гр",
               "description_en":null,
               "description_ch":null,
               "is_vegan":false,
               "is_special":false,
               "cost":"123.00",
               "additional":[
                  200
               ]
            },
            {
               "internal_code":200,
               "code":2,
               "name_ru":"Кола",
               "description_ru":"Кола",
               "description_en":null,
               "description_ch":null,
               "is_vegan":false,
               "is_special":false,
               "cost":"123.00",
               "additional":[
                  
               ]
            },
            {
               "internal_code":300,
               "code":3,
               "name_ru":"Спрайт",
               "description_ru":"Спрайт",
               "description_en":null,
               "description_ch":null,
               "is_vegan":false,
               "is_special":false,
               "cost":"123.00",
               "additional":[
                  
               ]
            },
            {
               "internal_code":400,
               "code":4,
               "name_ru":"Байкал",
               "description_ru":"Байкал",
               "description_en":null,
               "description_ch":null,
               "is_vegan":false,
               "is_special":false,
               "cost":"123.00",
               "additional":[
                  
               ]
            }
         ]
      },
      {
         "id":2,
         "name_ru":"Выпечка",
         "name_en":null,
         "name_ch":null,
         "order_id":20,
         "foods":[...]
      },
      {...},
      {...}
     ]

Технологии:
- Python3
- Django >= 2.0
- Django REST framework
- mixer
- PostgresSQL

По оформлению:
- RESTful API
- PEP8

### Локальное разворачивание проекта
Для удобного запуска и разворачивания проекта используется образ, который запускается в отдельном изолированном 
контейнере при помощи docker.
Локальное разворачивание проекта осуществляется посредством docker-compose.

При локальном разворачивании проекта микросервиса - выполняется создание и запуск следующих контейнеров:
- restraunt_backend (основной контейнер проекта).

При запуске контейнера **restraunt_backend** выполняются следующие действия:
- применение набора миграций для создания таблиц в локальной базе данных проекта;
- запуск django-приложения.

Локальное разворачивание и запуск проекта микросервиса осуществляется следующей командой:
```commandline
docker-compose up -d --build
```

После выполнения указанной команды будет произведено создание и запуск вышеописанных контейнеров и 
сервис будет доступен по адресу http://localhost:8000.

После запуска проекта необходимо создать суперпользователя для возможности авторизации в админ.панели
с целью удобного наполнения используемой в проекте базы данных необходимыми данными. 
Для этого необходимо выполнить следующую команду внутри контейнера **restraunt_backend**:
```commandline
python manage.py createsuperuser
```

Запуск тестов внутри контейнера **restraunt_backend** производится следующей командой:
```commandline
python manage.py test
```

Получение списка категорий с относимыми к ним продуктов будет доступно по адресу http://localhost:8000/api/v1/foods/
