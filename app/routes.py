from flask import render_template, send_from_directory, url_for, render_template_string
from app import app


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404


@app.route('/app-ads.txt')
def download_file():
    return render_template_string('''google.com, pub-9371118693960899, DIRECT, f08c47fec0942fa00''')
