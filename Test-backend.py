from foreslaa_oppskrifter import getAbleRecepies
from oppbevaring import *

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allowing CORS for all domains (change this to your frontend's domain in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#res = run_recipe_search("dinner","no","beef")
#ingred = makeObject(res[0])

inventory = [{'name':'eggs', 'amt':40},
             {'name':'meat', 'amt':40},
             {'name':'cheese', 'amt':40},
             {'name':'eggs', 'amt':40}]


# for i in ingred:
#     fake_items.append(i[0:1])
# print(fake_items)
# Sample data
#fake_items = [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]

def get_multiple_lists():
    list_one = {
        "Ost": 392503,
        "kjeks": 2359,
        "bæsj": 123192
    }

    list_two = ['a', 'b', 'c', 'd', 'e']
    list_three = [10.5, 20.2, 30.7, 40.9, 50.1]

    # Create a dictionary to hold the lists
    response_data = {
        "listOne": list_one,
        "listTwo": list_two,
        "listThree": list_three
    }
    return response_data

def get_name_ablerecepies():
    ablerecepies = getAbleRecepies()
    names = {}
    for i in ablerecepies:
        names.update({'name':i[0]})
    print(names)
    return names

fake_items = get_multiple_lists()
ablerecepiesNames = get_name_ablerecepies()

@app.get("/items")
async def read_items():
    return fake_items

@app.get("/ablerecepiesNames")
async def read_recepies():
    return ablerecepiesNames