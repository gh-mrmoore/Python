from flask import Flask, request, redirect, render_template, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
import html
from datetime import datetime

from app import app, db
from model import Blogs, User
from helpers import validate_user_email, validate_user_password, validate_password_match, validate_post

from hash import make_salt, make_hash, check_hash

str_now = datetime.now()


#require that any user be logged in with the session set before accessing other pages
@app.before_request
def require_login():
    allowed_routes = ['login', 'register', 'static']

    if request.endpoint not in allowed_routes and 'username' not in session:
        return redirect('/login')


#give any visitor the chance to login
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(useremail=email).first()

        if user and check_hash(password, user.password):
            session['username'] = email
            session['user_id'] = user.id
            flash("Login Successful!", "success")   #success class
            return redirect('/')
        elif not user:
            flash("No matching user found.")
            return redirect('/register')
        else:
            flash("Login Failed!", "error")   #error class
            return redirect('/login')
    
    return render_template('login.html', str_now=str_now)


#allow new visitors to register to use the blog
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form['username']
        password = request.form['password']
        verify = request.form['verify_password']

        existing_user = User.query.filter_by(useremail=email).first()

        if not existing_user:
            validated_user = validate_user_email(email)
            validated_password = validate_user_password(password)
            passwords_matched = validate_password_match(password, verify)
            
            if not validated_user and not validated_password and not passwords_matched:
                new_user = User(email, password)
                db.session.add(new_user)
                db.session.commit()
                session['username'] = email
                session['user_id'] = new_user.get_id()

                return redirect('/newpost')
            else:
                if validated_user:
                    flash(validated_user, "error")
                if validated_password:
                    flash(validated_password, "error")
                if passwords_matched:
                    flash(passwords_matched, "error")
                return render_template('register.html', email=email, str_now=str_now)
        else:
            flash("This username appears to have already been registered.", "error")
            return redirect('/login')
    else:
        return render_template('register.html', str_now=str_now)


#create my home page
@app.route('/')
def index():
    all_users = User.query.all()

    return render_template('index.html', page_header='Blogz Home Page', all_users=all_users, str_now=str_now)


#create my form for new posts and validate them
@app.route('/newpost', methods=['POST', 'GET'])
def addpost():

    if request.method == 'POST':
        #get variables from the submitted form
        blog_title = html.escape(request.form['entry_title'])
        blog_entry = html.escape(request.form['blog_body'])
        public = html.escape(request.form['publish'])
        author = session['user_id']
        blogd_date = request.form['blog_date']
        
        #pass variables to the error-checking function
        title_error_check = validate_post(blog_title)
        body_error_check = validate_post(blog_entry)

        #check the entries for length
        if title_error_check != 'valid!' or body_error_check != 'valid!':
            title_error = 'Your title input was ' + title_error_check
            body_error = 'Your blog body input was ' + body_error_check
        else:
            title_error = ''
            body_error = ''
        
        if  title_error or body_error:   #go back to the posting form after an invalid posting
            return render_template('newpost.html', 
            entry_title=blog_title, 
            blog_bodytext=blog_entry, 
            title_error=title_error, 
            body_error=body_error, 
            str_now=str_now)
        else:
            new_post = Blogs(blog_title, blog_entry, public, blogd_date, author)
            db.session.add(new_post)
            db.session.commit()

            newest_post_id = new_post.get_id()

            return redirect('/blogs?blog_id={0}'.format(newest_post_id))   #go to the specific blog page after successful posting
    else:
        return render_template('newpost.html', str_now=str_now)


#create my path for displaying all public blog posts OR a single public blog post
@app.route('/blogs')
def blogs():
    #get a specific blog posting from anywhere elsee in the app
    if request.args.get('blog_id'):
        blog_id = int(request.args.get('blog_id'))

        current_page = request.args.get('page', 1, int)
        blogs = Blogs.query.filter_by(id=blog_id).paginate(current_page, 5, error_out=False)
        prev_url = 'blogs?page={0}'.format(blogs.prev_num)
        next_url = 'blogs?page={0}'.format(blogs.next_num)

    #get a singles user's blog postings from anywhere else in the app
    elif request.args.get('user_id'):
        user_id = int(request.args.get('user_id'))

        current_page = request.args.get('page', 1, int)
        blogs = Blogs.query.filter_by(author=user_id).order_by(Blogs.blogDate.desc()).paginate(current_page, 5, error_out=False)
        prev_url = 'blogs?page={0}'.format(blogs.prev_num)
        next_url = 'blogs?page={0}'.format(blogs.next_num)
        
    #get all blog posting for all users if no parameters are passed in to this section
    else:
        current_page = request.args.get('page', 1, int)
        blogs = Blogs.query.order_by(Blogs.blogDate.desc()).paginate(current_page, 5, error_out=False)
        prev_url = 'blogs?page={0}'.format(blogs.prev_num)
        next_url = 'blogs?page={0}'.format(blogs.next_num)
        
    return render_template('blogs.html', 
        blogs=blogs, 
        str_now=str_now, 
        prev_url=prev_url, 
        next_url=next_url)


#adding some functionality to edit the blog posts
@app.route('/edit', methods=['POST', 'GET'])
def editz():
    if request.method == 'POST':
        #get variables from the submitted form
        blog_id = request.form['blog_id']
        new_blog_title = html.escape(request.form['entry_title'])
        new_blog_body = html.escape(request.form['blog_body'])
        new_blog_published = request.form['blog_private']

        edit_post = Blogs.query.filter_by(id=blog_id).first()
        edit_post.title = new_blog_title
        edit_post.blog_body = new_blog_body
        edit_post.public = new_blog_published

        db.session.commit()

        return redirect('/blogs')
    
    elif not request.args.get('blog_id'):
        return redirect('blogs')
    
    else:
        blog_id = int(request.args.get('blog_id'))
        blogs = Blogs.query.filter_by(id=blog_id).all()
        return render_template('edit.html', blogs=blogs, str_now=str_now)


#user logout that deletes the session variable we set for the user
@app.route('/logout')
def logout():
    del session['username']
    del session['user_id']

    return redirect('/')


#shield the call to run the app if we're importing - this might work on Heroku, too
if __name__ == '__main__':
    app.run()