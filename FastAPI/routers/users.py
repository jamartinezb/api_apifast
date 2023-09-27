from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# uvicorn users:app --reload
router = APIRouter(prefix='/users',
                   tags=["users"],
                   responses={404: {"description": "Not found"}})

class User(BaseModel):
    id: int
    name: str
    edad: int
    url: str

user_list=[User(id=1, name="jhon", edad=31, url="https://www.youtube.com/watch?v=_y9qQZXE24A"),
          User(id=2, name="jhon", edad=30, url="https"),]

@router.get("/")
async def users():
    return user_list

@router.get("/{id}") #path
async def user(id: int):
    return search_user(id)

@router.get("/") #query
async def user(id: int):
    return search_user(id)


@router.post("/", response_model=User, status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=206, detail="User already exists")

    user_list.append(user)
    return user


@router.put("/")
async def user(user: User):
    found = False
    
    for index, saved_user in enumerate(user_list):
        if saved_user.id == user.id:
            user_list[index] = user
            found = True
    
    if not found:
        return {"message": "User not found"}
    return user

@router.delete("/{id}")
async def user(id: int):
    found = False
    
    for index, saved_user in enumerate(user_list):
        if saved_user.id == id:
            del user_list[index]
            found = True
    
    if not found:
        return {"message": "User not found"}
    return {"message": "User deleted successfully"}

def search_user(id):
    users = filter(lambda user: user.id == id, user_list)
    try:
        return list(users)[0]
    except:
        return {"message": "User not found"}