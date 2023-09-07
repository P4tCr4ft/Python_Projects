from flask import Flask, request
import os
import sys

# Get the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# Get the parent directory (one level up)
parent_dir = os.path.dirname(current_dir)
# Add the parent directory to the sys.path list
sys.path.insert(0, parent_dir)

# print(sys.path)

import config

app = Flask(__name__)


@app.route("/")
def hello_world():
    print(request)
    print(request.headers)
    return "Hello, World!"


if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT, threaded=False)
