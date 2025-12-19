from fastapi import FastAPI
from models import Product

app = FastAPI()

products = [
    Product(id=1, name="Laptop", description="A high performance laptop", price=1200.00, quantity=10),
    Product(id=2, name="Smartphone", description="A latest model smartphone", price=800.00, quantity=25),
    Product(id=3, name="Headphones", description="Noise cancelling headphones", price=150.00, quantity=50)
]

@app.get("/products")
def get_products():
    return products

@app.get('/product/{id}')
def get_product(id: int):
    for product in products:
        if product.id == id:
            return product
    return {"error": "Product not found"}

@app.post('/product')
def add_product(product: Product):
    products.append(product)
    return product

