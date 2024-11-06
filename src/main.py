from typing import Union

from fastapi import FastAPI

app = FastAPI()

from api.endpoints.user import router as user_router

app.include_router(user_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/test")
def read_root():
    return {"Hello": "World"}


# @app.get("/login")
# def read_item(email: Union[str, None] = None, password: Union[str, None] = None):
#     if not (email or password):
#         return {"Hello": "World"}
#     else:
#         user_router
#         return {"email": email,"password": password}
    

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}