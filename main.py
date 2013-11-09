"""
app setup thinkful.com.
"""


from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.debug = env("DEBUG", False, False) in ('True', 'true')
# app.config['SQLALCHEMY_DATABASE_URI'] = env('DATABASE_URL')
# db = SQLAlchemy(app)
# for flaskext.auth -- secret key needed to use sessions
# app.secret_key = env('USER_AUTH_SECRET_KEY')
