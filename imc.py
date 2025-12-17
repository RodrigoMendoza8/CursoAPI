from fastapi import FastAPI


def imc(peso: float, estatura: float):
    return peso / estatura**2

def imc_listas(peso_id: float, estatura_id: float):
    
    #7
    pesos = [60.0, 59.4, 65.9, 82.1, 67.1, 73.9, 62.9]
    #7
    alturas = [1.68, 1.90, 1.64, 1.74, 1.78, 1.83, 1.86]
    
    imc = pesos[peso_id-1] / alturas[estatura_id - 1]**2
    peso = pesos[peso_id-1]
    altura = alturas[estatura_id - 1]
    
    return imc, peso, altura

app = FastAPI(
    title='Prueba de API',
    description='Esto es una app backend rapida',
    debug=True,
    docs_url='/doc',
)


@app.get('/calcular_imc')
def main():
    peso_id = 4
    estatura_id = 1
    respuesta, peso, altura = imc_listas(peso_id, estatura_id)
    print(respuesta)
    return {'status_code' : 200,
        'mensaje': f'IMC: {respuesta:.2f}, Peso(kg): {peso}, Estatura(metros): {altura}'}
    
@app.get('/calcula_imc_id/{peso_id}/{estatura_id}')
def calcula_imc_id(peso_id:int, estatura_id:int):
    try:
        respuesta, peso, altura = imc_listas(peso_id, estatura_id)
        print(respuesta)
        return {'status_code' : 200,
            'mensaje': f'IMC: {respuesta:.2f}, Peso(kg): {peso}, Estatura(metros): {altura}'}
    except IndexError:
        return {'status_code' : 200,
            'mensaje': 'Indice fuera del rango'}
    