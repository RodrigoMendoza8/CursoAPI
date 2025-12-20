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
    return 'Product added sucefully'

@app.put('/product')
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return 'Product updated sucefully'
        
    return {"error": "Product not found"}

@app.delete('/product')
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return 'Product deleted sucefully'
        
    return 'Product not found'