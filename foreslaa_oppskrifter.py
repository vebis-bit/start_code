from run_recipe_search import *
from oppskrift_object import *

handlevogn = {
    "cheese":0,
    "dry white wine":0,
    "ham":0,
    "unsalted butter":0,
    "parsley":0,
    "garlic":0,
    "beef":0,
    "vegetable oil":0,
}

ingredienser = {
    "cheese":1000,
    "dry white wine":100000,
    "ham":800,
    "unsalted butter":10000,
    "parsley":10000,
    "garlic":20000,
    "beef":200000,
    "vegetable oil":200000,
    "red wine":40000,
    "beef consommé":200000,
    "blackberries":200000,
    "apple cider":2000000,
    "simple sirup":20000,
    "lemon juice":200000,
    "bourbon":12401240,
    "cinnamon sugar":1250912,
    "berries":123124124,
    "syrup":2103123,
    "whole-wheat flour":1203129,
    "sugar":1239123124,
    "baking powder":109231,
    "baking soda":1230249,
    "egg":1203,
    "buttermilk":482489,
    "canola oil":12312312,
    "pancake mix":123124124,
    "rye flour":123123,
    "whole wheat flour":12491024,
    "extra-virgin olive oil":1029381,
    "kosher salt": 1293142,
    "all-purpose flour":12041924,
    "light brown sugar":1295124,
    "buttermilk":1249125,
    "Butter":1295812
}
# 5 er det hellige tall for ingredienser
#run_recipe_search("dinner", "no", "cheese")[0][5][0]["food"]

#res[nr matrett][5][nr ingrediens]

def makeObject(recepie):
    listIngredients = []
    for i in range(len(recepie[4])):
        listIngredients.append({'name':recepie[4][i]["food"],'weight':recepie[4][i]["weight"], 'enough':False})
    return listIngredients

def checkIfEnough(listIngredients):
    totalEnough = True
    for i in range(len(listIngredients)):
        if listIngredients[i]['name'] in ingredienser:
            if listIngredients[i]['weight'] < ingredienser[listIngredients[i]['name']]:
                listIngredients[i]['enough'] = True
                #print("Har nok", listIngredients[i]['name'])
            else:
                totalEnough = False
        else:
            totalEnough = False        
    return listIngredients, totalEnough

def iterate(res):
    listOfOkRecepies = []
    for i in range(len(res)):
        obj = makeObject(res[i])
        obj,enough = checkIfEnough(obj)
        if enough:
            listOfOkRecepies.append(res[i])
    return listOfOkRecepies

def getAbleRecepies():
    global ingredienser
    #ingredienser = sorted(ingredienser)
    finalres = []
    #itererer igjennom alle ingrediensene vi har i kjøleskapet og søker etter om det er noen av de vi har alle ingredisensene til å lage
    for key in ingredienser:
        res = run_recipe_search("dinner", "no", key)
        print("Found", len(res), "recepies with", key)
        res = iterate(res)
        if len(res) > 0:
            for x in res:
                if not x in finalres:
                    finalres.append(x)
                print("la til")
    return finalres


#Hent oppskrifter basert på hva man har mest av på lager:


#Skjekke hvilke av oppskriftene man har ingredienser til å lage
#print("Disse oppskriftene har du nok ingredienser til: \n", getAbleRecepies())
