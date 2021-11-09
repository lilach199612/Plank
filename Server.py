import datetime

from pip._vendor import requests
from flask import Flask, request
from flask import url_for

API = requests.get("https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod=pickup").json()
lastUpdate=datetime.date.today()

def GET(categoryName, dishName="*"):
    global API
    if(lastUpdate!=datetime.date.today()):#update daily
        API = requests.get("https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod=pickup").json()
    categoryName=categoryName[0].upper()+categoryName[1:]
    listOfThisCatagoryItems = []
    for catagory in API["Data"]["categoriesList"]:
        if catagory["categoryName"] == categoryName:
            listOfThisCatagoryItems = catagory
            break;

    getItems = {}
    if dishName == "*":
        for item in listOfThisCatagoryItems["dishList"]:
            curr = {}
            curr["dishId"] = item["dishId"]
            curr["dishName"] = item["dishName"]
            curr["dishDescription"] = item["dishDescription"]
            curr["dishPrice"] = item["dishPrice"]
            getItems[item["dishName"]]=curr
        return getItems
    else:
        for item in listOfThisCatagoryItems["dishList"]:
            if dishName == item["dishName"]:
                curr = {}
                curr["dishId"] = item["dishId"]
                curr["dishName"] = item["dishName"]
                curr["dishDescription"] = item["dishDescription"]
                curr["dishPrice"] = item["dishPrice"]
                return curr
        return dishName




app = Flask(__name__)
@app.route('/order', methods=['POST'])
def POST():
    orderDetail=request.json
    totalPrice = 0
    for catagory in orderDetail:
        for item in orderDetail[catagory]:
            totalPrice += GET(catagory, item)["dishPrice"]
    return {"price": totalPrice}

@app.route("/<catagory>",methods=['GET'])
def get(catagory):
    return GET(catagory)

@app.route("/<catagory>/<id>",methods=['GET'])
def getItem(catagory,id):
    return GET(catagory,id)

