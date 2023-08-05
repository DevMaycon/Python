import flask
from db import sql

app = flask.Flask(__name__)

@app.route("/<int:id>")
def response(id: str):
    return flask.jsonify(sql.get_by_id(id))



app.run(debug=True, port=4444)
