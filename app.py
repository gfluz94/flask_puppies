from my_project import app
from flask import render_template

@app.route("/")
def index():
    return render_template("home.html")

@app.errorhandler(404)
def error404(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)