from repositories.db import get_pool
from psycopg.rows import dict_row
from flask import redirect, url_for
from flask import Flask, session

def get_all_posts():
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute(''' 
                           SELECT
                                username,
                                post_id,
                                title,
                                body,
                                price,
                                condition,
                                image_url,
                                posted_date
                           FROM
                                posts
                            ''')
            return cursor.fetchall()


def get_searched_posts(title: str):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute(''' 
                           SELECT
                                username,
                                post_id,
                                title,
                                body,
                                price,
                                condition,
                                image_url,
                                posted_date
                           FROM
                                posts
                           WHERE
                                title ILIKE %s
                            ''', ['%' + title + '%'])
            search_result = cursor.fetchall()
    return search_result


def get_post_by_id(post_id):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute(''' 
                           SELECT
                                username,
                                post_id,
                                title,
                                body,
                                condition,
                                price,
                                image_url,
                                posted_date
                           FROM
                                posts
                           WHERE
                                post_id = %s
                            ''', [post_id])
            return cursor.fetchone()
        

def get_posts_by_username(username):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute(''' 
                           SELECT
                                username,
                                post_id,
                                title,
                                body,
                                condition,
                                price,
                                image_url,
                                posted_date
                           FROM
                                posts
                           WHERE
                                username = %s
                            ''', [username])
            return cursor.fetchall()

# testing update and delete post
# post_repo.py

def update_post(post_id, title, body, price=None, condition=None, image_url=None):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cur:
            if price is not None and condition is not None and image_url is not None:
                cur.execute('''
                            UPDATE posts 
                            SET title = %s, body = %s, price = %s, condition = %s, image_url = %s
                            WHERE post_id = %s;
                            ''', (title, body, price, condition, image_url, post_id))
            elif price is not None and condition is not None:
                cur.execute('''
                            UPDATE posts 
                            SET title = %s, body = %s, price = %s, condition = %s
                            WHERE post_id = %s;
                            ''', (title, body, price, condition, post_id))
            elif price is not None and image_url is not None:
                cur.execute('''
                            UPDATE posts 
                            SET title = %s, body = %s, price = %s, image_url = %s
                            WHERE post_id = %s;
                            ''', (title, body, price, image_url, post_id))
            elif condition is not None and image_url is not None:
                cur.execute('''
                            UPDATE posts 
                            SET title = %s, body = %s, condition = %s, image_url = %s
                            WHERE post_id = %s;
                            ''', (title, body, condition, image_url, post_id))
            elif price is not None:
                cur.execute('''
                            UPDATE posts 
                            SET title = %s, body = %s, price = %s
                            WHERE post_id = %s;
                            ''', (title, body, price, post_id))
            elif condition is not None:
                cur.execute('''
                            UPDATE posts 
                            SET title = %s, body = %s, condition = %s
                            WHERE post_id = %s;
                            ''', (title, body, condition, post_id))
            elif image_url is not None:
                cur.execute('''
                            UPDATE posts 
                            SET title = %s, body = %s, image_url = %s
                            WHERE post_id = %s;
                            ''', (title, body, image_url, post_id))
            else:
                cur.execute('''
                            UPDATE posts 
                            SET title = %s, body = %s
                            WHERE post_id = %s;
                            ''', (title, body, post_id))
            conn.commit()


def delete_post(post_id):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                DELETE FROM posts
                WHERE post_id = %s
            ''', (post_id))
            conn.commit()
    # Redirect back to the profile page after deleting the post
    return redirect(url_for('show_profile', username=session['username']))

