from flask import Blueprint, render_template, redirect
from database.models import register_user, check_password
from . import forms

login_bp = Blueprint('login', __name__, url_prefix='/login')


@login_bp.route('/register')
def register_user_app():
    form = forms.RegisterLogin()
    register_user('pavel', 'admin')
    # return render_template('register.html', form=form)
    return redirect('/')


@login_bp.route('/')
def login_user():
    form = forms.RegisterLogin()
    return render_template('login.html', form=form)


@login_bp.route('/check_data', methods=['post'])
def check_login_data():
    form = forms.RegisterLogin()

    name = form.name.data
    password = form.password.data

    checker = check_password(name, password)

    if checker:
        print('прошел проверку')

    else:
        print('не прошел проверку')

    return redirect('/')
