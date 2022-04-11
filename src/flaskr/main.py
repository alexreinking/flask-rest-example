from flask import jsonify, request, Blueprint

bp = Blueprint('main', __name__)


@bp.route('/echo', methods=['POST'])
def echo():
    """
    Sending a POST request to the /echo endpoint will respond in one of the following
    ways:

    1. If the content type is application/json and the body can be parsed as JSON,
       it will return that same body back as the response.
    2. Otherwise, it will raise HTTP 400
    """
    return jsonify(request.json)


@bp.route('/echo/<string:token>', methods=['POST'])
def echo_token(token):
    """
    Sending a POST request to the /echo/<token> endpoint will result in a response that
    contains a JSON dictionary with a single key, token, whose value is the <token>
    provided in the URL.
    """
    return jsonify({'token': token})
