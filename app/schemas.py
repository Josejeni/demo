from pydantic import BaseModel
from pydantic.types import conint

class log(BaseModel):
    user_name:str
    password:str
    title:str
    content:str

    class ConFig:
        orm_model=True

class user(BaseModel):
    username:str
    password:str
class post(BaseModel):
    
    user_id:int
    content:str
    title:str

    
class vote(BaseModel):
    post_id:int
    dir:conint(le=1)
    class ConFig:
     orm_model=True