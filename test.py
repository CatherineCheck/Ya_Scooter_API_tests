import requests
import configuration
import data
from standrequest import new_order


def test_get_order_by_track():
    # получение номера созданного заказа
    track = new_order(data.body).json()['track']
    response = requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + str(track))

    assert response.status_code == 200
