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
    results = food_search(food_name)
    foods = []
    for result in results:
        food = result.get('food', {})
        foods.append([
            food.get('label'),
            food.get('category'),
            food.get('nutrients', {})
        ])
    return foods

if __name__ == '__main__':
    food_name = input('Enter a food name to search: ')
    food_results = run_food_search(food_name)

    if food_results:
        for result in food_results:
            print(f"Food: {result[0]}")
            print(f"Category: {result[1]}")
            print("Nutrients:")
            for nutrient, value in result[2].items():
                print(f"  {nutrient}: {value}")
            print("----------------------")
    else:
        print(f"No results found for {food_name}.")
