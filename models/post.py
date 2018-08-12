
class Post(object):

    def __init__(self,id,blog_id,title,content,author,date):
        self.id = id
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date

    def save_to_mongo(self):
        Database.insert('posts',self.json())

    def json(self):
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'created_date': self.created_date

        }