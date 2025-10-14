# El Alambique - Tequila and Mezcal Shop API


## Функціонал

* **Управління каталогом**: CRUD для продуктів, категорій та виробників.
* **Фільтрація**: Отримання списку продуктів за категорією або виробником.
* **Аутентифікація**: Реєстрація, вхід та вихід користувачів з використанням JWT (Access + Refresh tokens).
* **Управління профілем**: Авторизовані користувачі можуть переглядати, оновлювати та видаляти свій профіль.
* **Захист ендпоінтів**: Доступ до особистих даних є тільки у авторизованих користувачів.
* **Логування**: Основні події (реєстрація, помилки) записуються у файл `info.log`.


## Як запустити проект

### 1. Попередні вимоги

* Python 3.8+
* pip 

### 2. Клонування репозиторію

```bash
git clone <URL-вашего-репозитория>
cd el_alambique_project
```

### 3. Встановлення та активація віртуального оточення

**Для Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Для macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Встановлення залежностей

```bash
pip install django djangorestframework django-cors-headers djangorestframework-simplejwt
```

### 5. Застосування міграцій

```bash
python manage.py migrate
```

### 6. Запуск сервера для розробки

```bash
python manage.py runserver
```

Бекенд буде доступний за адресою `http://127.0.0.1:8000/`.


### 7. Запуск Frontend

Для тестування фронтенду просто відкрийте файли `index.html`, `login.html` та інші у браузері. Рекомендується використовувати розширення Live Server для VS Code, щоб уникнути проблем з CORS і `file://` протоколом.


### 8. Опис нових ендпоінтів застосунку Users

**1\. Реєстрація нового користувача**

*   **Метод**: POST
*   **Адрес**: /auth/register/
*   **Headers**: Content-Type: application/json
*   **Request Body**: JSON з даними користувача.

JSON

{\
    "username": "newuser",\
    "first\_name": "Петро", // Необов.\
    "last\_name": "Петренко", // Необов.\
    "email": "user@example.com",\
    "password": "StrongPassword123",\
    "password\_check": "StrongPassword123"\
}

*   **Response Body (Успішно** **201 Created****)**:

JSON

{\
    "message": "Користувач успішно створено!"\
}

*   **Response Body (Помилка** **400 Bad Request****)**:

JSON

{\
    "email": \[ "Користувач із таким Email вже існує." \],\
    "password": \[ "Паролі не збігаються!" \]\
}

* * *

**2\. Вхід у систему (Отримання токенів)**

*   **Метод**: POST
*   **Адрес**: /auth/token/
*   **Headers**: Content-Type: application/json
*   **Request Body**:

JSON

{\
    "email": "user@example.com",\
    "password": "StrongPassword123"\
}\

*   **Response Body (Успішно** **200 OK****)**:

JSON

{\
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...", // Refresh token\
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."  // Access token\
}

*   **Response Body (Помилка** **401 Unauthorized****)**:

JSON

{\
    "detail": "No active account found with the given credentials"\
}

* * *

**3\. Оновлення Access токена**

*   **Метод**: POST
*   **Адрес**: /auth/token/refresh/
*   **Headers**: Content-Type: application/json
*   **Request Body**:

JSON

{\
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." // refresh токен\
}

*   **Response Body (Успішно** **200 OK****)**:

JSON

{\
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." // Новий access токен\
}

* * *

**4\. Отримання даних свого профілю**

*   **Метод**: GET
*   **Адрес**: /auth/profile/
*   **Headers**: Authorization: Bearer <\_access\_token>
*   **Request Body**: пусто
*   **Response Body (Успішно** **200 OK****)**:

JSON

{\
    "id": 1,\
    "username": "newuser",\
    "first\_name": "Петро",\
    "last\_name": "Петренко",\
    "email": "user@example.com"\
}

* * *

**5\. Оновлення свого профілю**

*   **Метод**: PUT или PATCH
*   **Адрес**: /auth/profile/
*   **Headers**:
*   Content-Type: application/json
*   Authorization: Bearer <\_access\_token>
*   **Request Body**: JSON з полями, які потрібно змінити.

JSON

{\
    "username": "new\_username",\
    "first\_name": "Дмитро"\
}

*   **Response Body (Успішно** **200 OK****)**: Повні, оновлені дані профілю.

JSON

{\
    "id": 1,\
    "username": "new\_username",\
    "first\_name": "Дмитро",\
    "last\_name": "Петренко",\
    "email": "user@example.com"\
}

* * *

**6\. Видалення свого профілю**

*   **Метод**: DELETE
*   **Адрес**: /auth/profile/
*   **Headers**: Authorization: Bearer <\_access\_token>
*   **Request Body**: пусто
*   **Response Body (Успішно** **204 No Content****)**: пусто

