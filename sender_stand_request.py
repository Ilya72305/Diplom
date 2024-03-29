import configuration
import requests
import data


def create_order(body):

    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.HEADERS)


def get_order_info(track):

    params = {'t': track}
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_INFO_PATH,
                        params=params,
                        headers=data.HEADERS)
