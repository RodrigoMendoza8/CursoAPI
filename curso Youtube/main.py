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
# Variable dinamica en la ruta
# Fasti API depende del tipo de parametro, lo ideal es epecificar el tipo de parametro en cada variable
@app.get("/items/{item_id}")
def read_item(item_id: int,):
    return {'item_id': item_id}
