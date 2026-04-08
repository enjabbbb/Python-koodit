import mysql.connector
from flask import Flask, request, jsonify

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game_old',
         user='root',
         password='A79777',
         autocommit=True
         )

def get_airport(icao):
    sql = f"SELECT name, ident, municipality FROM airport WHERE ident = %s"
    cursor = yhteys.cursor()
    cursor.execute(sql, (icao,))
    tulos = cursor.fetchone()
    if tulos:
        name = tulos[0]
        ident = tulos[1]
        municipality = tulos[2]
        return {"name" : name, "ICAO" : ident, "municipality" : municipality}
    else:
        return {"error": f"No airport found with ICAO code {icao}"}

app = Flask(__name__)
@app.route('/kenttä/<string:icao>')
def airport(icao):
    tulos = get_airport(icao)
    return jsonify(tulos)

app.run(use_reloader=True, host='127.0.0.1', port=3000)


