from fastapi import FastAPI,HTTPException,status
from .schemas import log, post, user, vote
from . import models
from .database import engine,get_db
from sqlalchemy.orm import Session
from fastapi import Depends




models.Base.metadata.create_all(bind=engine)

app=FastAPI()

@app.get("/")
def root():
    return {"Helo"}



@app.post("/posts")
def login(post:log,db:Session=Depends(get_db)):
    my_post=models.log(**post.dict())
    db.add(my_post)
    db.commit()
    db.refresh(my_post)
    return{"data":my_post}




@app.get("/get_info/{username}")
def get_post(username:str,db:Session=Depends(get_db)):
 
    try:
        get_post=db.query(models.log).filter(models.log.user_name == username)
      
        got=get_post.first()
        return {"msg":got}
    except:
        return HTTPException(state_code=status.HTTP_404_NOT_FOUND,detail="cannot found")




@app.delete("/delete/{username}")
def delete_post(username:str,db:Session=Depends(get_db)):
    deleted_post=db.query(models.log).filter(models.log.user_name==username)
    dell=deleted_post.first()
    deleted_post.delete(synchronize_session=False)
    db.commit()
    return{"data":dell}

@app.put("/put/{username}")
def put_post(user_name:str,post:log,db:Session=Depends(get_db)):
    updated_post=db.query(models.log).filter(models.log.user_name==user_name)
    up=updated_post.first()
    if up==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Page not found")
    new=updated_post.update(post.dict(),synchronize_session=False)
    db.commit()

    return "success"




@app.post("/post_user")
def user_post(post:user,db:Session=Depends(get_db)):
    my_post=models.users(**post.dict())
    db.add(my_post)
    db.commit()
    db.refresh(my_post)
    return{"data":my_post}

# @app.post("/post_user")
# def user_post(post:post,db:Session=Depends(get_db)):
#     my_post=models.posts(**post.dict())
#     db.add(my_post)
#     db.commit()
#     db.refresh(my_post)
#     return{"data":my_post}



@app.post("/vote")
def post_vote(vote:vote,db:Session=Depends(get_db)):
   vote_query=db.query(models.Vote).filter(vote.post_id==models.posts.id)
   found_vote=vote_query.first()
   if(dir==1):
    if found_vote:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="Already existed")
    new_vote=models.Vote(id=vote.post_id)
    db.add(new_vote)
    db.commit()
    db.refresh(new_vote)
    return{"success"}
   else:
    if not found_vote:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Not found..")
    db.delete(found_vote)
    db.commit()
    return {"deleted"}
