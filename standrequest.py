import requests
import configuration
import data

# Создание нового заказа
def new_order(body):

    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)

response = new_order(data.body)

# Получение заказа по его номеру
def get_order_info(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + str(track))