from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, votes
from .config import settings
from fastapi.middleware.cors import CORSMiddleware


# models.Base.metadata.create_all(bind = engine)

app = FastAPI()


# my_posts = [{'id': 62, 'title': ' post', 'content': 'successful', 'published': True, 'rating': 2},
#             {'id': 63, 'title': ' post', 'content': 'successful', 'published': True, 'rating': None},
#             {'id': 247214, 'title': ' post', 'content': 'successful', 'published': True, 'rating': 1}]

# def find_post(id):
#     for p in my_posts:
#         if p['id'] == id:
#             return p

# def find_index_post(id):
#     for i,p in enumerate(my_posts):
#         if(p['id'] == id):
#             return i

# @app.get("/") 
# async def root():
#     return {"message": "Hello World"}
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(votes.router)

@app.get("/")
def root():
    return {"message": "Hello world!! created"}