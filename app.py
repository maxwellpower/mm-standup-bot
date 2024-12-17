# Mattermost Example Standup Bot

# Copyright (c) 2024 Maxwell Power
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom
# the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE
# AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# File: app.py

from flask import Flask, request, jsonify
from routes.standup import handle_setup, handle_standup
from scheduler import start_scheduler
from database import initialize_db

app = Flask(__name__)

@app.route("/setup", methods=["POST"])
def setup():
    data = request.json
    return jsonify(handle_setup(data["channel_id"], data["reminder_time"]))

@app.route("/standup", methods=["POST"])
def standup():
    data = request.json
    return jsonify(handle_standup(data["channel_id"], data["user_id"], data["text"]))

if __name__ == "__main__":
    initialize_db()
    start_scheduler()
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 3000)))