import json
import requests

sarja = input("Anna sarja minkä tiedot haluat: ")

pyyntö = "https://api.tvmaze.com/search/shows?q=" + sarja
vastaus = requests.get(pyyntö).json()
print(json.dumps(vastaus, indent=2))

