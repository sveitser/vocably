from bottle import route, run

@route('/')
def home():
    return "Vocably, yeah!"

@route('/login')
def login():
    return "Show me your e-mail!"

run(host='ec2-54-242-121-195.compute-1.amazonaws.com', port=8080, debug=True, reloader=True)
