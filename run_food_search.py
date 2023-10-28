import requests

def food_search(food_name: str):
    api_id = 'af2ff285'
    api_key = '12f6fae7d6dfcd5ca9e941a89e3b0acb'

    params = {
        'app_id': api_id,
        'app_key': api_key,
        'ingr': food_name,
    }

    response = requests.get('https://api.edamam.com/api/food-database/v2/parser', headers={'Accept': 'application/json'}, params=params)
    response.raise_for_status()

    data = response.json()
    return data.get('hints', [])

def run_food_search(food_name):
    top_search = 0
    results = food_search(food_name)
    return {results[top_search].get('food').get('label') : results[top_search].get('measures')[0]['weight']}

if __name__ == '__main__':
    food_name = input('Enter a food name to search: ')
    food_results = run_food_search(food_name)

    if food_results:
        print(f"Food: {food_results}")
        print("----------------------")
    else:
        print(f"No results found for {food_name}.")
