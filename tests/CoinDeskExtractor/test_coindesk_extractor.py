#coding=utf-8
import json
import time
import requests

COINDESK_URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'


def main():
    ret = {
        'status_code': 500,
        'file_path': None,
        'content_type': None,
        'file_path': None

    }
    response = requests.get(COINDESK_URL)
    if response.status_code == 200:

        body = response.json()
        ret['status_code'] = response.status_code
        ret['content_type'] = response.headers['Content-Type']

        ts = time.time()
        filename = """coindesk-data-repository/raw/{}.json""".format(int(ts))
        
        ret['file_path'] = filename

        with open(filename, 'w') as f:
            json.dump(body, f)

    return ret


if __name__ == '__main__':
    main()