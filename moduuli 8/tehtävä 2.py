import mysql.connector

db = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='A79777',
    autocommit=True
)

icao_code = input("Enter the ICAO code of an airport: ").upper()

cursor = db.cursor()

sql = """
    SELECT name, municipality
    FROM airport
    WHERE ident = %s
"""

cursor.execute(sql, (icao_code,))
result = cursor.fetchall()

if not result:
    print(f"No airport found with ICAO code {icao_code}")
else:
    for row in result:
        print(f"Airport name: {row[0]}")
        print(f"Location: {row[1]}")