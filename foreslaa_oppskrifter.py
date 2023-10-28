from oppbevaring import *
from oppskrift_object import *

ingredienser = {
    "cheese":1000,
    "dry white wine":100000,
    "ham":800,
    "unsalted butter":10000,
    "parsley":10000,
    "garlic":20000
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
                finalres.append(x)
                print("la til")
    return finalres


#Hent oppskrifter basert på hva man har mest av på lager:


#Skjekke hvilke av oppskriftene man har ingredienser til å lage
#print("Disse oppskriftene har du nok ingredienser til: \n", getAbleRecepies())
