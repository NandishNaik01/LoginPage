from flask import Flask, render_template

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/")
def Home():
    return render_template('home.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route("/forgot")
def forgot():
    return render_template('forgotpass.html')

if __name__ == "__main__":
    app.run(debug=True)
