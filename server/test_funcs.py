import sqlite3
import funcs as f
from db import DB


conn = sqlite3.connect('data.db')
def chk(con):
    c = con.cursor()
    rows1 = c.execute("SELECT * FROM CurrentCapacity").fetchall()
    rows2 = c.execute("SELECT * FROM Allocations").fetchall()
    print rows1
    print rows2



f.init_allocations(conn)
f.update_current_capacity(conn)
f.modify_allocation(conn, 1, 1)
f.update_current_capacity(conn)

chk(conn)

print "Getting nearest point 1"
f.get_nearest_spot(conn, 1, 1)
chk(conn)

print "Getting nearest point 2"
f.get_nearest_spot(conn, 1, 1)
chk(conn)

print "Freeing Parking space"
f.free_space(conn, 4)
chk(conn)

