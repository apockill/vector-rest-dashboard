from flask import render_template


def attach(app):
    @app.route("/")
    def index():
        return render_template("index.html")
