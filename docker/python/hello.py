from bottle import route, run

@route('/')
@route('/<name>')
def index(name="Python"):
    return 'Hello %s!' % name
run(host='0.0.0.0', port=8080, theaded=True)
