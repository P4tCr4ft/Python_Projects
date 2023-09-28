import time

import requests


def generate_request():
    print("Sending 1st Msg")
    yield b"hi"
    print("Sleeping.....")
    time.sleep(2)
    print("Sending 2nd Msg")
    yield b"there"


with requests.Session() as client:
    resp = client.post(f"http://127.0.0.1:9000", data=generate_request())
    print(f"SJT -  resp and stripped are: {resp} and {resp.text.strip()}")
