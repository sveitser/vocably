from bottle import route, run, debug, template, request, static_file

from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage

import httplib2

# Landing Page    
@route('/')
def home():
    output = template('home')
    return output

# OAuth
@route('/oauth2callback')
def login_callback():
    print "Login callback from Google"
    if request.query.error:
        print "There was an error: '%s'" % request.query.error
        print "Redirecting back to root"
        redirect('/')
    else:
        print "Successfully acquired an authentication token"
        credentials = flow.step2_exchange(request.query.code)
        storage.put(credentials)
        print "Stored credentials"
        redirect('/')
        # http = credentials.authorize(httplib2.Http())

flow = flow_from_clientsecrets('config/client_secrets.json',
                               scope='https://mail.google.com/',
                               redirect_uri='http://localhost:8080/oauth2callback')
storage = Storage('config/credentials')

# Static Files
@route('/css/:path#.+#', name='css')
def css(path):
    return static_file(path, root='css')

@route('/img/:path#.+#', name='img')
def img(path):
    return static_file(path, root='img')

@route('/js/:path#.+#', name='js')
def js(path):
    return static_file(path, root='js')

    

run(host='0.0.0.0', port=8080, debug=True, reloader=True)
