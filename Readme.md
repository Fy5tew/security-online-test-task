# Тестовое задание (Django/DRF)

## Cервис по управлению задачами внутри компании.

### Описание

Проект представляет собой API сервиса по управлению задачами.
В сервисе есть два типа пользователей.
*Заказчики* могут создавать задачи, а *Сотрудники* - назначать себе задачи для выполнения.

Управление пользователями осуществляется через админ-панель.

Авторизация пользователей для работы с API проходит посредству JWT-токенов (access и refresh).


### Зависимости
- Python 3.10
- Django 5.0
- Django Rest Framework 3.15

Полный список зависимостей находится в файле [requirements.txt](https://github.com/Fy5tew/security-online-test-task/blob/main/requirements.txt).


### Установка и настройка

Здесь указаны основные команды для установки и настройки проекта.

#### Клонирование репозитория
```commandline
git clone https://github.com/Fy5tew/security-online-test-task.git
```
#### Установка зависимостей
```commandline
pip install -r requirements.txt
```
#### Запуск миграций базы данных
```commandline
python manage.py migrate
```
#### Запуск локального сервера
```commandline
python manage.py runserver
```
#### Создание суперпользователя
```commandline
python manage.py createsuperuser
```
Созданный суперпользователь имеет права для доступа к админ-панели и редактирования записей в базе данных.
От его имени необходимо создать типы пользователей, определенные в [файле настроек](https://github.com/Fy5tew/security-online-test-task/blob/main/taskmgr/settings.py),
а так же дополнительных пользователей - заказчиков и сотрудников.
Параметр **ALLOWED_USER_TYPES** отвечает за то, какие типы пользователей имеют доступ к API.
```python
ALLOWED_USER_TYPES = {
    'EMPLOYEE_TYPE_NAME': 'Employee',
    'CUSTOMER_TYPE_NAME': 'Customer',
}
```


### Использование

#### Администрирование
Управление пользователями и другими объектами может проводиться суперпользователем через админ-панель,
которая доступна по адресу ***/admin***.

#### Взаимодействие пользователей
Зарегистрированные пользователи могут взаимодействовать с сервисом с помощью REST API по адресу ***/api/v1/***.
Здесь доступны методы для работы как сотрудников, так и заказчиков.


### Дополнительно

Доступен экспорт коллекции запросов Postman для эндпоинтов - [endpoints.postman_collection.json](https://github.com/Fy5tew/security-online-test-task/blob/main/endpoints.postman_collection.json).
