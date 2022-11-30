from api import app, db
from api import models
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify
import ariadne

type_defs = ariadne.load_schema_from_path('schema.graphql')
schema = ariadne.make_executable_schema(
    type_defs, ariadne.snake_case_fallback_resolvers
)

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = ariadne.graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)