ALTER TABLE posts DROP CONSTRAINT IF EXISTS posts_username_fkey;
ALTER TABLE user_sessions DROP CONSTRAINT IF EXISTS user_sessions_username_fkey;
ALTER TABLE message_threads DROP CONSTRAINT IF EXISTS message_threads_sender_username_fkey;
ALTER TABLE message_threads DROP CONSTRAINT IF EXISTS message_threads_recipient_username_fkey;
ALTER TABLE messages DROP CONSTRAINT IF EXISTS messages_sender_username_fkey;
ALTER TABLE messages DROP CONSTRAINT IF EXISTS messages_recipient_username_fkey;
ALTER TABLE favorites DROP CONSTRAINT IF EXISTS favorites_username_fkey;

DROP TABLE IF EXISTS favorites CASCADE;
DROP TABLE IF EXISTS messages CASCADE;
DROP TABLE IF EXISTS posts CASCADE;
DROP TABLE IF EXISTS users CASCADE;


CREATE TABLE IF NOT EXISTS users (
   username            VARCHAR(255)    NOT NULL    UNIQUE,
   email               VARCHAR(255)    NOT NULL    UNIQUE,
   pass                VARCHAR(255)    NOT NULL,
   biography           VARCHAR(255),
   first_name          VARCHAR(255)    NOT NULL,
   last_name           VARCHAR(255)    NOT NULL,
   dob                 DATE            NOT NULL,
   profile_picture     VARCHAR(255)    NULL,
   PRIMARY KEY(username)
);


CREATE TABLE IF NOT EXISTS posts (
   username        VARCHAR(255)    NOT NULL,
   post_id         SERIAL          NOT NULL,
   title           VARCHAR(255)    NOT NULL,
   body            VARCHAR(255)    NOT NULL,
   price           DECIMAL(10,2)   NOT NULL,
   condition       VARCHAR(255)    NOT NULL,
   posted_date     DATE       DEFAULT     CURRENT_DATE,
   image_url       VARCHAR(255)    NULL,
   PRIMARY KEY(post_id),
   FOREIGN KEY(username) REFERENCES users(username) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS user_sessions (
 
   sid SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    session_id VARCHAR(255) UNIQUE NOT NULL,
    FOREIGN KEY (username) REFERENCES users(username) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS message_threads (
    thread_id SERIAL PRIMARY KEY,
    sender_username VARCHAR(255) NOT NULL,
    recipient_username VARCHAR(255) NOT NULL,
    UNIQUE (sender_username, recipient_username),
    FOREIGN KEY (sender_username) REFERENCES users(username) ON DELETE CASCADE,
    FOREIGN KEY (recipient_username) REFERENCES users(username) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS messages (
    message_id SERIAL PRIMARY KEY,
    thread_id INTEGER NOT NULL,
    sender_username VARCHAR(255) NOT NULL,
    recipient_username VARCHAR(255) NOT NULL,
    message_content TEXT,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (thread_id) REFERENCES message_threads(thread_id) ON DELETE CASCADE,
    FOREIGN KEY (sender_username) REFERENCES users(username) ON DELETE CASCADE,
    FOREIGN KEY (recipient_username) REFERENCES users(username) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS favorites (
    favorite_id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    post_id INTEGER NOT NULL,
    UNIQUE (username, post_id),
    FOREIGN KEY (username) REFERENCES users(username) ON DELETE CASCADE,
    FOREIGN KEY (post_id) REFERENCES posts(post_id) ON DELETE CASCADE
);

ALTER TABLE posts ADD CONSTRAINT posts_username_fkey FOREIGN KEY (username) REFERENCES users(username) ON UPDATE CASCADE;
ALTER TABLE user_sessions ADD CONSTRAINT user_sessions_username_fkey FOREIGN KEY (username) REFERENCES users(username) ON UPDATE CASCADE;
ALTER TABLE message_threads ADD CONSTRAINT message_threads_sender_username_fkey FOREIGN KEY (sender_username) REFERENCES users(username) ON UPDATE CASCADE;
ALTER TABLE message_threads ADD CONSTRAINT message_threads_recipient_username_fkey FOREIGN KEY (recipient_username) REFERENCES users(username) ON UPDATE CASCADE;
ALTER TABLE messages ADD CONSTRAINT messages_sender_username_fkey FOREIGN KEY (sender_username) REFERENCES users(username) ON UPDATE CASCADE;
ALTER TABLE messages ADD CONSTRAINT messages_recipient_username_fkey FOREIGN KEY (recipient_username) REFERENCES users(username) ON UPDATE CASCADE;
ALTER TABLE favorites ADD CONSTRAINT favorites_username_fkey FOREIGN KEY (username) REFERENCES users(username) ON UPDATE CASCADE;
