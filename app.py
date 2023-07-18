from flask import Flask, render_template

from main_page.main import main_page_bp
from admin.admin import admin_bp
from login.login import login_bp

app = Flask(__name__)

app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'hbjknmmdesdfgcvhb'

app.register_blueprint(main_page_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(login_bp)

from flask import Blueprint, render_template, request, redirect
from database.models import add_problem_db, get_all_problems_db
from main_page import forms

main_page_bp = Blueprint('main_page', __name__)


@main_page_bp.route('/')
def main_page():
    problems = get_all_problems_db()
    form = forms.PostProblem()
    return render_template('index.html', problems=problems, form=form)


@main_page_bp.route('/add_problem', methods=['post'])
def add_question():
    title = request.form.get('title')
    message = request.form.get('message')
    add_problem_db(title=title, message=message)
    return redirect('/')

@app.route('/profile/<string:name>')
def get_my_name(name):
    return f'My name is {name}'


app.run()
