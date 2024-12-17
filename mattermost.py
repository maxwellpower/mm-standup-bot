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

# File: mattermost.py

import requests
import os

API_URL = os.getenv("MATTERMOST_API_URL")
BOT_TOKEN = os.getenv("MATTERMOST_BOT_TOKEN")

def post_message(channel_id, message):
    url = f"{API_URL}/posts"
    headers = {"Authorization": f"Bearer {BOT_TOKEN}", "Content-Type": "application/json"}
    payload = {"channel_id": channel_id, "message": message}
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

def join_channel(channel_id):
    url = f"{API_URL}/channels/{channel_id}/members"
    headers = {"Authorization": f"Bearer {BOT_TOKEN}"}
    response = requests.post(url, headers=headers)
    return response.ok
