def update_current_capacity(conn):
    c = conn.cursor()
    rows = c.execute('''SELECT P.p_lot_id AS lid, P.group_id AS gid, COUNT(*) AS c FROM Allocations as A 
                            INNER JOIN PSpace AS P ON A.p_space_id = P.id 
                            WHERE A.reserved=False 
                            GROUP BY P.p_lot_id, P.group_id''').fetchall()
    print rows
    for row in rows:
        c.execute("INSERT OR IGNORE INTO CurrentCapacity (p_lot_id, group_id, capacity) VALUES ({0}, {1}, {2})"\
                .format(row['lid'], row['gid'], row['c']))
        c.execute("UPDATE CurrentCapacity SET capacity = c WHERE p_lot_id=lid and group_id=gid")

def get_nearest_spot(conn):
    c = conn.cursor()
    rows = c.execute('''SELECT C.p_lot_id as pid FROM DistanceGraph as D 
                            INNER JOIN CurrentCapacity as C on C.p_lot_id = D.p_lot_id
                            WHERE C.group_id = __gid
                                AND capacity > 0
                            ORDER BY D.distance''').fetchall()
    print rows
