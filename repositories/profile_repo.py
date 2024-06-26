from repositories.db import get_pool
from psycopg.rows import dict_row


def get_profile_info():
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''      
                           SELECT
                                username,
                                biography,
                                profile_picture
                           FROM
                                users
                            ''')
            return cursor.fetchall()
        
def get_profile_by_email(email):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''      
                           SELECT
                                username,
                                biography,
                                profile_picture
                           FROM
                                users
                           WHERE
                                email = %s
                            ''',[email])
            return cursor.fetchone()

def get_profile_by_username(username):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''      
                           SELECT
                                username,
                                biography,
                                profile_picture
                           FROM
                                users
                           WHERE
                                username = %s
                            ''',[username])
            return cursor.fetchone()
        
def update_profile(email, username=None, bio=None, img_url=None):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            if(username is not None and bio is not None and img_url is not None):
               cursor.execute('''      
                              UPDATE users
                              SET username = %s, biography = %s, profile_picture = %s
                              WHERE email = %s;
                              ''',(username, bio, img_url, email))
            elif(username is not None and bio is not None):
               cursor.execute('''      
                              UPDATE users
                              SET username = %s, biography = %s
                              WHERE email = %s;
                              ''',(username, bio, email))
            elif(username is not None and img_url is not None):
                 cursor.execute('''      
                              UPDATE users
                              SET username = %s, profile_picture = %s
                              WHERE email = %s;
                              ''',(username, img_url, email))
            elif(bio is not None and img_url is not None):
                 cursor.execute('''      
                              UPDATE users
                              SET biography = %s, profile_picture = %s
                              WHERE email = %s;
                              ''',(bio, img_url, email))
            elif(username is not None):
                 cursor.execute('''      
                              UPDATE users
                              SET username = %s
                              WHERE email = %s;
                              ''',(username, email))
            elif(bio is not None):
                 cursor.execute('''      
                              UPDATE users
                              SET biography = %s
                              WHERE email = %s;
                              ''',(bio, email))
            elif(img_url is not None):
                 cursor.execute('''      
                              UPDATE users
                              SET profile_picture = %s
                              WHERE email = %s;
                              ''',(img_url, email))
            else:
                 pass
            conn.commit()
