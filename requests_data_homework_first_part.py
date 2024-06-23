import requests
from pywebio.output import put_html

url = "http://api.open-notify.org/astros.json"

list_of_astronauts_iss = []
list_of_astronauts_tiangong = []


def get_status_of_astronauts():
    response = requests.get(url=url)
    response_json = response.json()
    astronauts = response_json['people']

    list_of_astronauts_iss = []
    list_of_astronauts_tiangong = []

    for person in astronauts:
        if person["craft"] == "ISS":
            list_of_astronauts_iss.append(person["name"])
        elif person["craft"] == "Tiangong":
            list_of_astronauts_tiangong.append(person["name"])

    return list_of_astronauts_iss, list_of_astronauts_tiangong


start_function_get_astronauts = get_status_of_astronauts()

put_html(f'<h1>ISS Astronauts: {start_function_get_astronauts[0]}')
put_html(f'<h1>Tiangong Astronauts: {start_function_get_astronauts[1]}')
