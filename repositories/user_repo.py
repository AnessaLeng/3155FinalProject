from typing import Any
from repositories.db import get_pool
from psycopg.rows import dict_row

def does_email_exist(email: str) -> bool:
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute('''
                        SELECT 
                            email
                        FROM 
                            users
                        WHERE 
                            email = %s;
                    ''', [email])
            user = cur.fetchone()
            return user is not None
        
def create_user(email: str, first_name: str, last_name: str, password: str, dob: str, profile_image: str) -> dict[str, Any] | None:
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute('''
                        INSERT INTO users (email, first_name, last_name, password, dob, profile_image)
                        VALUES (%s, %s, %s, %s, %s, %s)
                        RETURNING user_id
                    ''', [email, first_name, last_name, password, dob, profile_image])
            user_id = cur.fetchone()
            if user_id is None:
                return None
            return {
                "user_id": user_id,
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                "profile_image": profile_image
            }

def get_user_by_email(email:str) -> dict[str, Any] | None:
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute('''
                        SELECT 
                            user_id,
                            email,
                            first_name,
                            last_name,
                            password AS hashed_password,
                            dob,
                            profile_image
                        FROM 
                            users
                        WHERE 
                            email = %s;
                    ''', [email])
            user = cur.fetchone()
            return user
        
def get_user_by_id(user_id: int) -> dict[str, Any] | None:
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute('''
                        SELECT 
                            user_id,
                            email,
                            first_name,
                            last_name,
                            password AS hashed_password,
                            dob,
                            profile_image
                        FROM 
                            users
                        WHERE 
                            user_id = %s;
                    ''', [user_id])
            user = cur.fetchone()
            return user