import json
import time
import random
import pyfiglet
import requests


def get_sign():
    print("enter birthday")

    month = int(input("month(int):"))

    day = int(input("day(int):"))
    year = int(input("year(int):"))

    payload = {'month': month, 'day': day, 'year': year}
    r = requests.post("http://127.0.0.1:5000", json=payload)
    # And done.
    data = r.json()
    print(data)
    print(r.text)  # displays the result body.

if __name__ == '__main__':
    while True:
        get_sign()
