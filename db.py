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
                (date text, time text, value text)
            '''.format(name=table['name']))
    
def get_latest(conn, table, latest=1):
    c = conn.cursor()
    c.execute("select * from {table} order by date, time desc limit {latest}"
        .format(table=table, latest=latest))
    return c.fetchall()

def to_date(datetime):
    return datetime.strftime('%Y-%m-%d')

def to_time(datetime):
    return datetime.strftime('%H:%M:%S')


def delete_all_but_latest(conn, table, latest=None):
    if latest is None:
        # should keep about 7 days of data:
        latest = 60*60*24 / 5 * 7
    c = conn.cursor()
    c.execute("""
        delete from {table}
        where (date, time) not in (
            select date, time from {table}
            order by date, time desc
            limit {latest}
        )
    """.format(table=table, latest=latest))


def log_value(conn, table, value):
    c = conn.cursor()
    delete_all_but_latest(conn, table)
    now = datetime.now()
    c.execute("insert into {table} values ('{date}', '{time}', '{value}')"
        .format(table=table, date=to_date(now), time=to_time(now), value=str(value)))
    commit(conn)
    
def commit(conn):
    conn.commit()

def close(conn):
    conn.close()
