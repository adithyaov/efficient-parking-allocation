import sqlite3

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
            c.execute('''INSERT INTO DistanceGraph(p_lot_id, destination_id, distance)
                            VALUES ({pid}, {did}, {dist})'''\
                                .format(pid=p, did=d, dist=destinations[d][p]))
    conn.commit()
    return "Ta-da!"


@app.route('/get/pspaces', methods=['GET'])
def get_pspaces():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    rows = c.execute("SELECT id, name FROM PSpace").fetchall()
    return jsonify(map(lambda x: {"id": x[0], "name": x[1]}, rows)

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

app.run(host='0.0.0.0', port=8080)
