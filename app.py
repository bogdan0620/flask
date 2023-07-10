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


@app.route('/profile/<string:name>')
def get_my_name(name):
    return f'My name is {name}'


app.run()
