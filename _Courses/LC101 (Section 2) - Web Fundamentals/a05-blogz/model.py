from app import db

from hash import make_salt, make_hash, check_hash

#configure the persistent class that will be used to make the database changes for blog entries
class Blogs(db.Model):
    id = db.Column(db.Integer, primary_key=True)   #database unique ID - needed by every persistent class
    title = db.Column(db.String(120))   #blog title column
    blog_body = db.Column(db.Text())   #actual blog entry
    public = db.Column(db.Integer)   #is the blog entry public or private
    blogDate = db.Column(db.Date)
    author = db.Column(db.Integer, db.ForeignKey('user.id'))   #the author id from the user table

    def __init__(self, title, blog_body, public, blogDate, author):
        self.title = title
        self.blog_body = blog_body
        self.public = public
        self.author = author
        self.blogDate = blogDate
    
    def get_id(self):
        return self.id
    
    def get_title(self):
        return self.title
    
    def get_blog_body(self):
        return self.blog_body
    
    def get_blog_public(self):
        return self.public
    
    def get_blog_author(self):
        return self.author
    
#configure the persistent class that will be used to make the database changes for user entries
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    useremail = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    entries = db.relationship('Blogs', backref='owner')

    def __init__(self, useremail, password):
        self.useremail = useremail
        self.password = make_hash(password)
    
    def get_id(self):
        return self.id
    
    def get_useremail(self):
        return self.useremail
    
    def get_password(self):
        return self.password