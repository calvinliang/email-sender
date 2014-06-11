# How to install and run

* Running on Python 2.7.7 (https://www.python.org/download/releases/2.7.7/)

* Install pip (https://pip.pypa.io/en/latest/installing.html)

```> python get-pip.py```

* Install requests via pip (http://docs.python-requests.org/en/latest/user/install/#install)

```> pip install requests```

* Install nose via nose (http://nose.readthedocs.org/en/latest/)

```> pip install nose```

* Get an API key from Mailfun (https://mailgun.com/cp)
* Get an API key from Mandrill (http://mandrill.com/)
* ```mv``` your config/*ini.local files to config/*ini
* Update the config/ files with the appropriate usernames/passwords/keys
* You can now run the tests with ```nosetests -v```
* You can start the server with ```python email_sender.py``` and hit it with a properly formatted curl request. One example is here:

```
curl -i -H "Accept: application/json" -H "Content-Type: x-www-form-urlencoded" -X POST -d '{"to": "<email>", "to_name": "<name>", "from": "<email>", "from_name": "<from>", "subject": "<subject>", "body": "<body>"'} http://localhost:5000/email
```

# Tactical Decisions

### Language and Framework Choices
I chose to write this in Python because I love the simplicity of it and it's my go-to language for small projects like this. I chose Flask for my microframework because it was the first one I found (and the community and support behind it seemed more mature compared to Bottle for instance). I used pip because it was the biggest Python package manager I found. Requests allowed me to create the POST requests very easily to send off to Mailgun and Mandrill. I used Nose to gather all my tests and run them seamlessly.

### What-ifs and Trade-offs
I would like more experience in learning the conventions of project structure for Python projects. My code was placed by how I felt it should logically be, which is not necessarily the best place. One issue I ran into was my server and my tests were running in different places, so the ConfigParser which read the configuration files would run into pathing issues. This is also my first run-in with working closely with HTTP request, so some of my expected HTTP responses and errors might be off.


