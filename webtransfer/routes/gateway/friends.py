# Copyright 2022 iiPython

# Modules
from webtransfer import app
from flask import request, jsonify

# Routes
@app.route("/user/api/uvalidate", methods = ["POST"])
def route_user_uvalidate() -> None:
    users = request.form.getlist("users[]")
    if not isinstance(users, list):
        return jsonify(code = 400, message = "No users provided to validate."), 400

    return jsonify(code = 200, users = app.db("auth").check_users(users)), 200

@app.route("/user/api/friends/request", methods = ["POST"])
def route_user_friends_request() -> None:
    return "500 Not Implemented", 500

@app.route("/user/api/friends/accept", methods = ["POST"])
def route_user_friends_accept() -> None:
    return "500 Not Implemented", 500

@app.route("/user/api/friends/decline", methods = ["POST"])
def route_user_friends_decline() -> None:
    return "500 Not Implemented", 500
