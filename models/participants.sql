CREATE TABLE IF NOT EXISTS participants (
    id SERIAL PRIMARY KEY,
    channel_id TEXT NOT NULL,
    user_id TEXT NOT NULL,
    standup_text TEXT,
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
