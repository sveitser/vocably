from bottle import route, run

@route('/')
def home():
    return "Vocably, yeah!"

@route('/login')
def login():
    return "Show me your e-mail!"

run(host='0.0.0.0', port=8080, debug=True, reloader=True)
