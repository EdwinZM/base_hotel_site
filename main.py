from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/rooms")
def rooms():
    return render_template("rooms.html")

@app.route("/restaurant")
def restaurant():
    return render_template("restaurant.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/reservation")
def reservation():
    return render_template("reservation.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1")