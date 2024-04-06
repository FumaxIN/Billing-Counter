# Billing-Counter Backend

Backend system for Billing Counter built on [DRF](https://www.django-rest-framework.org/)

- **local**: http://localhost:/
- **production**: http://54.198.181.201/

## Requirements

##### For running the script

- [Python](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)
- Libraries mentioned below

## Cloning

* Create a virtual environment
```bash
python -m venv ./venv
source ./venv/bin/activate
```
* Use `git clone` to clone the repo
```bash
git clone git@github.com:FumaxIN/Billing-Counter.git
```

## Running

* Install the requirements
```bash
  pip install -r requirements.txt
```
* Create a databse 'billing' on psql `createdb psql` and make migrations
```bash
python manage.py migrate
```
* Run server
```bash
python manage.py runserver
```

## Swagger-Doc

**Note**: In each post request, `url` and `external_id` field are auto generated for navigation. <br />

### Auth Endpoints:
* **Login for existing employee**
    ```
    POST: /v1/auth/login
    ```
   Request body:
    ```
    {
        "email": "user@example.com",
        "password": "string"
    }
    ```
   An `access` token will be returned. 
   Click the `Authorize` button at the top-right section of the swagger page and paste the token to login


* **Registration for a new employee**
    ```
    POST: /v1/auth/register
    ```
    Request body:
    ```
    {
        "email": "user@example.com",
        "name": "Jane Smith",
        "password": "string",
        "password2": "string"
    }
    ```
  An `access` token will be returned.
  Click the `Authorize` button at the top-right section of the swagger page and paste the token to login

### Product endpoints
* **Add a product**
    ```
    POST: /v1/products
    ```
    Request body:
    ```
    {
        "name": "LeeCooper Jeans",
        "description": "Lee Cooper Skinny jeans unisex",
        "price": "2499.00"
    }
    ```

* **Get products**
    ```
    GET: /v1/products
    ```

* **Fetch a product** `/v1/products/{url}`
    ```
    GET: /v1/products/AbdFE3e6
    ```

* **Update a product** `/v1/products/{url}`
    ```
    PATCH: /v1/products/AbdFE3e6
    ```
  Request body:
    ```
    {
        "price": "1399.00"
    }
    ```

* **Delete a product**
    ```
    DELETE: /v1/products/{url}
    ```


### Customer endpoints
* **Add a customer**
    ```
    POST: /v1/customers
    ```
  Request body:
    ```
    {
      "name": "John Doe",
      "email": "johndoe@example.com",
      "phone": "9421459476",
      "address": "string"
    }
    ```

* **Get customers**
    ```
    GET: /v1/customers
    ```

* **Fetch a customer** `/v1/customers/{external_id}`
    ```
    GET: /v1/customers/04171903-6d50-43d2-a079-8c21d93bbfc3
    ```

* **Update customer details** `/v1/customers/{external_id}`
    ```
    PATCH: /v1/customers/04171903-6d50-43d2-a079-8c21d93bbfc3
    ```
  Request body:
    ```
    {
        "phone": "9342781065",
        "address": "New address"
    }
    ```

* **Delete a customer**
    ```
    DELETE: /v1/customers/{external_id}
    ```

### Billing endpoints
* **Generate a new bill**
    ```
    POST: /v1/bills
    ```
  Request body:
    ```
    {
      "customer_id": "04171903-6d50-43d2-a079-8c21d93bbfc3",
      "products_id":  [ 
            { 
                "a05f4c35-323e-4439-b76b-93e34ad7c9dd": 2
            },
            { 
                "690775a6-96c2-4cc9-93d6-878c322cac6d": 1
            }
        ]
    }
    ```
  In the backend, each product will be fetched, price to be multiplied with quantity to ge the final amount.

    Response:
    ```
    {
      "external_id": "4c9d1de8-a9a7-4af8-a011-7a08292f5d4c",
      "url": "Cff03bf9",
      "amount": "13497.00",
      "orders": [
        {
          "product": {
            "external_id": "a05f4c35-323e-4439-b76b-93e34ad7c9dd",
            "url": "AbdFE3e6",
            "name": "Lee Cooper Jeans",
            "description": "unisex skinny jeans",
            "price": "2499.00",
            "created_at": "2024-04-06T17:28:56.921158Z",
            "updated_at": "2024-04-06T17:37:58.986056Z"
          },
          "quantity": 2,
          "total": "4998.00"
        },
        {
          "product": {
            "external_id": "690775a6-96c2-4cc9-93d6-878c322cac6d",
            "url": "200478ff",
            "name": "Casio Watch",
            "description": "Unisex Chronograph Watch by Casio",
            "price": "8499.00",
            "created_at": "2024-04-05T16:27:26.307872Z",
            "updated_at": "2024-04-05T16:27:26.307892Z"
          },
          "quantity": 1,
          "total": "8499.00"
        }
      ],
      "customer": {
        "external_id": "04171903-6d50-43d2-a079-8c21d93bbfc3",
        "url": "F3EE7a75",
        "name": "John Doe",
        "email": "johndoe@example.com",
        "phone": "9780119670",
        "address": "South Ex, New Delhi",
        "created_at": "2024-04-06T17:15:16.415319Z",
        "updated_at": "2024-04-06T17:15:16.415337Z"
      },
      "employee": {
        "external_id": "87526cf6-2cd5-4ef1-bd36-0bf7461e91db",
        "email": "harshit@gmail.com",
        "name": "Harshit",
        "meta": {
          "is_admin": false,
          "is_staff": false,
          "is_superuser": false
        },
        "created_at": "2024-04-06T16:15:36.659393Z",
        "updated_at": "2024-04-06T16:15:36.659422Z"
      },
      "created_at": "2024-04-06T17:39:47.179698Z",
      "modified_at": "2024-04-06T17:39:47.179716Z",
      "deleted": false
    }
    ```

* **Get bills**
    ```
    GET: /v1/bills
    ```

* **Fetch a bill** `/v1/bills/{url}`
    ```
    GET: /v1/bills/Cff03bf9
    ```
  

### Analytics Endpoint

* **Get analytics**
    ```
    GET: /v1/analytics
    ```
    Fetches top employee wrt revenue and top selling product along with the details

    Response:
    ```
    {
      "top_employee": {
        "user": {
          "external_id": "87526cf6-2cd5-4ef1-bd36-0bf7461e91db",
          "email": "harshit@gmail.com",
          "name": "Harshit",
          "meta": {
            "is_admin": false,
            "is_staff": false,
            "is_superuser": false
          },
          "created_at": "2024-04-06T16:15:36.659393Z",
          "updated_at": "2024-04-06T16:15:36.659422Z"
        },
        "total_revenue": 18495
      },
      "top_product": {
        "name": {
          "external_id": "a05f4c35-323e-4439-b76b-93e34ad7c9dd",
          "url": "AbdFE3e6",
          "name": "Lee Cooper Jeans",
          "description": "unisex skinny jeans",
          "price": "2499.00",
          "created_at": "2024-04-06T17:28:56.921158Z",
          "updated_at": "2024-04-06T17:39:47.183438Z"
        },
        "total_units_sold": 4
      }
    }
    ```