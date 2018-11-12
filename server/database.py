'''
PLot:
    id
    name
    lat
    long
    capacity

Destinations:
    id
    name
    lat
    long

DistanceGraph:
    parking_id
    destination_id
    distance

PSpace:
    p_lot_id
    id
    group_id
    name

PSpacePixPos:
    p_space_id
    x
    y

PGroup:
    id
    name
'''

import sqlite3
conn = sqlite3.connect('data.db')

c = conn.cursor()
c.execute('''INSERT INTO PGroup (name) 
                VALUES 
                    ('General'),
                    ('Senior'),
                    ('Handicapped')''')
conn.commit()

with open('./sql/tables.sql','r') as f:
    sql_table_creation = f.read()


with open('./sql/mock.sql','r') as f:
    sql_mock = f.read()


with sqlite3.connect('data.db') as conn:
    c = conn.cursor()
    c.executescript(sql_table_creation)
    # c.executescript(sql_mock)
    conn.commit()
