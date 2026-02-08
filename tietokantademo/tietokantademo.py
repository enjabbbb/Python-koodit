import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='A79777',
         autocommit=True
         )

def hae_data():
    sql = "SELECT * FROM airport LIMIT 10"
    sql2 = "SELECT country. FROM country"

    cursor = yhteys.cursor()
    cursor.execute(sql)
    tulos = cursor.fetchall()

    print(tulos[0])
    print(tulos[0][0])

    for rivi in tulos:
        print(rivi)

       # (a,b,c) =rivi

        id = rivi[0]
       # print (F'name: {name}')
        print(F'id: {id}')


        for alkio in rivi:
            print(" ", alkio)

hae_data()

