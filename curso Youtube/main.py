from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Variable dinamica en la ruta
# Fasti API depende del tipo de parametro, lo ideal es epecificar el tipo de parametro en cada variable
@app.get("/items/{item_id}")
def read_item(item_id: int,):
    return {'item_id': item_id}
