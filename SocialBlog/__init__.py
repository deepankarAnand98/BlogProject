# SocialBlog/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY']='newsecretkey'

"""
Database Setup
"""

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)
Migrate(app,db)

""" Login Configuration """
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'
""""""


from SocialBlog.main.views import main
from SocialBlog.users.views import users
from SocialBlog.blog_posts.views import blog_posts
from SocialBlog.error_pages.handlers import error_pages

app.register_blueprint(main)
app.register_blueprint(blog_posts)
app.register_blueprint(users)
app.register_blueprint(error_pages)