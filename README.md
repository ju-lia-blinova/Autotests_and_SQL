﻿В файле SQL.md находятся sql запросы к заданию про базу данных


Для запуска теста должны быть установлены пакеты pytest и requests 
Запуск теста выполянется командой pytest
Перед запуском необходимо обновить ссылку на адрес стенда, содержащуюся в URL_SERVICE в файле "configuration.py"

Был автоматизирован сценарий:
1. Клиент создает заказ.
2. Проверяется, что по треку заказа можно получить данные о заказе.

Шаги автотеста:
1. Выполнить запрос на создание заказа.
2. Сохранить номер трека заказа.
3. Выполнить запрос на получения заказа по треку заказа.
4. Проверить, что код ответа равен 200.