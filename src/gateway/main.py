import uvicorn
from fastapi import FastAPI

import envs as _envs
import routes.product as _product_route

app = FastAPI()

@app.get('/test')
async def testApp():
    return {"Hello": "FastAPI!"}


# Add API routers : Product & User
app.include_router(_product_route.router)


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=int(_envs.PORT), reload=True)