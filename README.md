
# plank test

We want you to implement a web server in Python that exposes an API for a menu in a specific restaurant<br />
Find an API to get the menu of ארקפה in Tel Aviv from the following website<br />
Create a server which implements the following API:<br />
(for all GET operations - name and description - string. price - integer)<br />
GET /drinks - Returns the id, name, description and price of all drinks<br />
GET /drink/<id> - Returns id, name, description and price of a drink<br />
GET /pizzas - Returns the id, name, description and price of all pizzas<br />
GET /pizza/<id> - Returns id, name, description and price of a pizza<br />
GET /desserts - Returns the id, name, description and price of all desserts<br />
GET /dessert/<id> - Returns id, name, description and price of a dessert<br />
POST /order - receives an order and returns its total price.<br />
Body - (drinks, desserts, or pizzas are optional). You can define the body structure by yourself, or use the suggested structure below -<br />
{<br />
    "drinks": [id_5, id_6],<br />
    "desserts": [id_1, id_2],<br />
    "pizzas": [id_3, id_4]<br />
}<br />
Response - {"price": 123}.<br />
The data that the service provides should be updated daily<br />
Suggest a simple way to demonstrate the service functionality (CLI, unit tests, other) ----> Did not make it <br />
