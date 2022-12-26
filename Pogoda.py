import requests
city = input("Enter city: ")
r = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=5ad7b8fca6310aff7d3bdd2d7d6a2631&units=metric")
data = r.json()
print(f"It is {data['main']['temp']} in {city}")

