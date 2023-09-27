from fastapi import APIRouter

router = APIRouter(prefix='/products', 
                   tags=["products"],
                   responses={404: {"description": "Not found"}})

products_list =['products1', 'products2', 'products3']


@router.get('/')
async def products():
    return {"productos": "producto1"}

@router.get('/{id}')
async def products(id:int):
    return products_list[id]