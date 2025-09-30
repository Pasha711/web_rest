
# El Alambique
### Original tequila and craft mezcal shop

_Sale of original varieties of tequila and craft mezcal from the manufacturer, direct deliveries, 
own import without intermediaries, ordering rare varieties_


## Endpoints


**_Get a list of product categories_**\
**GET /category**\
_no request body\
response status, response body(if successful)_

**_Get a list of all products_**\
**GET /products**\
_no request body\
response status, response body(if successful)_

**_Get product description by id_**\
**GET /products/id/1**\
_no request body\
response status, response body(if successful)_

**_Get a list of products in a category by id_**\
**GET /products/cat/1**\
_no request body\
response status, response body(if successful)_

**_Get a list of manufacturers_**\
**GET /manufacturers**\
_no request body\Create a product
response status, response body(if successful)_

**_Get a list of manufacturer's products by id_**\
**GET /products/man/1**\
_no request body\
response status, response body(if successful)_

**_Створити товар_**\
**POST /products**\
_Request Body(product description)\
response status, response body-id товару(if successful)_

**_Create a category_**\
**POST /category**\
_Request Body(category description)\
response status, response body-id товару(if successful)_

**_Create a manufacturer description_**\
**POST /manufacturers**\
_Request Body(manufacturer description)\
response status, response body-id товару(if successful)_

**_Update product by id_**\
**PUT /products/id/1**\
_Request Body(product description)\
response status, response body(if successful)_

**_Update category description by id_**\
**PUT /category/id/1**\
_Request Body(category description)\
response status, response body(if successful)_

**_Update manufacturer description by id_**\
**PUT /manufacturers/id/1**\
_Request Body(manufacturer description)\
response status, response body(if successful)_

**_Delete product by id_**\
**DELETE /products/id/1**\
_no request body\
response status_

**_Delete category by id_**\
**DELETE /category/id/1**\
_no request body\
response status_

**_Delete manufacturer by id_**\
**DELETE /manufacturers/id/1**\
_no request body\
response status_

Response status - Success or Error
The content of the Request Body depends on the endpoint.
Response body content depends on the endpoint

Deleting categories and manufacturers that are related to products is not allowed.
Deleting products that appear in at least one sale (order) is also not allowed.

## Description of the database structure
_(additional tables can be added as needed during the development process):_

**Table Products**\
**id**-number\
**code**-string-Product code\
**name**-string-Product name\
**category**-FK Category-Link to Category\
**manufacturer**-FK Manufacturers-Link to Manufacturers\
**short_descr**-string-Short description\
**description**-string-Full description

**Table Category**\
**id**-number\
**code**-string-Category code\
**name**-string-Назва категорії\
**description**-string-Category description


**Table Manufacturers**\
**id**-number\
**code**-string-Manufacturer code\
**name**-string-Manufacturer name\
**description**-string-Manufacturer description


**Table Clients**\
**id**-number\
**name**-string-Nickname\
**phone**-string-Phone\
**email**-string-E-mail

**Table Orders**\
**id**-number\
**number**-string-Order number\
**odate**-date-Sale date

**Table OrderProducts**\
**FK Orders**-Link to Orders\
**prod_id**-FK Products-Link to Products

**Table ClientOrders**\
**client_id**-FK Clients-Link to Clients\
**order_id**-FK Orders-Link to Orders





