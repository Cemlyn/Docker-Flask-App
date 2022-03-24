import flask
#from gevent.pywsgi import WSGIServer
app = flask.Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"
    
@app.route('/ping', methods=['GET'])
def ping():
    """Determine if the container is working and healthy. In this sample container, we declare
    it healthy if we can load the model successfully."""
    #health = ScoringService.get_model() is not None  # You can insert a health check here

    #status = 200 if health else 404
    return flask.Response(response='\n', status=200, mimetype='application/json')

@app.route('/invocations', methods=['POST'])
def transformation():
    data = None

    # Convert from CSV to pandas
    if flask.request.content_type == 'application/json':
        data = flask.request.json
        data = {'success':'it worked'}
    else:
        data = {"error":"didnt work"}

    return flask.make_response(data,200)


if __name__ == '__main__':
    #http_server = WSGIServer(('0.0.0.0:8080'), app)
    #http_server.serve_forever()
    app.run(port=8080)