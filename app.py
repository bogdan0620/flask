from flask import Flask, render_template
from main_page.main import main_page_bp

app = Flask(__name__)

app.register_blueprint(main_page_bp)

@app.route('/profile/<string:name>')
def get_my_name(name):
    return f'My name is {name}'








app.run()