
from app.api.routes import health, orders, payments, webhooks
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI(
    title='M-Pesa Reconciliation API',
    description='FastAPI service for M-Pesa payment intake and order reconciliation',
    version='0.1.0'
)

app.include_router(health.router)
app.include_router(orders.router)
app.include_router(payments.router)
app.include_router(webhooks.router)

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
