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

# File: routes/standup.py

from database import connect_db
from mattermost import post_message
import os

def handle_setup(channel_id, reminder_time):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute(
            "INSERT INTO channels (channel_id, reminder_time) VALUES (%s, %s) ON CONFLICT (channel_id) DO UPDATE SET reminder_time = EXCLUDED.reminder_time",
            (channel_id, reminder_time),
        )
        conn.commit()
    return post_message(channel_id, "Standup reminders have been configured!")

def handle_standup(channel_id, user_id, standup_text):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute(
            "INSERT INTO participants (channel_id, user_id, standup_text) VALUES (%s, %s, %s)",
            (channel_id, user_id, standup_text),
        )
        conn.commit()
    return "Standup logged successfully!"
