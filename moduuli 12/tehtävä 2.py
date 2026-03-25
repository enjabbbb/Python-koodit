import requests

API_key = "f786fbb4e490bba97728e51e642f9f19"

paikka = input("Enter municipality name: ")


def inputs(API_key, paikka):
    try:
        request = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={paikka}&appid={API_key}&units=metric")
        if request.status_code == 200:
            data = request.json()
            print(f"Weather in {paikka}: {data['weather'][0]['description']}")
            print(f"Temperature: {data['main']['temp']}°C")
        else:
            print(f"Error: {request.status_code} - {request.reason}")
    except requests.exceptions.RequestException as e:
        print(f"Virhe: {e}")


inputs(API_key, paikka)
