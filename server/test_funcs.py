import sqlite3
import funcs as f
from db import DB


def chk():
    db = DB(dbtype='sqlite', filename='./data.db')
    print db.tables.Allocations.head()
    print db.tables.CurrentCapacity.head()
    print db.tables.TempReserves.head()



conn = sqlite3.connect('data.db')
f.init_allocations(conn)
f.update_current_capacity(conn)
f.modify_allocation(conn, 1, 1)
f.update_current_capacity(conn)

chk()

f.get_nearest_spot(conn, 1, 1)
chk()

f.get_nearest_spot(conn, 1, 1)
chk()

f.free_space(conn, 4)
chk()

