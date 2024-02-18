# Юлия Блинова, 13-я когорта — Финальный проект. Инженер по тестированию плюс

import configuration
import requests
import data

def post_new_order(order):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER,
                         json=order,
                         headers=data.headers)

response = post_new_order(data.order)
order = response.json()
track = order.get('track')
print(response.status_code)
print(track)

def get_orger():
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + str(track))

response = get_orger()
print(response.status_code)

def test_positive_assert():
   assert response.status_code == 200
