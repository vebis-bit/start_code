from foreslaa_oppskrifter import *
from pydantic import BaseModel
from run_recipe_search import *
from run_food_search import *
from foreslaa_oppskrifter import *
#from oppbevaring import *

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

# for i in ingred:
#     fake_items.append(i[0:1])
# print(fake_items)
# Sample data
#fake_items = [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]
def get_multiple_lists():
    list_one = ingredienser

    list_two = ['a', 'b', 'c', 'd', 'e']
    list_three = [10.5, 20.2, 30.7, 40.9, 50.1]

    # Create a dictionary to hold the lists
    response_data = {
        "listOne": list_one,
        "listTwo": list_two,
        "listThree": list_three
    }
    return response_data

def get_ablerecepies():
    ablerecepies = getAbleRecepies()
    names = {}
    print(len(ablerecepies))
    for i in range(len(ablerecepies)):
        names[ablerecepies[i][0]] = ablerecepies[i][0]
    
    print("ABLE RECEPIES",names)
    return {'names':names}

def get_suggested_recepies():
    suggestedrecepies = run_recipe_search("dinner", "no", "pizza")
        
    names = {}
    print(len(suggestedrecepies))
    print(suggestedrecepies[0])
    for i in range(len(suggestedrecepies)):
        names[suggestedrecepies[i][0]] = suggestedrecepies[i][0]
    
    print("SUGGESTED RECEPIES",names)
    return {'names':names}

def putshitincart(item_id, query):
    sanitized = item_id.replace('_',' ')
    print("Legger inn:", sanitized, query)
    if sanitized in handlevogn:
        handlevogn[sanitized] += query
    else:
        handlevogn[sanitized] = query
        
def queryRecepie(query):
    sanitized = query.replace('_',' ')
    print("Querying recepie", sanitized)
    q = run_recipe_search("","none",sanitized)
    arr = makeObject(q[0])
    ret = {}
    for i in range(len(arr)):
        ret[arr[i]['name']] = arr[i]['weight']
    print(ret)
    #print(arr)
    #{"Ost":392503,"kjeks":2359,"bæsj":123192}
    return {"ingredients":ret}

def get_shopping_cart():
    return {'cart':handlevogn}
#print(run_recipe_search("dinner","none","beef")[0])
fake_items = get_multiple_lists()
ablerecepiesIds = get_ablerecepies()
suggestedRecepies = get_suggested_recepies()
shoppingCart = get_shopping_cart()

#{"listOne":{"Ost":392503,"kjeks":2359,"bæsj":123192},"listTwo":["a","b","c","d","e"],"listThree":[10.5,20.2,30.7,40.9,50.1]}
#{'name':'monstercock', 'name':'bæsj','name':'grillet rumpe'}

@app.get("/items")
async def read_items():
    return fake_items

@app.get("/shoppingcart")
async def read_shoppingcart():
    return get_shopping_cart()

@app.get("/ablerecepiesIds")
async def read_recepies():
    return ablerecepiesIds

@app.get("/suggestedRecepies")
async def read_suggested_recepies():
    return suggestedRecepies

class Item(BaseModel):
    name: str
    description: str

# Endpoint to receive parameters
class Item(BaseModel):
    name: str
    description: str

# Function to be triggered by the endpoint
def getIngredientsForFood(item: Item):

    # Your specific action/functionality using the parameters
    print(f"Performing action with name: {item.name} and description: {item.description}")
    # Perform the desired action using the passed parameters

# Endpoint to trigger the specific action with parameters
@app.post("/putincart")
async def trigger_specific_action(item: Item):
    getIngredientsForFood(item)  # Call the function with the parameters
    return {"message": "Specific action triggered successfully"}

@app.get("/recepies/{item_id}")
async def read_item(item_id: str, query_param: str = None):
    return queryRecepie(item_id)

@app.get("/putshitincart/{item_id}")
async def put_in_cart(item_id: str, query_param: float = None):
    return putshitincart(item_id, query_param)

