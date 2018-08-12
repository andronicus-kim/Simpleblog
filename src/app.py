from models.post import Post
from src.database import Database

Database.initialize()
post = Post("title","onettad","asdss")

print(post.content)