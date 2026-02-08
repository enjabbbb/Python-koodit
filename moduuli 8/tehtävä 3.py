import mysql.connector
from geopy.distance import geodesic


def get_airport_coordinates(icao_code):
    db = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='A79777',
        autocommit=True
    )

    cursor = db.cursor()

    sql = """
        SELECT latitude_deg, longitude_deg
        FROM airport
        WHERE ident = %s
    """

    cursor.execute(sql, (icao_code,))
    result = cursor.fetchone()

    cursor.close()
    db.close()

    return result


def run_airport_distance():
    icao1 = input("Enter the ICAO code of the first airport: ").upper()
    icao2 = input("Enter the ICAO code of the second airport: ").upper()

    coord1 = get_airport_coordinates(icao1)
    coord2 = get_airport_coordinates(icao2)

    if not coord1 or not coord2:
        print("One or both ICAO codes were not found.")
        return

    distance_km = geodesic(coord1, coord2).kilometers

    print(f"\nDistance between {icao1} and {icao2}: {distance_km:.2f} kilometers")


run_airport_distance()
