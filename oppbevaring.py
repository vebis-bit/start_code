import requests
lager = {"eple": 1000 
    ,"banan": 300
    ,"appelsin": 1000
    ,"melon": 1000
}


api_key = '92c3bcf84731f6098ecf4e793b53ad1e'
base_url = 'https://api.edamam.com/api/recipes/v2'
endpoint = '/search'
query = 'chicken'  # Endre dette til ditt søkeord

# Sett opp parametre for forespørselen
params = {
    'q': query,
    'app_id': 'DIN_APP_ID',  # Erstatt med din app-id hvis nødvendig
    'app_key': api_key,
}

# Lag HTTP GET-forespørsel
response = requests.get(f'{base_url}{endpoint}', params=params)

# Håndter responsen
if response.status_code == 200:
    data = response.json()
    # Behandle dataene her
    for hit in data.get('hits', []):
        recipe = hit.get('recipe', {})
        print(f"Oppskrift: {recipe.get('label')}")
        print(f"Lenke: {recipe.get('url')}")
        print("----------------------")
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