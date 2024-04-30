DROP TABLE IF EXISTS messages CASCADE;
DROP TABLE IF EXISTS message_threads CASCADE;
DROP TABLE IF EXISTS user_sessions CASCADE;
DROP TABLE IF EXISTS posts CASCADE;
DROP TABLE IF EXISTS messages CASCADE;
DROP TABLE IF EXISTS user_sessions CASCADE;
DROP TABLE IF EXISTS message_threads CASCADE;
DROP TABLE IF EXISTS users CASCADE;

CREATE TABLE IF NOT EXISTS users (
<<<<<<< HEAD
   username            VARCHAR(255)    NOT NULL    UNIQUE,
   email               VARCHAR(255)    NOT NULL    UNIQUE,
   pass                VARCHAR(255)    NOT NULL,
   biography           VARCHAR(255),
   first_name          VARCHAR(255)    NOT NULL,
   last_name           VARCHAR(255)    NOT NULL,
   dob                 DATE            NOT NULL,
   profile_picture     VARCHAR(255)    NULL,
   PRIMARY KEY(username)
=======
    username            VARCHAR(255)    NOT NULL    UNIQUE,
    email               VARCHAR(255)    NOT NULL    UNIQUE,
    pass                VARCHAR(255)    NOT NULL,
    biography           VARCHAR(255),
    first_name          VARCHAR(255)    NOT NULL,
    last_name           VARCHAR(255)    NOT NULL,
    dob                 DATE            NOT NULL,
<<<<<<< HEAD
    profile_picture     VARCHAR(255)    NOT NULL,
    sockets_id          INTEGER         NOT NULL,
=======
    profile_picture     VARCHAR(255)    NULL,
>>>>>>> 2ae617eba3f1a84381ba245945d63422155ebb1f
    PRIMARY KEY(username)
>>>>>>> 5d669e1c5a960ad9b52ba0beb6a81827d59ce10c
);


CREATE TABLE IF NOT EXISTS posts (
<<<<<<< HEAD
    username        VARCHAR(255)    NOT NULL,
    post_id         SERIAL          NOT NULL,
    title           VARCHAR(255)    NOT NULL,
    body            VARCHAR(255)    NOT NULL,
    price           DECIMAL(10,2)   NOT NULL,
    condition       VARCHAR(255)    NOT NULL,
    posted_date     TIMESTAMP       DEFAULT     CURRENT_TIMESTAMP,
    image_url       VARCHAR(255)    NULL,
    PRIMARY KEY(post_id),
    FOREIGN KEY(username) REFERENCES users(username)
);

CREATE TABLE IF NOT EXISTS user_sessions (
    sid SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    session_id VARCHAR(255) UNIQUE NOT NULL,
    FOREIGN KEY (username) REFERENCES users(username)
);

CREATE TABLE IF NOT EXISTS message_threads (
    thread_id SERIAL PRIMARY KEY,
    sender_username VARCHAR(255) NOT NULL,
    recipient_username VARCHAR(255) NOT NULL,
    UNIQUE (sender_username, recipient_username),
    FOREIGN KEY (sender_username) REFERENCES users(username),
    FOREIGN KEY (recipient_username) REFERENCES users(username)
);

CREATE TABLE IF NOT EXISTS messages (
    message_id SERIAL PRIMARY KEY,
    thread_id INTEGER NOT NULL,
    sender_username VARCHAR(255) NOT NULL,
    recipient_username VARCHAR(255) NOT NULL,
    message_content TEXT,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (thread_id) REFERENCES message_threads(thread_id),
    FOREIGN KEY (sender_username) REFERENCES users(username),
    FOREIGN KEY (recipient_username) REFERENCES users(username)
);
=======
   username        VARCHAR(255)    NOT NULL,
   post_id         SERIAL          NOT NULL,
   title           VARCHAR(255)    NOT NULL,
   body            VARCHAR(255)    NOT NULL,
   price           DECIMAL(10,2)   NOT NULL,
   condition       VARCHAR(255)    NOT NULL,
   posted_date     DATE       DEFAULT     CURRENT_DATE,
   image_url       VARCHAR(255)    NULL,
   PRIMARY KEY(post_id),
   FOREIGN KEY(username) REFERENCES users(username)
);




CREATE TABLE IF NOT EXISTS user_sessions (
 
   sid SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    session_id VARCHAR(255) UNIQUE NOT NULL,
    FOREIGN KEY (username) REFERENCES users(username)
);


CREATE TABLE IF NOT EXISTS message_threads (
    thread_id SERIAL PRIMARY KEY,
    sender_username VARCHAR(255) NOT NULL,
    recipient_username VARCHAR(255) NOT NULL,
    UNIQUE (sender_username, recipient_username),
    FOREIGN KEY (sender_username) REFERENCES users(username),
    FOREIGN KEY (recipient_username) REFERENCES users(username)
);


CREATE TABLE IF NOT EXISTS messages (
    message_id SERIAL PRIMARY KEY,
    thread_id INTEGER NOT NULL,
    sender_username VARCHAR(255) NOT NULL,
    recipient_username VARCHAR(255) NOT NULL,
    message_content TEXT,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (thread_id) REFERENCES message_threads(thread_id),
    FOREIGN KEY (sender_username) REFERENCES users(username),
    FOREIGN KEY (recipient_username) REFERENCES users(username)
);
>>>>>>> 2ae617eba3f1a84381ba245945d63422155ebb1f
