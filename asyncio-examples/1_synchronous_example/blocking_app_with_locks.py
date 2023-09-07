from threading import Lock
from time import sleep

from flask import Flask

app = Flask(__name__)
lock = Lock()

"""
The Python Global Interpreter Lock or GIL, in simple words, is a mutex (or a lock) 
that allows only one thread to hold the control of the Python interpreter. 
This means that only one thread can be in a state of execution at any point in time.
"""


@app.route("/")
def hello_world():
    slow_processing(1, 1)
    # for i in range(5):
    #     print(f"#{i} root doing some processing ...")
    #     sleep(1)
    return "Hello, World!"


@app.route("/healthz")
def healthz():
    slow_processing(2, 1)
    # for i in range(5):
    #     print(f"#{i} healthz doing some processing ...")
    #     sleep(1)
    return "OK"


def slow_processing(pid, duration):  # blocks the python interpreter
    with lock:
        for i in range(10):
            print(f"PID #{pid} Itter #{i} doing some processing ...")
            sleep(duration)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="9000")
