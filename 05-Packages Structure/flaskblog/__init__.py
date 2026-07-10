from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flaskblog.forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '9618884c3669589dcae9c211'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from flaskblog import routes