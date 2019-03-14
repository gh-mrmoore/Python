from flask import Flask, request, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import html

#configure flask and SQLAlchemy
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:build-a-blog@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

#configure the persistent class that will be used to make the database changes
class Blogs(db.Model):
    id = db.Column(db.Integer, primary_key=True)   #database unique ID - needed by every persistent class
    title = db.Column(db.String(120))   #blog title column
    blog_body = db.Column(db.Text())   #actual blog entry
    blogread = db.Column(db.Boolean())   #has the blog been read

    def __init__(self, title, blog_body, blogread):
        self.title = title
        self.blog_body = blog_body
        self.blogread = blogread
    
    def get_id(self):
        return self.id
    
    def get_title(self):
        return self.title
    
    def get_blog_body(self):
        return self.blog_body
    
    def get_blog_blogread(self):
        return self.blogread

#create the function to check for the length of the entries the user makes
def error_check(x):
    if len(x) == 0:
            return 'missing'
    elif len(x) < 2:
        return 'too short. Input must be at least 2 characters long.'
    else:
        return 'valid!'

#create my home page
@app.route('/')
def index():

    return render_template('home.html', page_title='Blog Home Page')

#create my form for new posts and validate them
@app.route('/newpost', methods=['POST', 'GET'])
def addpost():

    if request.method == 'POST':
        #get variables from the submitted form
        blog_title = html.escape(request.form['entry_title'])
        blog_entry = html.escape(request.form['blog_body'])
        blog_read = request.form['blogread']

        #pass variables to the error-checking function
        title_error_check = error_check(blog_title)
        body_error_check = error_check(blog_entry)

        #check the entries for length
        if title_error_check != 'valid!' or body_error_check != 'valid!':
            title_error = 'Your title input was ' + title_error_check
            body_error = 'Your blog body input was ' + body_error_check
        else:
            title_error = ''
            body_error = ''
        
        if  title_error or body_error:   #go back to the posting form after an invalid posting
            return render_template('newpost.html', 
            page_title='Create Your New Post', 
            entry_title=blog_title, 
            blog_bodytext=blog_entry, 
            title_error=title_error, 
            body_error=body_error)
        else:
            new_post = Blogs(blog_title, blog_entry, False)
            db.session.add(new_post)
            db.session.commit()

            newest_post_id = new_post.get_id()

            return redirect('/blogs?blog_id={0}'.format(newest_post_id))   #go to the specific blog page after successful posting
    else:
        return render_template('newpost.html', page_title='Create Your New Post')

#create my path for displaying all blog posts OR an individual blog post
@app.route('/blogs')
def blogs():
    if not request.args.get('blog_id'):
        blogs = Blogs.query.order_by('id desc').all()
        page_title = 'Blog Posts'
    else:
        blog_id = int(request.args.get('blog_id'))
        blogs = Blogs.query.filter_by(id=blog_id).all()
        page_title = 'Single Post'
    return render_template('posts.html', page_title=page_title, blogs=blogs)

#adding some functionality to edit the blog posts
@app.route('/edit', methods=['POST', 'GET'])
def editz():
    if request.method == 'POST':
        #get variables from the submitted form
        blog_id = request.form['blog_id']
        new_blog_title = html.escape(request.form['entry_title'])
        new_blog_body = html.escape(request.form['blog_body'])

        edit_post = Blogs.query.filter_by(id=blog_id).first()
        edit_post.title = new_blog_title
        edit_post.blog_body = new_blog_body

        db.session.commit()

        return redirect('/blogs')
    
    elif not request.args.get('blog_id'):
        return redirect('blogs')
    
    else:
        blog_id = int(request.args.get('blog_id'))
        blogs = Blogs.query.filter_by(id=blog_id).all()
        page_title = 'Edit Single Post'
        return render_template('edit.html', page_title=page_title, blogs=blogs)


#shield the call to run the app if we're importing - this might work on Heroku, too
if __name__ == '__main__':
    app.run()