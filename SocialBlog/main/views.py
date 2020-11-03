# main/views.py

from flask import render_template, request, Blueprint
from SocialBlog.models import BlogPost

main = Blueprint('main',__name__)

@main.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=10)
    return render_template('index.html',blog_posts=blog_posts)

@main.route('/about')
def about():
    return render_template('about.html')