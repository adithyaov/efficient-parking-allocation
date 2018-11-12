import sys
sys.path.insert(0, '../imageProcessing/class')
from modules import get_feed_points, mark_points

def update_current_capacity(conn):
    c = conn.cursor()
    rows = c.execute('''SELECT P.p_lot_id AS lid, P.group_id AS gid, COUNT(*) AS c FROM Allocations as A 
                            INNER JOIN PSpace AS P ON A.p_space_id = P.id 
                            WHERE A.reserved=0 
                            GROUP BY P.p_lot_id, P.group_id''').fetchall()
    for row in rows:
        c.execute("INSERT OR IGNORE INTO CurrentCapacity (p_lot_id, group_id, capacity) VALUES ({lid}, {gid}, {c})"\
                    .format(lid=row[0], gid=row[1], c=row[2]))
        c.execute("UPDATE CurrentCapacity SET capacity = {c} WHERE p_lot_id={lid} and group_id={gid}"\
                    .format(c=row[2], lid=row[0], gid=row[1]))
    conn.commit()

def get_nearest_spot(conn, did, gid):
    c = conn.cursor()
    rows = c.execute('''SELECT C.p_lot_id as pid FROM DistanceGraph as D 
                            INNER JOIN CurrentCapacity as C on C.p_lot_id = D.p_lot_id
                            WHERE C.group_id = {gid}
                                AND capacity > 0
                                AND destination_id = {did}
                            ORDER BY D.distance'''\
                                .format(did=did, gid=gid)).fetchall()
    row = rows[0]
    lid = row[0]

    rows = c.execute('''SELECT id, name FROM PSpace as P
                            INNER JOIN Allocations AS A ON A.p_space_id = P.id
                            WHERE P.p_lot_id = {lid}
                                AND P.group_id = {gid}
                                AND A.reserved = 0'''\
                                    .format(lid=lid, gid=gid)).fetchall()

    row = rows[0]
    pid = row[0]
    pname = row[1]
    c.execute('''UPDATE Allocations set reserved = 1
                    WHERE p_space_id = {pid}'''\
                        .format(pid=pid))
    update_current_capacity(conn)
   
    tt = temp_time(did)
    c.execute('''INSERT INTO TempReserves (p_space_id, till_timestamp)
                    VALUES ({pid}, {tt})'''\
                        .format(pid=pid, tt=tt))
    
    print lid, pid, pname
    conn.commit()

def temp_time(did):
    return 4

def free_space(conn, pid):
    c = conn.cursor()
    c.execute('''UPDATE Allocations SET reserved = 0 
                    WHERE p_space_id = {pid}'''\
                        .format(pid=pid))
    update_current_capacity(conn)
    conn.commit()

def modify_allocation(conn, id, reserved):
    c = conn.cursor()
    c.execute('''INSERT OR IGNORE INTO Allocations (p_space_id, reserved)
                    VALUES ({id}, {reserved})'''\
                        .format(id=id, reserved=reserved))
    c.execute('''UPDATE Allocations SET reserved = {reserved}
                    WHERE p_space_id = {id}'''\
                        .format(id=id, reserved=reserved))
    conn.commit()

def init_allocations(conn):
    c = conn.cursor()
    rows = c.execute("SELECT id FROM PSpace").fetchall()
    for row in rows:
        modify_allocation(conn, row[0], 0)
    
def init_prob(conn, p_lot_id):
    points = get_feed_points(p_lot_id) # Change this!
    c = conn.cursor()
    for point in points:
        c.execute("INSERT OR IGNORE INTO PSpace (p_lot_id, x, y) VALUES ({lid}, {x}, {y})"\
                        .format(lid=p_lot_id, x=point[0], y=point[1]))
    conn.commit()
    rows = c.execute('''SELECT x, y, id FROM PSpace
                            WHERE p_lot_id={lid}'''\
                                .format(lid=p_lot_id)).fetchall()
    marked_blob = mark_points(p_lot_id, rows) #return blob
    return marked_blob

 
