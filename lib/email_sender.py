from flask import Flask, request, abort
import json
import re
import requests
import ConfigParser
app = Flask(__name__)

@app.route('/email', methods = ['POST'])
def email():
    if request.method == 'POST':

        # Throw a 400 error if anything goes wrong
        provider = retrieve_email_provider()
        if not provider:
            abort(400)

        d = json.loads(request.data)
        if not validate_inputs(d):
            abort(400)

        successful_response = send_request(d, provider)
        if not successful_response:
            abort(400)

        # Only if it's successful do we return2 01
        return successful_response, 201

    abort(400)

def retrieve_email_provider():
    # Standardize the provider in case the config is different
    try:
        config = ConfigParser.ConfigParser()
        config.read('config/email_config.ini')
        return config.get('Provider', 'provider').lower()
    except:
        return False

def validate_inputs(d):
    # Validate the fields to make sure they are all there
    if validate_email(d.get('to')) and \
      d.get('to_name') and \
      validate_email(d.get('from')) and \
      d.get('from_name') and \
      d.get('body') and \
      d.get('subject'):
        return True
    return False

def validate_email(email):
    # Validates the email. Currently only allows american letters 
    # and no consecutive periods

    if email == None or not isinstance(email, str):
        return False

    match = re.match(r"[a-zA-Z0-9._%+-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]", email)

    if match == None:
        return False

    return match

def send_request(d, provider):
    try:
        headers = {"content-type": "application/x-www-form-urlencoded"}

        if provider == 'mailgun':
            response = retrieve_mailgun_config()
            if not response:
                return False
            url, username, password = response

            data = format_mailgun(d)
            if not data:
                return False

            # Create the POST request
            r = requests.post(url, \
                auth = (username, password), \
                data = data, \
                verify = False, \
                headers = headers)

        elif provider == 'mandrill':
            response = retrieve_mandrill_config()
            if response == False:
                return False
            url, key = response

            data = format_mandrill(d, key)
            if not data:
                return False

            # Create the POST request
            r = requests.post(url, \
                data = json.dumps(data), \
                verify = False, \
                headers = headers)
        else:
            # If there's a third provider or there is a typo, return False
            return False

        if r.status_code == 200:
            return r.text
    except:
        return False

    return False

def format_mailgun(d):
    try:
        data = {}
        data['to'] = d['to_name'] + " <" + d['to'] + ">"
        data['from'] = d['from_name'] + " <" + d['from'] + ">"
        data['text'] = clean_body(d['body'])
        data['subject'] = d['subject']
        return data
    except:
        return False

def format_mandrill(d, key):
    try:
        data = {}
        data['key'] = key
        to = [{
            "email": d['to'],
            "name": d['to_name'],
            "type": "to"
        }]
        message = {
            "to": to,
            "from_email": d['from'],
            "from_name": d['from_name'],
            "subject": d['subject'],
            "text": clean_body(d['body'])
        }
        data['message'] = message
        return data
    except:
        return False

def retrieve_mailgun_config():
    try:
        config = ConfigParser.ConfigParser()
        config.read('config/mailgun_config.ini')
        return [config.get('Mailgun', 'url'),
                config.get('Mailgun', 'username'),
                config.get('Mailgun', 'password')]
    except:
        return False
        
def retrieve_mandrill_config():
    try:
        config = ConfigParser.ConfigParser()
        config.read('config/mandrill_config.ini')
        return [config.get('Mandrill', 'url'),
                config.get('Mandrill', 'key')]
    except:
        return False

# Removes all HTML tags that start with '<'' and everything in between until
# the first '>' and repeats.
def clean_body(body):
    return re.sub('<[^>]*>', '', body)

if __name__ == '__main__':
    app.debug = True
    app.run()
