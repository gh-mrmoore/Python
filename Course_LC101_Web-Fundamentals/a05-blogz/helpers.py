import re

#create function to validate the user email/name
def validate_user_email(useremail):
    regex_test = re.search(r'([a-zA-z0-9]*)@(\D*)(\....)', useremail)
    if len(useremail) <= 1 and len(useremail) >= 75:
        verify_email_message = 'Your email appears to be too long or too short.'
    elif '@' not in useremail or ' ' in useremail or '.' not in useremail:
        verify_email_message = 'This does not appear to be a valid email/username.'
    elif not regex_test:
        verify_email_message = 'This does not appear to be a valid email format.'
    else:
        verify_email_message = ''
    
    return verify_email_message


#check that the password entered meets our criteria
def validate_user_password(password):
    if len(password) < 5 or len(password) > 25:
        valid_password_message = 'Your password must be between 5 and 25 characters long.'
    elif ' ' in password:
        valid_password_message = 'Your password cannot contain any spaces.'
    else:
        valid_password_message = ''
    
    return valid_password_message


#check that the password cross-verify
def validate_password_match(password, verify):
    if len(password) == 0:
        verify_pword_message = 'No password validation entered.'
    elif password != verify:
        verify_pword_message = 'Password entries do not match'
    else:
        verify_pword_message = ''
    
    return verify_pword_message


#create the function to check for the length of the entries the user makes
def validate_post(x):
    if len(x) == 0:
            return 'missing'
    elif len(x) < 2:
        return 'too short. Input must be at least 2 characters long.'
    else:
        return 'valid!'
