import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS, cross_origin

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
!! Running this funciton will add one
'''
db_drop_and_create_all()

# ROUTES
'''
@TODO implement endpoint
    GET /drinks
        it should be a public endpoint
        it should contain only the drink.short() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''

@app.route('/drinks', methods=['GET'])
# @cross_origin(headers=["Content-Type", "Authorization"])
# @requires_auth('get:drinks')
def get_drinks():
    all_drinks = Drink.query.all()

    return jsonify({
        'success': True,
        'drinks': [drink.short() for drink in all_drinks]
    }), 200


'''
@TODO implement endpoint
    GET /drinks-detail
        it should require the 'get:drinks-detail' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks-detail', methods=['GET'])
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth('get:drinks-detail')
def get_drink_detail(payload):
    all_drinks = Drink.query.all()

    return jsonify({
        'success': True,
        'drinks': [drink.long() for drink in all_drinks]
    }), 200

'''
@TODO implement endpoint
    POST /drinks
        it should create a new row in the drinks table
        it should require the 'post:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def add_drink(payload):
    data = request.get_json()

    try:
        req_recipe = data['recipe']
        if isinstance(req_recipe, dict):
            req_recipe = [req_recipe]

        drink = Drink()
        drink.title = data['title']
        drink.recipe = json.dumps(req_recipe)  # convert object to a string
        drink.insert()

    except BaseException:
        abort(400)

    return jsonify({'success': True, 'drinks': [drink.long()]})

'''
@TODO implement endpoint
    PATCH /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
        or appropriate status code indicating reason for failure
'''
        
@app.route('/drinks/<id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def edit_drink(payload,id):
    body = request.get_json()

    drink = Drink.query.filter(Drink.id == id).one_or_none()

    if not drink:
        abort(404)

    try:
        req_title = body.get('title')
        req_recipe = body.get('recipe')

        # check if updating title, add the update
        if req_title:
            drink.title = body['title']
        # check if updating recipe, add the update
        if req_recipe:
            drink.recipe = json.dumps(body['recipe'])

        drink.update()

        return jsonify({
            'success': True,
            'drinks': [drink.long()]
        })

    except Exception:
        abort(422)

'''
@TODO implement endpoint
    DELETE /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
'''

@app.route('/drinks/<id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drinks(payload, id):
    drink = Drink.query.filter_by(id=id).one_or_none()
    if not drink:
        abort(404)
    else:
        try:
            drink.delete()
            return jsonify({
                'success': True,
                'deleted': id
            })
        except:
            abort(422)



# Error Handling
'''
Example error handling for unprocessable entity
'''


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


'''
@TODO implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with approprate messages):
             jsonify({
                    "success": False,
                    "error": 404,
                    "message": "resource not found"
                    }), 404

'''

'''
@TODO implement error handler for 404
    error handler should conform to general task above
'''
@app.errorhandler(404)
def not_found(error):
    error_data = {
        "success": False,
        "error": 404,
        "message": "resource not found"
    }
    return jsonify(error_data), 404
    
'''
@TODO implement error handler for AuthError
    error handler should conform to general task above
'''
@app.errorhandler(AuthError)
def auth_error(Aerror):
    return jsonify({
        "success": False,
        "error": Aerror.status_code,
        "message": Aerror.error
    }), Aerror.status_code


@app.errorhandler(401)
def unauthorized(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": 'athorization error'
    }), 401


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": 'Internal Server Error'
    }), 500


@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": 'Bad Request'
    }), 400


@app.errorhandler(403)
def unauthorized(error):
    return jsonify({
        "success": False,
        "error": 403,
        "message": 'Forbidden'
    }), 403