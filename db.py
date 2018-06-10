import sqlite3
from datetime import datetime

def connect(db):
    conn = sqlite3.connect(db)
    return conn

def create(conn):
    tables = [
        {
            'name': 'ir',
        }
    ]
    
    c = conn.cursor()
    for table in tables:
        c.execute('''
                create table {name}
                (date text, time text, value int)
            '''.format(name=table['name']))
    
def get_latest(conn, table, latest=1):
    c = conn.cursor()
    c.execute("select * from {table} order by date, time desc limit {latest}"
        .format(table=table, latest=latest))
    return c.fetchone()

def to_date(datetime):
    return datetime.strftime('%Y-%m-%d')

def to_time(datetime):
    return datetime.strftime('%H:%M:%S')

def log_value(conn, table, value):
    c = conn.cursor()
    now = datetime.now()
    c.execute("insert into {table} values ('{date}', '{time}', {value})"
        .format(table=table, date=to_date(now), time=to_time(now), value=value))
    

def commit(conn):
    conn.commit()

def close(conn):
    conn.close()
