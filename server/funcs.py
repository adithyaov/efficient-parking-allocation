def update_current_capacity(conn):
    c = conn.cursor()
    rows = c.execute('''SELECT P.p_lot_id AS lid, P.group_id AS gid, COUNT(*) AS c FROM Allocations as A 
                            INNER JOIN PSpace AS P ON A.p_space_id = P.id 
                            WHERE A.reserved=False 
                            GROUP BY P.p_lot_id, P.group_id''').fetchall()
    print rows
    for row in rows:
        c.execute("INSERT OR IGNORE INTO CurrentCapacity (p_lot_id, group_id, capacity) VALUES ({lid}, {gid}, {c})"\
                    .format(lid=row['lid'], gid=row['gid'], c=row['c']))
        c.execute("UPDATE CurrentCapacity SET capacity = {c} WHERE p_lot_id={lid} and group_id={gid}"\
                    .format(c=row['c'], lid=row['lid'], gid=row['gid']))

def get_nearest_spot(conn, did, gid):
    c = conn.cursor()
    rows = c.execute('''SELECT C.p_lot_id as pid FROM DistanceGraph as D 
                            INNER JOIN CurrentCapacity as C on C.p_lot_id = D.p_lot_id
                            WHERE C.group_id = {gid}
                                AND capacity > 0
                                AND destination_id = {did}
                            ORDER BY D.distance'''\
                                .format(did=did, gid=gid)).fetchall()
    print rows

def modify_allocation(conn, id, reserved):
    c = conn.cursor()
    c.execute('''INSERT OR IGNORE INTO Allocations (p_space_id, reserved)
                    VALUES ({id}, {reserved})'''\
                        .format(id=id, reserved=reserved))
    c.execute('''UPDATE Allocations SET reserved = {reserved}
                    WHERE p_space_id = {id}'''\
                        .format(id=id, reserved=reserved))

def init_allocations(conn):
    c = conn.cursor()
    rows = c.execute("SELECT id FROM PSpace").fetchall()
    for row in rows:
        modify_allocation(conn, row['id'], False)
    
    
    
