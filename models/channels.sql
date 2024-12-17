CREATE TABLE IF NOT EXISTS channels (
    id SERIAL PRIMARY KEY,
    channel_id TEXT NOT NULL UNIQUE,
    reminder_time TEXT NOT NULL
);
