from flask import Blueprint, render_template
from database.models import add_problem_db, get_all_problems_db

main_page_bp = Blueprint('main_page', __name__)

@main_page_bp.route('/')
def main_page():
    problems = get_all_problems_db()
    context = {'problems': problems}

    return render_template('index.html', context=context)
