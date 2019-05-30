from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('form.html')

def error_check(x):
    if len(x) == 0:
            return 'missing'
    elif ' ' in x:
        return 'invalid. No spaces allowed in the input.'
    elif len(x) < 3:
        return 'too short. Input must be at least 3 characters long.'
    elif len(x) > 20:
        return 'too long. Input must be less than 20 characters long'
    else:
        return 'valid!'

@app.route("/", methods=['POST'])
def validate():
    error_count = 0

    uname = cgi.escape(request.form['username'])
    pword = cgi.escape(request.form['password'])
    pwordv = cgi.escape(request.form['verify_password'])
    email = cgi.escape(request.form['email'])

    uresult = error_check(uname)
    presult = error_check(pword)
    
    #check the username for length and spaces
    if uresult != 'valid!':
        username_message = 'Your username input was ' + uresult
        error_count += 1
    else:
        username_message = 'Your username input was ' + uresult
        error_count = error_count
    
    #check the password for length and spaces
    if presult != 'valid!':
        password_message = 'Your password input was ' + presult
        error_count += 1
    else:
        password_message = 'Your password input was ' + presult
        error_count = error_count

    #check that the password cross-verify
    if len(pword) == 0:
        verify_pword_message = 'No password entered.'
        error_count += 1
    elif pword != pwordv:
        verify_pword_message = 'Password entries do not match'
        error_count += 1
    else:
        verify_pword_message = 'Password entries match!'
        error_count = error_count

    #check that the email, if entered, is valid
    if len(email) >= 1:
        if '@' not in email or ' ' in email or '.' not in email:
            verify_email_message = 'This does not appear to be a valid email address.'
            error_count += 1
        else:
            verify_email_message = 'Validated!'
            error_count = error_count
    else:
        verify_email_message = "Are you sure you don't wish to provide your e-mail address?"

    #return the appropriate error message(s) or relay that everything is okay
    if error_count == 0:
        return redirect('/welcome?uname={0}'.format(uname))
    else:
        return render_template('form.html', uname=uname, email=email, 
        error_count=error_count, u_error=username_message, p_error=password_message, 
        pv_error=verify_pword_message, e_error=verify_email_message)

@app.route("/welcome")
def welcome():
    uname = request.args.get('uname')
    return render_template('welcome.html', uname=uname)

app.run()