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

# File: routes/scheduler.py

from apscheduler.schedulers.background import BackgroundScheduler
from database import connect_db
from mattermost import post_message

scheduler = BackgroundScheduler()

def send_reminders():
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT channel_id, reminder_time FROM channels")
        channels = cur.fetchall()
        for channel_id, _ in channels:
            post_message(channel_id, "Reminder: Submit your daily standup using `/standup`!")

def start_scheduler():
    scheduler.add_job(send_reminders, "cron", hour="9", minute="0")  # Default to 9 AM
    scheduler.start()
