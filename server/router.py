import sqlite3

conn = sqlite3.connect('data.db')
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.route('/post/lots')
def post_lots():
    c = conn.cursor()
    content = request.get_json()
    for x in content:
        c.execute('''INSERT INTO PLot (name, lat, long, capacity)
                        VALUES ({name}, {lat}, {long}, {capacity})''')\
                            .format(name=x['name'], lat=x['lat'], long=x['long'], capacity=x['capacity'])
    conn.commit()
    return "Ta-da!"

@app.route('/post/destinations')
def post_destinations():
    c = conn.cursor()
    content = request.get_json()
    for x in content:
        c.execute('''INSERT INTO Destinations (name, lat, long)
                        VALUES ({name}, {lat}, {long})''')\
                            .format(name=x['name'], lat=x['lat'], long=x['long'])
    conn.commit()
    return "Ta-da!"

@app.route('/get/lots')
def get_lots():
    c = conn.cursor()
    rows = c.execute("SELECT id, name FROM PLot").fetchall()
    return jsonify(rows)

@app.route('/get/destinations')
def get_lots():
    c = conn.cursor()
    rows = c.execute("SELECT id, name FROM Destinations").fetchall()
    return jsonify(rows)


@app.route('/post/interconnects')
def post_interconnects():
    c = conn.cursor()
    destinations = request.get_json()
    for d in destinations.keys():
        for p in destinations[d].keys():
            c.execute('''INSERT INTO DistanceGraph(p_lot_id, destination_id, distance)
                            VALUES ({pid}, {did}, {dist})''')\
                                .format(pid=p, did=d, dist=destinations[d][p])
    conn.commit()
    return "Ta-da!"


@app.route('/get/pspaces')
def post_pspaces():
    c = conn.cursor()
    rows = c.execute("SELECT id, name FROM PSpace").fetchall()
    return jsonify(rows)

@app.route('/get/pspaceimage/<id>')
def get_pspaceimage(id):
    # SOMEHOW GET IMAGE BINARY !!!
    response = make_response(image_binary)
    response.headers.set('Content-Type', 'image/jpeg')
    return response

@app.route('/post/pspaces')
def post_pspaces():
    c = conn.cursor()
    content = request.get_json()
    for x in content:
        c.execute('''UPDATE PSpace set name={name}
                        WHERE id={id}'''\
                            .format(id=x['id'], name=x['name']))
    conn.commit()
    return "Ta-da!"

