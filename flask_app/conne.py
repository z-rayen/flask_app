import psycopg2

url="postgresql://project_db_98ib_user:U5QleuaLfTqDkKBmFbMCM5uhanXM7CJG@dpg-cjt0okqbgj9c739533v0-a.oregon-postgres.render.com/project_db_98ib"
def connection():

    return  psycopg2.connect(
        host='dpg-cjt0okqbgj9c739533v0-a.oregon-postgres.render.com',
        user='project_db_98ib_user',
        password='U5QleuaLfTqDkKBmFbMCM5uhanXM7CJG',
        database='project_db_98ib'
    )