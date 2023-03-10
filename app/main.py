from fastapi import FastAPI

app =  FastAPI()


@app.get('/')
async def index():
    return {'estado':'funcionando'}

@app.get('/mati')
async def mati():
    return {'camara':'prendela'}