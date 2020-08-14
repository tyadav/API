# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 13:35:16 2020

@author: TejYadav
"""
# Import required libraries
import flask
from flask import request
#from werkzeug.utils import secure_filename

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/me")
def me_api():
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        "image": url_for("user_image", filename=user.image),
    }

@app.route("/users")
def users_api():
    users = get_all_users()
    return jsonify([user.to_json() for user in users])

'''
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')
'''       
        
app.run(host='0.0.0.0')
