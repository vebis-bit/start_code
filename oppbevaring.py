import requests
lager = {"eple": 1000 
    ,"banan": 300
    ,"appelsin": 1000
    ,"melon": 1000
}


api_key = '92c3bcf84731f6098ecf4e793b53ad1e'
url = 'https://api.spoonacular.com/recipes/random'
parameters = {'apiKey': api_key, 'number': 1}

response = requests.get(url, params=parameters)

if response.status_code == 200:
    data = response.json()
    # Behandle dataene her
    print(data)
else:
    print(f'Feil ved henting av data. Statuskode: {response.status_code}')


fruktsalat = {
    "eple": 200
    ,"banan": 100
    ,"appelsin": 100
    ,"melon": 100
}

def lag_oppskrift(lager, oppskrit):
    for key,value in oppskrit.items():
        if key in lager:
            lager[key] -= value
        else:
            lager[key] = -value
    return lager
print(lag_oppskrift(lager, fruktsalat))