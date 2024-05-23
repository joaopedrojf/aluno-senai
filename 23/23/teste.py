import requests()

weather_url = "http://wttr.in/São Paulo "
try:       
    response = requests.get(weather_url)
    data = response.text
    if response.status_code == 200: 
    print(data)

    except Exception as e:
    print(" Ocorreu um erro ao acessar a API " )
