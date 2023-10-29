from typing import Any

import requests


def recipe_search(meal_type: str, ingredient: str, health_restriction: str):
    with requests.get(
        'https://api.edamam.com/api/recipes/v2',
        headers={'Accept': 'application/json'},
        params={
            'app_id': '64a8539d',
            'app_key': '5b6d901e27fd64a68ff9ac4a59e4321e',
            'type': 'any',
            'mealType': meal_type,
            'health': health_restriction,
            'q': ingredient,
        },
    ) as result:
        result.raise_for_status()
        data = result.json()
    return data['hits']

def run_recipe_search(has_meal_type, has_restriction, ingredient):
    if has_meal_type == 'yes':
          meal_type = input(
              'Select an option from the following list:'
              '\n - breakfast'
              '\n - brunch'
              '\n - lunch'
              '\n - snack'
              '\n - teatime'
              '\n > '
          )
    else:
        meal_type = None

    if has_restriction == 'yes':
        health_restriction = input(
            'Select an option from the following list:'
            '\n - vegan'
            '\n - vegetarian'
            '\n - paleo'
            '\n - dairy-free'
            '\n - gluten-free'
            '\n - wheat-free'
            '\n - fat-free'
            '\n - low-sugar'
            '\n - egg-free'
            '\n - peanut-free'
            '\n - tree-nut-free'
            '\n - soy-free'
            '\n - fish-free'
            '\n - shellfish-free'
            '\n >'
        )
    else:
        health_restriction = None

    results = recipe_search(meal_type, ingredient, health_restriction)
    recepies = []
    for result in results:
        recipe = result['recipe']
        recepies.append([recipe['label'],
                         
                         recipe['ingredientLines'],
                         recipe['calories'],
                         #recipe['dishType'],
                         recipe['totalTime'],
                         recipe['ingredients']
                         ])
    return recepies

if __name__ == '__main__':
    print(run_recipe_search("breakfeast", "none", "apple"))
    