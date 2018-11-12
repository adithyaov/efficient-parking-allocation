import sqlite3
import funcs as f
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/post/lots', methods=['POST'])
def post_lots():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    content = request.get_json()
    for x in content:
        c.execute('''INSERT INTO PLot (name, lat, long, capacity)
                        VALUES ("{name}", {lat}, {long}, {capacity})'''\
                            .format(name=x['name'], lat=x['lat'], long=x['long'], capacity=x['capacity']))
    conn.commit()
    return "Ta-da!"

@app.route('/post/destinations', methods=['POST'])
def post_destinations():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    content = request.get_json()
    for x in content:
        c.execute('''INSERT INTO Destinations (name, lat, long)
                        VALUES ("{name}", {lat}, {long})'''\
                            .format(name=x['name'], lat=x['lat'], long=x['long']))
    conn.commit()
    return "Ta-da!"

@app.route('/get/lots', methods=['GET'])
def get_lots():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    rows = c.execute("SELECT id, name FROM PLot").fetchall()
    return jsonify(map(lambda x: {"id": x[0], "name": x[1]}, rows))


@app.route('/get/groups', methods=['GET'])
def get_groups():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    rows = c.execute("SELECT id, name FROM PGroup").fetchall()
    return jsonify(map(lambda x: {"id": x[0], "name": x[1]}, rows))




@app.route('/get/destinations', methods=['GET'])
def get_destinations():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    rows = c.execute("SELECT id, name FROM Destinations").fetchall()
    return jsonify(map(lambda x: {"id": x[0], "name": x[1]}, rows))


@app.route('/post/interconnects', methods=['POST'])
def post_interconnects():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    destinations = request.get_json()
    for d in destinations.keys():
        for p in destinations[d].keys():
            c.execute('''INSERT OR IGNORE INTO DistanceGraph(p_lot_id, destination_id, distance)
                            VALUES ({pid}, {did}, {dist})'''\
                                .format(pid=p, did=d, dist=destinations[d][p]))
            c.execute('''UPDATE DistanceGraph set distance = {dist}
                            WHERE p_lot_id = {pid}
                                AND destination_id = {did}'''\
                                    .format(pid=p, did=d, dist=destinations[d][p]))
    conn.commit()
    return "Ta-da!"

@app.route('/get/interconnects', methods=['GET'])
def get_interconnects():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    rows = c.execute("SELECT p_lot_id, destination_id, distance FROM DistanceGraph").fetchall()
    return jsonify(map(lambda x: {"p_lot_id": x[0], "destination_id": x[1], "distance": x[2]}, rows)) 

@app.route('/get/pspaces', methods=['GET'])
def get_pspaces():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    rows = c.execute("SELECT id, name FROM PSpace").fetchall()
    return jsonify(map(lambda x: {"id": x[0], "name": x[1]}, rows))

@app.route('/get/pspaceimage/<id>', methods=['GET'])
def get_pspaceimage(id):
    # SOMEHOW GET IMAGE BINARY !!!
    response = make_response(image_binary)
    response.headers.set('Content-Type', 'image/jpeg')
    return response

@app.route('/post/pspaces', methods=['POST'])
def post_pspaces():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    content = request.get_json()
    for x in content:
        c.execute('''UPDATE PSpace set name="{name}"
                        WHERE id={id}'''\
                            .format(id=x['id'], name=x['name']))
    conn.commit()
    return "Ta-da!"

@app.route('/get/probe-ids-init/<p_lot_id>', methods=['GET'])
def probe_init_ids(p_lot_id):
    p_lot_id = int(p_lot_id)
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    rows = c.execute('''SELECT id, name FROM PSpace
                            WHERE p_lot_id={lid}'''\
                                .format(lid=p_lot_id)).fetchall()
    return jsonify(map(lambda x: {"id": x[0], "name": x[1]}, rows))

@app.route('/get/probe-image-init/<p_lot_id>', methods=['GET'])
def probe_init_image(p_lot_id):
    p_lot_id = int(p_lot_id)
    conn = sqlite3.connect('data.db')
    marked_blob = f.init_prob(conn, p_lot_id)
    response = make_response(marked_blob)
    response.headers.set('Content-Type', 'image/jpeg')
    return response

@app.route('/get/parkingspace/<did>/<gid>', methods=['GET'])
def get_eff_p(did, gid):
    did = int(did)
    gid = int(gid)
    conn = sqlite3.connect('data.db')
    nps = f.get_nearest_spot(conn, did, gid)
    if nps == None:
        return "Error", 404
    return jsonify(nps)

@app.route('/get/parkinglots-poll', methods=['GET'])
def get_poll():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    rows = c.execute("SELECT * FROM PLot").fetchall()
    l = []
    for row in rows:
        rs = c.execute('''SELECT G.id, G.name, C.capacity FROM CurrentCapacity AS C
                            INNER JOIN PGroup AS G ON G.id = C.group_id
                            WHERE C.p_lot_id={lid}'''\
                            .format(lid=row[0]))
        l.append({
            'id': row[0],
            'name': row[1],
            'lat': row[2],
            'long': row[3],
            'capacity': row[4],
            'freespace': map(lambda x: {'id': x[0], 'name': x[1], 'capacity': x[2]}, rs)
            })

    return jsonify(l)

app.run(host='0.0.0.0', port=8080)
