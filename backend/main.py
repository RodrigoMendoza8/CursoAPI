from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from database import Base, engine, get_db, Session
from models import MensajeLog
from schemas import (
    MensajeLogCreate,
    MensajeLogRead,
    MensajeLogUpdate,
    MensajeLogListResponse,
    MensajeLogItemResponse,
    MensajeDeleteResponse,
) 
#from services.whats import enviar_mensaje
from colorstreak import Logger as log

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int
    
app = FastAPI(
    title="Product API",
    description="API para manejar productos",
    debug=True,
    docs_url="/doc",
)

Base.metadata.create_all(bind=engine)

def avisar_en_whats(data, mensaje: str):
    try:
        #res = enviar_mensaje(persona="club_empresarios", mensaje=mensaje)
        res = 'Hola'
        log.debug(f"[SIMULACION] mensaje enviado {mensaje} a bots")
        log.info(f"Mensaje enviado a bots: {res}")
        return {"status": "success", "data": data, "whats_response": res}
    except Exception as e:
        log.error(f"Error al enviar mensaje a bots: {e}")
        return {"status": "error", "data": data, "whats_response": "Fallo al enviar mensaje"}

# ============================== Listar mensajes ==============================
@app.get("/mensajes", response_model=MensajeLogListResponse)
def main(db: Session = Depends(get_db)):
    query = db.query(MensajeLog)
    query = query.order_by(MensajeLog.created_at.desc())
    mensajes = query.all()
    
    resp = avisar_en_whats(data=mensajes, mensaje="[🥵] Se ha accedido a la lista de mensajes")
    return resp

# ============================== Crear mensaje ==============================
@app.post("/mensajes", response_model=MensajeLogItemResponse, status_code=201)
def enviar_mens(payload: MensajeLogCreate, db: Session = Depends(get_db)):
    
    mensaje = payload.mensaje
    status = payload.status or "enviado"
    
    elemento = MensajeLog(mensaje=mensaje, status=status)
    db.add(elemento)
    db.commit()
    db.refresh(elemento)
    
    resp = avisar_en_whats(data=elemento, mensaje="[🥵] Nuevo mensaje creado")
    return resp

# ============================== Actualizar mensaje ==============================
@app.patch("/mensaje/{mensaje_id}", response_model=MensajeLogItemResponse)
def actualizar_mensaje(mensaje_id: str , payload: MensajeLogUpdate, db: Session = Depends(get_db)):
    # Objeto de la base de datos
    query = db.query(MensajeLog)
    query_filtrada = query.filter(MensajeLog.id == mensaje_id)
    elemento = query_filtrada.first()
    
    if elemento is None:
        raise HTTPException(status_code=404, detail="Mensaje no encontrado")
    
    # Objeto enviado por el usuario
    mensaje = payload.mensaje
    status = payload.status
    
    
    # Validaciones
    if mensaje is not None:
        elemento.mensaje = mensaje
    if status is not None:
        elemento.status = status
    
    db.commit()
    db.refresh(elemento)
    
    resp = avisar_en_whats(data=elemento, mensaje=f"[🥵] Mensaje {mensaje_id} actualizado")
    return resp

# ============================== Eliminar mensaje ==============================
@app.delete("/mensaje/{mensaje_id}", response_model=MensajeDeleteResponse)
def eliminar_mensaje(mensaje_id: str, db: Session = Depends(get_db)):
    query = db.query(MensajeLog)
    query_filtrada = query.filter(MensajeLog.id == mensaje_id)
    elemento = query_filtrada.first()
    
    if elemento is None:
        raise HTTPException(status_code=404, detail="Mensaje no encontrado")
    
    query_filtrada.delete()
    db.commit()
    
    resp = avisar_en_whats(data={"mensaje_id": mensaje_id}, mensaje=f"[🥵] Mensaje {mensaje_id} eliminado")
    return resp

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