
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI(
    title='My FastAPI API',
    description='A sample FastAPI application',
    version='0.1.0'
)

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.get('/')
async def root():
    return {'message': 'Welcome to the FastAPI API', 'docs': '/docs'}

@app.get('/health')
async def health_check():
    return {'status': 'healthy', 'service': 'fastapi'}

@app.post('/items/')
async def create_item(item: Item):
    return {
        'message': 'Item created successfully',
        'item': item
    }

@app.get('/items/{item_id}')
async def read_item(item_id: int, q: Optional[str] = None):
    return {
        'item_id': item_id,
        'q': q,
        'sample_data': {'name': 'Sample Item', 'price': 29.99}
    }

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
