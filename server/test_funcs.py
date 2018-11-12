import sqlite3
import funcs as f
from db import DB

conn = sqlite3.connect('data.db')
f.init_allocations(conn)
f.update_current_capacity(conn)
f.modify_allocation(conn, 1, 1)
f.update_current_capacity(conn)

db = DB(dbtype='sqlite', filename='./data.db')
f.get_nearest_spot(conn, 1, 1)
f.get_nearest_spot(conn, 1, 1)
print db.tables.Allocations.head()
print db.tables.CurrentCapacity.head()
print db.tables.TempReserves.head()
