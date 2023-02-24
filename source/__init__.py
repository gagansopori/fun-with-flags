from flask import Flask, render_template, url_for


def create_app(config=None):
    app = Flask(__name__)

    @app.route("/")
    def welcome_page():
        return render_template('index.html')

    return app

