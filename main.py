from typing import Optional
from fastapi import FastAPI, Response,status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None




my_posts= [{"title":"title for post 1", "content": "content for post 1", "id": 1}, {"title": "favorite foods", "content": "couscous", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id: 
            return p
        

@app.get("/")
def root():
    return {"message": " Welcome to my API"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(post: Post):
    post_dict= post.dict() 
    post_dict["id"] = randrange(0, 10000000)

    my_posts.append(post_dict)

    return {"new_post": post_dict}


@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    the_post=find_post(id)
    if not the_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post with id {id} was not found') 
        """ response.status_code = status.HTTP_404_NOT_FOUND
        return {'message': f'Post with id {id} was not found'} """

        
    return {"post_detail": the_post }