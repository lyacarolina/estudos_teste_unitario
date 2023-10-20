#coding=utf-8
import requests

COINDESK_URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'


def main():
    ret = {'status_code': 500}
    response = requests.get(COINDESK_URL)
    if response.status_code == 200:
        body = response.json()
        ret['status_code'] = response.status_code
    return ret


if __name__ == '__main__':
    main()