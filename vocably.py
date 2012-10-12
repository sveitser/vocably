from bottle import route, run

@route('/login')
def login():
    return "Show me your e-mail!"

run(host='localhost', port=80, debug=True, reloader=True)
