# from repositories.db import get_pool
# from psycopg.rows import dict_row

# #for Nhu's explore feature
# def get_all_posts():
#     pool = get_pool()
#     with pool.connection() as conn:
#         with conn.cursor(row_factory=dict_row) as cursor:
#             cursor.execute(''' 
#                            SELECT
#                                 user_id,
#                                 username,
#                                 post_id,
#                                 title,
#                                 body,
#                                 posted_date
#                            FROM
#                                 posts
#                             ''')
#             return cursor.fetchall()

# #for Nhu's search feature
# def get_searched_posts(title: str):
#     pool = get_pool()
#     with pool.connection() as conn:
#         with conn.cursor(row_factory=dict_row) as cursor:
#             cursor.execute(''' 
#                            SELECT
#                                 user_id,
#                                 username,
#                                 post_id,
#                                 title,
#                                 body,
#                                 posted_date
#                            FROM
#                                 posts
#                            WHERE
#                                 title = %s;
#                             ''', [title])
#             return cursor.fetchall()