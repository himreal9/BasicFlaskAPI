from flask import Flask, request
from flask_restful import Api, Resource
import requests

app = Flask(__name__)
api = Api(app)

# In-memory storage for products
products = []

# URL for Dummy JSON API
DUMMY_API_URL = "https://dummyjson.com/produc"

def fetch_products():
    """Fetch products from Dummy JSON API and populate the in-memory storage."""
    global products
    try:
        response = requests.get(DUMMY_API_URL)
        response.raise_for_status()  # Raise exception for non-2xx status codes
        products.clear()  # Ensure the list is clean before updating
        products.extend(response.json().get("products", []))
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch products: {e}"}, 500


class ProductListResource(Resource):
    def get(self):
        """GET endpoint to fetch the list of products."""
        if not products:
            error = fetch_products()
            if error:  # If an error occurred, return the error response
                return error
        return products, 200  # Return raw list with status code 200

    def post(self):
        """POST endpoint to add a new product."""
        data = request.get_json()

        # Validate required fields
        if not data or not all(key in data and data[key] for key in ['title', 'price', 'category']):
            return {"error": "Invalid data. 'title', 'price', and 'category' are required and cannot be null or blank."}, 400

        # Add the product to the in-memory list
        new_product = {
            "id": len(products) + 1,  # Auto-increment ID
            "title": data['title'],
            "price": data['price'],
            "category": data['category'],
            **{k: v for k, v in data.items() if k not in ['title', 'price', 'category', 'id']}
        }
        products.append(new_product)

        return products, 201  # Return the products with newly added product with status code 201


# Register the resource with the API
api.add_resource(ProductListResource, '/products')

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors."""
    return {"error": "Resource not found"}, 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return {"error": "Internal server error"}, 500

if __name__ == "__main__":
    app.run(debug=True)