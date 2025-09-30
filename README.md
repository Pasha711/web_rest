
# El Alambique
### Магазин оригінальної текіли й крафтового мескаля

_Продаж оригінальных сортів текіли й крафтового мескалю від виробника,
прямі поставки, власний імпорт без посередників, замовлення рідкісних сортів_


## Ендпоінти

**_Отримати список категорій товарів_**\
**GET /category**\  
_no request body\  
response status, response body(якщо успішно)_

**_Отримати список усіх товарів_**\
**GET /products**\
_no request body\
response status, response body(якщо успішно)_

**_Отримати опис товару за id_**\
**GET /products/id/1**\
_no request body\
response status, response body(якщо успішно)_

**_Отримати список товарів у категорії за id_**\
**GET /products/cat/1**\
_no request body\
response status, response body(якщо успішно)_

**_Отримати список виробників_**\
**GET /manufacturers**\
_no request body\
response status, response body(якщо успішно)_

**_Отримати список товарів виробника за id_**\
**GET /products/man/1**\
_no request body\
response status, response body(якщо успішно)_

**_Створити товар_**\
**POST /products**\
_Request Body(опис товару)\
response status, response body-id товару(якщо успішно)_

**_Створити категорію_**\
**POST /category**\
_Request Body(опис категорії)\
response status, response body-id товару(якщо успішно)_

**_Створити опис виробника_**\
**POST /manufacturers**\
_Request Body(опис виробника)\
response status, response body-id товару(якщо успішно)_

**_Оновити товар за id_**\
**PUT /products/id/1**\
_Request Body(опис товару)\
response status, response body(якщо успішно)_

**_Оновити опис категорії за id_**\
**PUT /category/id/1**\
_Request Body(опис категорії)\
response status, response body(якщо успішно)_

**_Оновити опис виробника за id_**\
**PUT /manufacturers/id/1**\
_Request Body(опис виробника)\
response status, response body(якщо успішно)_

**_Видалити товар за id_**\
**DELETE /products/id/1**\
_no request body\
response status_

**_Видалити категорію за id_**\
**DELETE /category/id/1**\
_no request body\
response status_

**_Видалити виробника за id_**\
**DELETE /manufacturers/id/1**\
_no request body\
response status_

Response status - Успішно або Помилка
Вміст Request Body залежить від ендпоінту
Вміст Response body залежить від ендпоінту

Попередньо - видалення категорій та виробників, що мають зв'язок з товарами не дозволяється
Видалення продуктів, що фігурують хоч у одному продажу(ордері)теж не дозволяється.

## Опис структури бази данних
_(таблиці можуть додаватися у процесі розробки):_

**Таблиця Products**\
**id**-число\
**code**-строка-Код продукту\
**name**-строка-Назва продукту\
**category**-FK Category-Посилання на категорію\
**manufacturer**-FK Manufacturers-Посилання на виробника\
**short_descr**-строка-Короткий опис\
**description**-строка-Повний опис

**Таблиця Category**\
**id**-число\
**code**-строка-Код категорії\
**name**-строка-Назва категорії\
**description**-строка-Опис категорії


**Таблиця Manufacturers**\
**id**-число\
**code**-строка-Код виробника\
**name**-строка-Назва виробника\
**description**-строка-Опис виробника


**Таблиця Clients**\
**id**-число\
**name**-строка-Нікнейм\
**phone**-строка-Телефон\
**email**-строка-Пошта

**Таблиця Orders**\
**id**-число\
**number**-строка-Номер ордеру\
**odate**-дата-Дата продажу

**Таблиця OrderProducts**\
**FK Orders**-Посилання на Orders\
**prod_id**-FK Products-Посилання на Products

**Таблиця ClientOrders**\
**client_id**-FK Clients-Посилання на Clients\
**order_id**-FK Orders-Посилання на Orders





