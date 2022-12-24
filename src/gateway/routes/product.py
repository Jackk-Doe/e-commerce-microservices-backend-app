from fastapi import APIRouter


# Create Product APIrouter
router = APIRouter(prefix="/product")

@router.get('/test')
async def testRoute():
    return {"Test": "Product route"}