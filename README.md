
# plank test

We want you to implement a web server in Python that exposes an API for a menu in a specific restaurant_
Find an API to get the menu of ארקפה in Tel Aviv from the following website_
Create a server which implements the following API:_
(for all GET operations - name and description - string. price - integer)_
GET /drinks - Returns the id, name, description and price of all drinks_
GET /drink/<id> - Returns id, name, description and price of a drink
GET /pizzas - Returns the id, name, description and price of all pizzas
GET /pizza/<id> - Returns id, name, description and price of a pizza
GET /desserts - Returns the id, name, description and price of all desserts
GET /dessert/<id> - Returns id, name, description and price of a dessert
POST /order - receives an order and returns its total price.
Body - (drinks, desserts, or pizzas are optional). You can define the body structure by yourself, or use the suggested structure below -
{
    "drinks": [id_5, id_6],
    "desserts": [id_1, id_2],
    "pizzas": [id_3, id_4]
}
Response - {"price": 123}.
The data that the service provides should be updated daily
Suggest a simple way to demonstrate the service functionality (CLI, unit tests, other) ----> Did not make it 
