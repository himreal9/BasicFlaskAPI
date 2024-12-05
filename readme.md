# Flask REST API for Products

This is a simple Flask-based REST API that interacts with an external API to fetch and manipulate product data. The application demonstrates the use of Flask and Flask-RESTful for creating a RESTful service.

## Features

- **GET /products**: Fetches a list of products from the Dummy JSON API. If the data is unavailable locally, it fetches and caches it in memory.
- **POST /products**: Adds a new product to the in-memory list. Validates input fields before adding the product.

## Technologies Used

- Python
- Flask
- Flask-RESTful
- Requests

## Prerequisites

- Python 3.8 or later
- pip (Python package installer)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/himreal9/BasicFlaskAPI.git
   cd BasicFlaskAPI
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python app.py
   ```

5. The API will be available at `http://127.0.0.1:5000`.

## API Endpoints

### **GET /products**

Fetches the list of products.

#### Response

- **200 OK**: Returns a list of products.
- **500 Internal Server Error**: If there's an issue fetching data from the Dummy JSON API.

#### Example Response

```json
[
  {
    "id": 1,
    "title": "iPhone 9",
    "price": 549,
    "category": "smartphones"
  },
  ...
]
```

### **POST /products**

Adds a new product to the in-memory list.

#### Request Body

```json
{
  "title": "New Product",
  "price": 100,
  "category": "Electronics"
}
```

#### Response

- **201 Created**: Returns the updated list of products, including the newly added product.
- **400 Bad Request**: If any required field is missing or empty.

#### Example Response

```json
[
  {
    "id": 1,
    "title": "iPhone 9",
    "price": 549,
    "category": "smartphones"
  },
  {
    "id": 2,
    "title": "New Product",
    "price": 100,
    "category": "Electronics"
  }
]
```

## Error Handling

- **404 Not Found**: Returned for undefined routes.
- **500 Internal Server Error**: Returned for internal server issues.

## Dependencies

All dependencies are listed in `requirements.txt`:

```plaintext
Flask==3.1.0
Flask-RESTful==0.3.10
requests==2.32.3
```

---

### Author

**Himanshu Patel**  
[GitHub](https://github.com/himreal9) | [Email](mailto:himreal9@gmail.com)
