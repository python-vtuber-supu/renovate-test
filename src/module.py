import requests


def get_status(url):
    res = requests.get(url)
    return res.status_code
